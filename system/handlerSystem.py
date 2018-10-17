# coding:utf-8
from system.baseSystem import System
from common.server.commonProtocol import Protocol


class HandlerSystem(System):

    def __init__(self):
        super(HandlerSystem, self).__init__(interest='server', option_interest=['heartbeat'])

    def update(self, comp, option_comp):
        '''
        执行处理包逻辑
        @param comp: 名为 server 的 component
        '''
        for client in comp.client_dict.itervalues():
            for req in Protocol.unpack(client.recv_buff):
                self.handle(req, comp)

    def handle(self, req, comp):
        pass

    def heartbeat(self, hb_com, client):
        hb_com.timeout_window[client] += 1
