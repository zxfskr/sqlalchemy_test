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
_session = None


def get_base():
    return _base


def get_session():
    if _session == None:
        raise NameError("模块未初始化.")
    return _session


def module_init(app):
    global _session, _base
    engine = create_engine(app.config['DB_CONNECT_URL'],
                           pool_size=20, pool_recycle=1800,
                           pool_pre_ping=True, echo=app.config["DB_ECHO"])

    _base.metadata.create_all(engine)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
    _base.to_dict = to_dict

    Session = sessionmaker(bind=engine)
    _session = Session()


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
