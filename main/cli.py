# coding:utf-8
import fire
import sys
sys.path.append('.')

from main import engine
from util import conf
from system.baseSystem import SystemManager


class Command(object):

    def __init__(self):
        pass

    def start_server(self, conf=conf.SERVER_CONF):
        sysm = SystemManager()
        engine.init_server_proc(sysm, conf)

    # def start_client(self, conf=conf.CLIENT_CONF):
    #     sysm = SystemManager()
    #     engine.init_base_client(sysm, conf)


fire.Fire(Command)