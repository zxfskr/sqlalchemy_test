import sqlalchemy
from sqlalchemy import create_engine
from pprint import pprint
from usingai.common.application import app
from datetime import timezone, timedelta
import logging
import logging.config

from common.utils.db_helper import get_session, module_init
from common.services import user_service
from common.models.users import Users
from common.dao.user_dao import UserDao

import config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger('web')


def main():
    # print(sqlalchemy.__version__)

    # Base = declarative_base()
    app.config.from_object(config)
    app.config.from_pyfile('config.py', silent=True)
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)
    print("start init")
    module_init(app)
    user = Users(username="1")
    print(user.to_dict())
    # user_service.get_user_by_name()



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(e)