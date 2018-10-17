# coding:utf-8
from component.baseComponent import Component
from common.server.commonSocket import Socket
from common.server.commonClient import Client


class SelectComponent(Component):
    '''
    使用 select 方式监听客户端的 socket 服务端
    '''
    def __init__(self, config):
        super(SelectComponent, self).__init__(sign='server')
        self.read_list = []
        self.write_list = []
        self.client_dict = {}
        self.init_socket(config)

    def init_socket(self, conf):
        self.socket_obj = Socket(conf)
        self.socket = self.socket_obj.socket
        self.read_list.append(self.socket)  # 将 socket 加入到监听的列表