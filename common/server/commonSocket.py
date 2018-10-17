# coding:utf-8
import socket
import ConfigParser
from util.logger import server_logger


class Socket(object):

    def __init__(self, conf):
        cf = ConfigParser.ConfigParser()
        cf.read(conf)
        self.start(
            cf.get('server', 'host'),
            cf.getint('server', 'port'),
            cf.getfloat('option', 'timeout'),
            cf.getint('option', 'backlog')
        )

    def start(self, ip_addr, port, timeout, backlog):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setblocking(False)
        self.timeout = timeout
        self.socket.settimeout(timeout)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        self.socket.bind((ip_addr, port))
        self.socket.listen(backlog)
        server_logger.info('listening on %d' % port)

    def get_timeout(self):
        return self.timeout

    def close(self):
        self.socket.close()
        server_logger.info('server close')