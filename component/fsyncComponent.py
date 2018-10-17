# coding:utf-8
from component.baseComponent import Component


class FsyncComponent(Component):
    '''
    采用帧同步
    '''

    def __init__(self):
        super(FsyncComponent, self).__init__(sign='fsync')
        self.frame_list = []
