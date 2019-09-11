"""
redis 工具类
"""
import redis


def module_init(app) -> None:
    """
    注册
    """
    init_redis(host=app.config["REDIS_HOST"],
               port=app.config["REDIS_PORT"], db=app.config["REDIS_DB_INDEX"])


_REDIS_POOL = None


def init_redis(host: str, port: int, db: int) -> None:
    """
    初始化 redis
    """
    global _REDIS_POOL
    _REDIS_POOL = redis.ConnectionPool(host=host, port=port, db=db)


def get_redis() -> redis.Redis:
    """
    获取 redis 实例
    """
    return redis.Redis(connection_pool=_REDIS_POOL)
