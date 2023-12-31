from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.sql import func
from app.db.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    full_name = Column(String)


class UserFollowing(Base):
    __tablename__ = "user_following"

    user_pk_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    following_pk_id = Column(String, ForeignKey("users.id"), primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now())
    unfollowed = Column(Boolean)

    __table_args__ = (
        PrimaryKeyConstraint('user_pk_id', 'following_pk_id'),
    )


class UserFollower(Base):
    __tablename__ = "user_followers"

    user_pk_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    follower_pk_id = Column(String, ForeignKey("users.id"), primary_key=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now())
    unfollowed = Column(Boolean)

    __table_args__ = (
        PrimaryKeyConstraint('user_pk_id', 'follower_pk_id'),
    )
