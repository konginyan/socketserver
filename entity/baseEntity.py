# coding:utf-8

class Entity(object):

    coms = []

    def __init__(self):
        self.components = {}
        self.init()

    def init(self):
        for com in self.__class__.coms:
            self.register_component(com[0], com[1])

    def register_component(self, name, component):
        self.components[name] = component

    def get_component(self, name):
        return self.components[name]


class NotEntityError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return 'non-Entity class cannot run "%s"' % self.ErrorInfo