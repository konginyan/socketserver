# coding:utf-8
import socket
import ConfigParser
from component.baseComponent import Component
from util import conf


class ClientComponent(Component):
    '''
    客户端用 component
    '''

    def __init__(self, config):
        super(ClientComponent, self).__init__(sign='client')
        self.status = conf.DISCONNECTED
        self.init_socket(config)

    def init_socket(self, conf):
        cf = ConfigParser.ConfigParser()
        cf.read(conf)
        self.host = cf.get('server', 'host')
        self.port = cf.getint('server', 'port')
        self.timeout = cf.getfloat('option', 'timeout')
        self.socket = socket.socket()
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.settimeout(self.timeout)
