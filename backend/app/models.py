from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import JSONB, JSON

from .database import Base
import logging

logging.basicConfig(level=logging.ERROR)


class User(Base):
    __tablename__ = 'User'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    role: Mapped[str] = mapped_column(String(), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), nullable=False)
    last_login: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)


class Part(Base):
    __tablename__ = 'Part'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, unique=True,)
    comment: Mapped[str] = mapped_column(String(), nullable=False)  # Comment field added
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),
                                                 server_default=func.now(), nullable=False)
    created_by: Mapped[User] = relationship(User)
    created_by_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('User.id'), nullable=False)


class History(Base):
    """
    Table to keep track of changes to the DB
    """
    __tablename__ = 'History'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tableName: Mapped[str] = mapped_column(String(), nullable=False)
    userID: Mapped[int] = mapped_column(
        Integer, ForeignKey('User.id'), nullable=False)
    createdAt = mapped_column(DateTime(timezone=True),
                              server_default=func.now(), nullable=False)
    action: Mapped[str] = mapped_column(String(), nullable=False)
    input: Mapped[Optional[JSON]] = mapped_column(JSONB)
    output: Mapped[Optional[JSON]] = mapped_column(JSONB)

    user: Mapped['User'] = relationship(User)
  