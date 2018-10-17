# coding:utf-8
import socket
from system.baseSystem import System
from util.logger import client_logger
from util import conf


class ClientSystem(System):

    def __init__(self):
        super(ClientSystem, self).__init__(interest='client')

    def update(self, comp, option_comp):
        if comp.status == conf.DISCONNECTED:
            self.do_connect(comp)
    
    def do_connect(self, comp):
        try:
            comp.socket.connect((comp.host, comp.port))
        except socket.error:
            pass
        else:
            comp.status = conf.CONNECTED
            client_logger.info('connect to server %s:%d success' % (comp.host, comp.port))

