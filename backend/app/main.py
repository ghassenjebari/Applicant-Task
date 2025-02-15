from fastapi import FastAPI, Request, Depends
from typing import List
from . import settings, models, schemas, crud, errors
from .database import SessionLocal, engine
import logging

from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.exception_handlers import (
    http_exception_handler
)

app = FastAPI(root_path=settings.API_ROOT_PATH)

origins = [
    "http://localhost",
    "http://localhost:5001",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# get root logger
# the __name__ resolve to "main" since we are at the root of the project.
logging.basicConfig(level=logging.ERROR)


def get_db():
    # Dependency
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" Error Handling """


@app.exception_handler(errors.NotFoundError)
async def not_found_error_handler(request: Request, exc: errors.NotFoundError):
    """
    This method converts a NotFoundError from the crud part to an HTTPException error
    """
    return await http_exception_handler(request, exc)


@app.exception_handler(errors.NotUniqueError)
async def not_unique_error_handler(request: Request, exc: errors.NotUniqueError):
    """
    This method converts a NotUniqueError from the crud part to an HTTPException error
    """
    return await http_exception_handler(request, exc)


def add_mock_data():
    add_admin_user()

    db = SessionLocal()
    # Get the created admin user
    admin = crud.User.get_by_name(db, 'admin')

    # Add some mock parts
    crud.Part.create(db, schemas.PartCreate(
        name='Engine',
        comment="Main engine for propulsion" 
    ), admin)
    crud.Part.create(db, schemas.PartCreate(
        name='Tank',
        comment="Fuel tank" 
    ), admin)
    crud.Part.create(db, schemas.PartCreate(
        name='Fairing',
        comment="Payload fairing" 
    ), admin)
    crud.Part.create(db, schemas.PartCreate(
    name='Booster',
    comment="Solid rocket booster for additional thrust"
), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Avionics',
    comment="Flight control and navigation systems"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Payload Bay',
    comment="Compartment for carrying satellites or cargo"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Interstage',
    comment="Connects rocket stages and allows for separation"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Thrust Vector Control',
    comment="System for controlling engine direction"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Heat Shield',
    comment="Protects from atmospheric re-entry heat"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Grid Fins',
    comment="Used for aerodynamic control during descent"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Reaction Control System',
    comment="Thrusters for fine attitude control"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='LOX Tank',
    comment="Liquid oxygen tank for combustion"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Fuel Lines',
    comment="Transfers fuel from tanks to engines"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Landing Legs',
    comment="Deployable legs for soft landings"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Escape Tower',
    comment="Emergency crew escape system"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Oxidizer Tank',
    comment="Stores oxidizer needed for combustion"
    ), admin)

    crud.Part.create(db, schemas.PartCreate(
    name='Telemetry System',
    comment="Transmits flight data to ground stations"
    ), admin)


    return


def add_admin_user():
    # necessary for get_by_name function of admin user when adding normal users
    db = SessionLocal()

    users = [
        models.User(
            name='admin',
            role='admin',
        ),
    ]
    try:
        crud.User.get_by_name(db, 'admin')
    except errors.NotFoundError:
        db.add_all(users)
        db.commit()
        db.close()
    return


@app.on_event("startup")
def startup_event(db: Session = Depends(get_db)):
    # Uncomment this to add some test data for testing. Warning: deletes all data.
    if settings.ENV_MODE == 'DEV':
        models.Base.metadata.drop_all(bind=engine)
        models.Base.metadata.create_all(bind=engine)
        add_mock_data()
    return


""" Users """


def get_current_user(
    db: Session = Depends(get_db),
    # token: str = Depends(oauth2_scheme)
) -> models.User:

    return crud.User.get_by_name(db, 'admin')


@app.get(
    "/users",
    response_model=List[schemas.User],
    tags=['Users'])
def get_users(
    db: Session = Depends(get_db),
):
    return crud.User.get_all(db)


""" Parts """


@app.get(
    "/parts/{id}",
    response_model=schemas.Part,
    tags=['Parts'])
def get_part_by_id(
    id: int,
    db: Session = Depends(get_db)
):
    return crud.Part.get_by_id(db, id)

@app.get(
    "/parts",
    response_model=List[schemas.Part],
    tags=['Parts'])
def get_parts(
    db: Session = Depends(get_db)
):
    return crud.Part.get_all(db)

@app.post(
    "/parts",
    response_model=schemas.Part,
    tags=['Parts'])
def create_part(
    obj_in: schemas.PartCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud.Part.create(db, obj_in, user)


@app.patch(
    "/parts/{id}",
    response_model=schemas.Part,
    tags=['Parts'])
def update_part(
    id: int,
    obj_in: schemas.PartUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return crud.Part.update(db, id, obj_in, user)


""" Debug """


@app.get(
    "/",
    tags=['Test'])
def root():
    return {"message": "Hello World"}
