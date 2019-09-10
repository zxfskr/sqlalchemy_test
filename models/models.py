from sqlalchemy import Column, Integer, String, SmallInteger, BigInteger, JSON

from .db_helper import UTCDateTime, get_base

class Models(get_base()):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    datastreamId = Column("datastreamId", BigInteger)
    createdBy = Column("createdBy", BigInteger)
    createTime = Column("createTime", UTCDateTime())
    stats = Column("stats", SmallInteger)
    name = Column("name", String(64))
    config = Column("config", JSON)
    completeTime = Column("completeTime", UTCDateTime())
    modelPath = Column("modelPath", String(64))
    
    def __repr__(self):
        return "name: %s" % (self.__tablename__)