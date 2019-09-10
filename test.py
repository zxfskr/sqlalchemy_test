import sqlalchemy
from sqlalchemy import create_engine
from pprint import pprint
from usingai.common.application import app
from datetime import timezone, timedelta
import logging
import logging.config

from models.db_helper import module_init, get_base, get_session
from models.datasources import Datasources
from models.users import Users
from models.models import Models

import config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger('web')


def main():
    print(sqlalchemy.__version__)

    # Base = declarative_base()

    print("start init")
    module_init(app)
    session = get_session()
    session.add_all([
        Users(username="root", password=123456, displayName="管理员用户")
    ])

    print(session.new)
    # input()
    session.commit()

    result = session.query(Users).filter_by(username="root").first()
    # print(result)
    print(result.to_dict())
    tmp = result.to_dict()
    # time = tmp["createTime"]
    # print(time.timestamp())
    # print(time.replace(tzinfo=timezone(timedelta(hours=0))))
    # print(time.replace(tzinfo=timezone(timedelta(hours=0))).timestamp())
    # print(time.astimezone(timezone.utc))
    # print(result.__table__)
    # print(session.dirty)
    # print(app.config)
    # print(Datasources.__table__)

    # Base = get_base()
    # print(Base.__subclasses__())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(str(e))