# -*- coding: utf-8 -*-
"""
注意： 如要更改配置，请修改此文件
"""
import os


##############################
# mysql 相关
##############################
DB_CONNECT_URL = "mysql+pymysql://root:123456@192.168.5.106:63306/test_db"
DB_ECHO = False

##############################
# redis 相关
##############################
REDIS_HOST = "192.168.5.250"
REDIS_PORT = 16379
REDIS_DB_INDEX = 2