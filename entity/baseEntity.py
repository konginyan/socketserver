# coding:utf-8

class Entity(object):

    coms = []

    def __init__(self):
        self.components = {}
        self.init()

    def init(self):
        for com in self.__class__.coms:
            com_instance = com[0](**com[1]) if com[1] else com[0]()
            self.register_component(com_instance.sign, com_instance)

    def register_component(self, name, component):
        self.components[name] = component

    def get_component(self, name):
        try:
            return self.components[name]
        except KeyError:
            return None


class NotEntityError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return 'non-Entity class cannot run "%s"' % self.ErrorInfo