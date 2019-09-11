"""
数据库 工具类
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import DATETIME

from datetime import datetime, timezone
from typing import Callable
from sqlalchemy import create_engine, MetaData, types
from sqlalchemy.dialects.mysql import DATETIME

from sqlalchemy.engine import Engine

_base = declarative_base()
_engine = None


def get_base():
    return _base


def get_session():
    if _engine == None:
        raise NameError("模块未初始化.")
    Session = sessionmaker(bind=_engine)
    return Session()


def module_init(app):
    global _engine, _base
    _engine = create_engine(app.config['DB_CONNECT_URL'],
                           pool_size=1, pool_recycle=1800,
                           pool_pre_ping=True, echo=app.config["DB_ECHO"])

    _base.metadata.create_all(_engine)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    _base.to_dict = to_dict


class UTCDateTime(types.TypeDecorator):
    """
    Datetime 转换解析类
    """

    impl = DATETIME(fsp=6)

    def process_bind_param(self, value, dialect):
        # print(value)
        if value is not None:
            return value.astimezone(timezone.utc)

        return None

    def process_result_value(self, value, dialect):
        if value is not None:
            return datetime(value.year, value.month, value.day,
                            value.hour, value.minute, value.second,
                            value.microsecond, tzinfo=timezone.utc)

        return None
