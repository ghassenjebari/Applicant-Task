from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

from fastapi.encoders import jsonable_encoder

from . import models, schemas
from typing import ClassVar, Generic, List, Type, TypeVar
from . import database
from pydantic import BaseModel
import logging

from .errors import NotFoundError, NotUniqueError
# Define placeholder types for models and schemas
# Only subtypes of the base types are allowed
ModelType = TypeVar("ModelType", bound=database.Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

"""
This file contains a class for each model and a base class
defining basic CRUD (create, read, update & delete) functions
"""

# get root logger
# the __name__ resolve to "main" since we are at the root of the project.
logging.basicConfig(level=logging.ERROR)


class CRUDBase(Generic[ModelType, SchemaType, CreateSchemaType, UpdateSchemaType]):
    """
    Base class to implement generic functions that are the same for all models
    """
    _model: ClassVar[Type[ModelType]]

    @classmethod
    def get_by_id(cls, db: Session, id: int) -> ModelType:
        """
        Get object by unique id
        @id: unique id of object
        """
        obj = db.query(cls._model).filter(cls._model.id == id).one_or_none()
        if obj is None:
            raise NotFoundError(
                "{} with id=\'{}\' was not found.".format(
                    cls._model.__name__, id)
            )
        return obj

    @classmethod
    def get_all(cls, db: Session) -> List[ModelType]:
        return db.query(cls._model).all()

    @classmethod
    def create(cls, db: Session, obj_in: CreateSchemaType, user: models.User) -> ModelType:
        """
        Create an object in db
        @obj_db: Object to be created
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_db = cls._model(**obj_in_data)  # type: ignore
        # Add user in case it is required in model
        if (hasattr(obj_db, 'created_by_id')):
            obj_db.created_by_id = user.id
        db.add(obj_db)
        try:
            db.commit()
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):

                # Extract column name and value from error message
                msg: str = e.orig.args[0]
                detail = msg.split('\n')[1]
                res = re.findall("\((.*?)\)", detail)

                raise NotUniqueError(
                    "{} with {}=\'{}\' already exists.".format(
                        cls._model.__name__, res[0], res[1])
                )
        db.refresh(obj_db)

        # Create history entry
        History.create(db, schemas.HistoryCreate(
            tableName=cls._model.__name__,
            userID=user.id,
            action='create',
            input={
                'obj_in': obj_in
            },
            output=jsonable_encoder(obj_db)
        ))

        return obj_db

    @classmethod
    def __update__(cls, db: Session, obj_db: ModelType, obj_in: UpdateSchemaType, user: models.User) -> ModelType:
        """
        Internal function of CRUDBase to update an object in db

        Check if object exists needs to be done before
        @obj_db: object in database
        @obj_in: schema of parameters to be changed
        """

        obj_data = jsonable_encoder(obj_db)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(obj_db, field, update_data[field])
        db.add(obj_db)
        try:
            db.commit()
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                # Catch UniqueViolation Error from psycopg2 and format the output
                # Extract column name and value from error message
                msg: str = e.orig.args[0]
                detail = msg.split('\n')[1]
                res = re.findall("\((.*?)\)", detail)

                raise NotUniqueError(
                    "{} with {}=\'{}\' already exists.".format(
                        cls._model.__name__, res[0], res[1])
                )
        db.refresh(obj_db)

        # Create history entry
        History.create(db, schemas.HistoryCreate(
            tableName=cls._model.__name__,
            userID=user.id,
            action='update',
            input={
                'obj_db': obj_db,
                'obj_in': obj_in
            },
            output=jsonable_encoder(obj_db)
        ))

        return obj_db

    @classmethod
    def update(cls, db: Session, id: int, obj_in: UpdateSchemaType, user: models.User) -> ModelType:
        """
        Update an object referenced by id with given parameters
        @obj_in: Parameters to change
        """
        # Get object that should be update by id
        try:
            obj_db = cls.get_by_id(db, id)
        except NotFoundError as e:
            # Catch if object not found and extend exception
            raise NotFoundError(
                '{} with id={} could not be updated, because '.format(
                    cls._model.__name__, id) + e.detail
            ) from e
        return cls.__update__(db, obj_db, obj_in, user)


"""
Create a class for every model and insantiate an object
"""


class User(
    CRUDBase[
        models.User,
        schemas.User,
        schemas.UserCreate,
        schemas.UserUpdate
    ],
):
    _model = models.User

    @classmethod
    def get_by_name(cls, db: Session, name: str) -> models.User:
        user = db.query(models.User).filter(
            models.User.name == name
        ).one_or_none()

        if user is None:
            raise NotFoundError(
                "User with name=\'{}\' was not found.".format(
                    cls._model.__name__, name)
            )
        return user


class Part(
    CRUDBase[
        models.Part,
        schemas.Part,
        schemas.PartCreate,
        schemas.PartUpdate
    ],
):
    _model = models.Part


class History():
    """
    Track all changing methods on database tables
    """
    @classmethod
    def get_all(cls, db: Session) -> List[models.History]:
        return db.query(models.History).all()

    @classmethod
    def create(cls, db: Session, obj_in: schemas.HistoryCreate) -> models.History:
        """
        Create a history object
        """
        obj_in_data = jsonable_encoder(obj_in)
        obj_db = models.History(**obj_in_data)  # type: ignore
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db
