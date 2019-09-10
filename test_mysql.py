from usingai.common.application import app
import config
from usingai.autoops.utils import db_helper
from usingai.autoops.services import models_service

# app.config.from_object(config)
# app.config.from_pyfile('config.py', silent=True)
# app.config.from_envvar('APP_CONFIG_FILE', silent=True)

DB_CONNECT_URL = "mysql+pymysql://root:123456@192.168.5.250:13306/autoops_cycle"
DB_ECHO = False

app.config["DB_CONNECT_URL"] = DB_CONNECT_URL
app.config["DB_ECHO"] = DB_ECHO

db_helper.module_init(app)

r = models_service.get_models_by_id(2)
print(r)