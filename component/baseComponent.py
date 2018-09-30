# coding:utf-8
from entity.baseEntity import Entity, NotEntityError


class Component(object):

    def __init__(self):
        pass

    @classmethod
    def decorate(cls, entity_cls):
        if not issubclass(entity_cls, Entity):
            raise NotEntityError('component_decorate')
        if not entity_cls.coms:
            entity_cls.coms = []
        entity_cls.coms.append((cls.__name__[0:-len('Component')], cls()))
        return entity_cls