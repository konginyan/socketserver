# coding:utf-8
from entity.baseEntity import Entity, NotEntityError


class Component(object):

    def __init__(self, sign='base'):
        self.sign = sign

    @classmethod
    def seton(cls, **args):
        def decorate(entity_cls):
            if not issubclass(entity_cls, Entity):
                raise NotEntityError('component_decorate')
            if not entity_cls.coms:
                entity_cls.coms = []
            entity_cls.coms.append((cls, args))
            return entity_cls
        return decorate


class NotComponentError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return 'non-Component class cannot run "%s"' % self.ErrorInfo