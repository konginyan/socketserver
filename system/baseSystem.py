# coding:utf-8
from entity.baseEntity import Entity, NotEntityError
from util.timer import Timer
from util.conf import PER_FRAME


class System(object):

    def __init__(self, interest, option_interest=[]):
        self.interest = interest
        self.option_interest = option_interest

    def scan(self, entity):
        option_comp = {}
        for interest in self.option_interest:
            option_comp[interest] = entity.get_component(interest)

        if self.interest in entity.components.keys():
            self.update(entity.get_component(self.interest), option_comp)

    def update(self, comp, option_comp):
        raise NotImplementedError


class NotSystemError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.ErrorInfo = ErrorInfo

    def __str__(self):
        return 'non-System class cannot run "%s"' % self.ErrorInfo


class SystemManager(object):

    def __init__(self):
        self.systems = []
        self.entities = []

    def register_system(self, system):
        if not isinstance(system, System):
            raise NotSystemError('register_system')
        self.systems.append(system)

    def register_entity(self, entity):
        if not isinstance(entity, Entity):
            raise NotEntityError('register_entity')
        self.entities.append(entity)

    def scan(self):
        for sy in self.systems:
            for en in self.entities:
                sy.scan(en)

    def update(self):
        timer = Timer()
        timer.add_task(self.scan, PER_FRAME, True)
        timer.run_ever()