#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
usingai
"""

import hashlib
import json

from usingai.autoops.utils.redis_helper import get_redis
from ..dao.user_dao import UserDao
from ..models.users import Users
# from webapp.comm.redis_helper import get_redis

# _user_cache = {}


def hash_password(password):
    """
    @summary: 对密码hash后保存
    @param password: 传入str
    @return: pwd.hexdigest() hash后结果
    """
    # password = password.encode('utf8')
    password = 'ai4health_oa_' + password
    password = password.encode('utf8')
    pwd = hashlib.md5()
    pwd.update(password)
    return pwd.hexdigest()


def get_all_user(query: dict):
    """
    @summary: 缓存用户列表
    @param ：
    @return:
    """
    user_dao = UserDao()
    result = user_dao.query_page(query)
    return result


def get_user(userid: int) -> Users:
    """
    @summary: 获取用户
    @param: userid
    @return: user
    """
    user_dao = UserDao()
    result = user_dao.query_by_id(userid)
    return Users(**result) if result else None


def get_cache_user(userid: str) -> Users:
    """
    获取用户。 Session 模块使用。
    """
    redis = get_redis()
    value = redis.get("autoops.user.{}".format(userid))
    if value:
        value = value.decode("utf8")
        # user = User.from_json(value.decode("utf8"))
        
        user = Users(**value)
        # print("get: ", user.__dict__)
        return user
    else:
        return None
    # return _user_cache.get(userid, None)


def get_user_by_name(username: str, password: str) -> Users:
    """
    @summary: 查看用户是否存在。 登录时使用。
    @param: username
    @param: password
    @return: user
    """
    user_dao = UserDao()
    result = user_dao.query_all_users(username, hash_password(password))[0]
    if result:
        # user = Users(**result)
        # _user_cache[user.get_id()] = user
        redis = get_redis()
        redis.set("autoops.user.{}".format(result.id), result.to_dict())
        # print("set: ", user.__dict__)
        return result
    else:
        return None


def confirm_password(plain_pwd: str, hex_pwd: str) -> bool:
    """
    检查当前用户密码
    """
    return hex_pwd == hash_password(plain_pwd)


def check_user_exist(username: str) -> bool:
    """
    检查用户名是否已存在
    """
    user_dao = UserDao()
    result = user_dao.query_all_users({"username": username})
    if result:
        return len(result) > 0
    else:
        return False
    # return user_dao.check_user_exist(username)


def new_user(username: str, displayname: str, password: str, userlevel: int = 1) -> dict:
    """
    @summary: 新建用户
    @param: username
    @param: password
    @param: userlevel
    @return: entity
    """

    entity = {
        "username": username,
        "displayName": displayname,
        "password": hash_password(password),
        "userLevel": userlevel
    }
    user_dao = UserDao()
    
    userid = user_dao.insert_one(Users(**entity))
    entity["id"] = userid

    return entity


def update_user(userid: int, displayname: str) -> int:
    """
    @summary: 修改用户
    @param: displayname
    """
    sql = {
        "id": userid,
        "displayName": displayname
    }
    user_dao = UserDao()
    result = user_dao.update_one_by_id(userid, Users(**sql))

    text_id = str(userid)
    # if text_id in _user_cache:
    #     _user_cache[text_id].displayName = displayname
    redis = get_redis()
    value = redis.get("autoops.user.{}".format(text_id))
    if value:
        output = json.loads(value.decode("utf8"))
        output["displayName"] = displayname
        redis.set("autoops.user.{}".format(text_id), json.dumps(output))

    return result


def delete_user(userid: int) -> int:
    """
    @summary: 删除用户
    @param: userid
    """
    user_dao = UserDao()
    return user_dao.delete_one_by_id(userid)


def change_pwd(userid: int, password: str) -> int:
    """
    用户修改密码
    """
    info = {
        "id": userid,
        "password": hash_password(password)
    }
    user_dao = UserDao()
    result = user_dao.update_one_by_id(userid, Users(**info))
    return result
