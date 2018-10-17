# coding:utf-8
from system.baseSystem import System
from util.conf import PER_FRAME


class MoveSystem(System):

    def __init__(self):
        super(MoveSystem, self).__init__(interest='move', option_interest=['fsync'])

    def update(self, comp, option_comp):
        if comp.pos.isvaild() and comp.start.isvaild() and comp.target.isvaild():
            if comp.pos == comp.target:
                comp.start.set_invaild()
                comp.target.set_invaild()

            elif comp.pos == comp.start and option_comp.has_key('fsync'):
                option_comp['fsync'].frame_list.append(None)

            else:
                distance = comp.speed * PER_FRAME
                comp.pos.x += (comp.target.x - comp.start.x) * distance
                comp.pos.y += (comp.target.x - comp.start.y) * distance