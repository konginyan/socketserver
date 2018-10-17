# coding:utf-8
from component.baseComponent import Component
from common.math.point import Position


class MoveComponent(Component):
    '''
    物体移动组件
    '''
    def __init__(self, config):
        super(MoveComponent, self).__init__(sign='move')
        self.start = Position()
        self.pos = Position()
        self.speed = 0.0  # grid per second
        self.target = Position()
