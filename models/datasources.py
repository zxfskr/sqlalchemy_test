from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger

from .db_helper import UTCDateTime, get_base


class Datasources(get_base()):
    __tablename__ = "datasources"
    id = Column(Integer, primary_key=True)
    type = Column("type", SmallInteger)
    protocol = Column("protocol", String(16))
    host = Column("host", String(64))
    port = Column("port", Integer)
    username = Column("username", String(16))
    password = Column("password", String(32))
    elementTemplateName = Column("elementTemplateName", String(32))
    createdBy = Column("createdBy", BigInteger)
    createTime = Column("createTime", UTCDateTime())
    updatedBy = Column("updatedBy", BigInteger)
    updateTime = Column("updateTime", UTCDateTime())
    
    def __repr__(self):
        return "name: %s" % (self.__tablename__)
