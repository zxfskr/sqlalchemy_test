"""
mongodb 工具类
"""
from typing import Callable
from pymongo import MongoClient
from pymongo.collection import Collection
from bson.codec_options import CodecOptions


def module_init(app) -> None:
    """
    注册
    """
    init_mongodb(app.config["MONGODB_URL"], app.config["MONGODB_DATABASE"],
                 app.config["MONGODB_USER"], app.config["MONGODB_PASSWORD"])


_DB = None
_HAS_INIT = False
_INIT_LIST = []


def init_mongodb(url: str, database: str, username: str, password: str) -> None:
    """
    初始化 mongodb
    """
    global _DB, _INIT_LIST, _HAS_INIT

    client = MongoClient(url)
    db = client[database]
    db.authenticate(
        name=username,
        password=password
    )
    _DB = db
    if not _HAS_INIT:
        _HAS_INIT = True
        for func in _INIT_LIST:
            func()
        _INIT_LIST.clear()


def get_collection(collection: str) -> Collection:
    """
    获取 mongodb collection
    """
    global _DB
    # 在数据中标志时区信息
    options = CodecOptions(tz_aware=True)
    return _DB.get_collection(collection, codec_options=options)


def add_init_callback(init_func: Callable) -> None:
    """
    mongodb 初始化回调注册
    """
    global _HAS_INIT, _INIT_LIST
    if _HAS_INIT:
        init_func()
    else:
        _INIT_LIST.append(init_func)
