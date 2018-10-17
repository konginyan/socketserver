# coding:utf-8
from util import conf


class Protocol(object):

    end_flag = '//'

    def __init__(self):
        self.version = 1.0
        self.header = {}
        self.params = {}

    def check_str(self):
        for key, value in self.header.iteritems():
            if (isinstance(key, str) and Protocol.end_flag in key) or (isinstance(value, str) and Protocol.end_flag in value):
                raise ProtocolError('"%s" is not allow in value' % Protocol.end_flag)

        for key, value in self.params.iteritems():
            if (isinstance(key, str) and Protocol.end_flag in key) or (isinstance(value, str) and Protocol.end_flag in value):
                raise ProtocolError('"%s" is not allow in value' % Protocol.end_flag)

    def pack(self):
        self.check_str()
        header_raw = ''.join('%s:%s' % (key, str(value)) for (key, value) in self.header.iteritems())
        params_raw = ''.join('%s:%s' % (key, str(value)) for (key, value) in self.params.iteritems())
        return ''.join('%d;%s;%s%s' % (self.version, header_raw, params_raw, Protocol.end_flag))

    @staticmethod
    def unpack(req):
        if Protocol.end_flag not in req:
            pass
        else:
            yield req


class ProtocolError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return self.ErrorInfo