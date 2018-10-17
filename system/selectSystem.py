# coding:utf-8
import select
from system.baseSystem import System
from common.server.commonClient import Client
from util.logger import server_logger


class SelectSystem(System):

    def __init__(self):
        super(SelectSystem, self).__init__(interest='server')

    def update(self, comp, option_comp):
        '''
        执行 select 逻辑
        @param comp: selectComponent
        '''
        readable, writable, exceptional = select.select(comp.read_list, comp.write_list, comp.read_list, comp.socket_obj.get_timeout())
        for so in exceptional:
            self.do_except(so, comp)

        for so in readable:
            if so is comp.socket:
                self.do_accept(comp)
            else:
                self.do_read(comp.client_dict[so])

        for so in writable:
            self.do_write(comp.client_dict[so])


    def do_accept(self, comp):
        conn, addr = comp.socket.accept()
        comp.client_dict[conn] = Client(conn, addr, 1024)
        comp.read_list.append(conn)
        server_logger.info('connected by socket %s:%d' % (addr[0], addr[1]))

    def do_read(self, client):
        client.recv()

    def do_write(self, client):
        client.send_all()

    def do_except(self, so, comp):
        comp.client_dict[so].close()  # 删除对象对 connection(so) 的引用
        so.close()  # 断开连接
        del comp.client_dict[so]  # 删除 client_dict(so) 元素
        comp.read_list.remove(so)  # 删除 select 中 read_list
