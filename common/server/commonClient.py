# coding:utf-8


class Client(object):

    def __init__(self, conn, addr, buff_size):
        self.connection = conn
        self.address = addr
        self.recv_buff = ''
        self.send_buff = ''
        self.send_frame_buff = ''
        self.broadcast_buff = ''
        self.buff_size = buff_size

    def recv(self):
        msg = self.connection.recv(self.buff_size)
        self.recv_buff = ''.join([self.recv_buff, msg])

    def send(self):
        pass

    def send_frame(self):
        pass

    def broadcast(self):
        pass

    def send_all(self):
        self.send()
        self.send_frame()
        self.broadcast()

    def close(self):
        self.connection = None