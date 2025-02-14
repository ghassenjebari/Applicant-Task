import datetime
from pydantic import ConfigDict, BaseModel
from typing import Optional, Dict, Any


""" User """


class User(BaseModel):
    id: int
    name: str
    role: str
    created_at: datetime.datetime
    last_login: datetime.datetime
    is_active: bool
    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    name: str
    role: str


class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[str] = None
    is_active: Optional[bool] = None


""" Part """


class Part(BaseModel):
    id: int
    name: str
    comment: str #Comment section
    created_at: datetime.datetime
    created_by: User
    model_config = ConfigDict(from_attributes=True)


class PartCreate(BaseModel):
    name: str
    comment: str #Comment section


class PartUpdate(BaseModel):
    name: Optional[str] = None
    comment: str #Comment section

""" History """


class History(BaseModel):
    id: int
    tableName: str
    user: User
    createdAt: datetime.datetime
    action: str
    input: Dict[Any, Any] = None
    output: Dict[Any, Any] = None
    model_config = ConfigDict(from_attributes=True)


class HistoryCreate(BaseModel):
    tableName: str
    userID: int
    action: str
    input: Dict[Any, Any] = None
    output: Dict[Any, Any] = None
