# coding: utf-8

import os

import leancloud
from wsgiref import simple_server

import cloud
from app import app

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])


leancloud.init(APP_ID, master_key=MASTER_KEY)

application = cloud.engine


if __name__ == '__main__':
    # 只在本地开发环境执行的代码
    app.debug = True
    cloud.load_tasks()
    server = simple_server.make_server('localhost', PORT, application)
    server.serve_forever()
