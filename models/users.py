from sqlalchemy import text, Column, Integer, String, SmallInteger, BigInteger, UnicodeText, DateTime, TIMESTAMP
from sqlalchemy.dialects.mysql import DATETIME, TIMESTAMP
from .db_helper import UTCDateTime, get_base

class Users(get_base()):
    __tablename__ = "users"
    id = Column("id", BigInteger, primary_key=True)
    username = Column("username", String(64), nullable=False)
    password = Column("password", String(64), nullable=False)
    displayName = Column("displayName", String(64), nullable=False)
    userLevel = Column("userLevel", SmallInteger, server_default="1")
    stats = Column("stats", SmallInteger, server_default="1")
    createTime = Column("createTime", UTCDateTime(), server_default=text("NOW()"))

    def __repr__(self):
        return "name: %s" % (self.__tablename__)
