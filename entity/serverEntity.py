# coding:utf-8
from entity.baseEntity import Entity
from component.selectComponent import SelectComponent
from component.heartbeatComponent import HeartbeatComponent
from component.fsyncComponent import FsyncComponent
from util.conf import SERVER_CONF


@SelectComponent.seton(config=SERVER_CONF)
@HeartbeatComponent.seton()
@FsyncComponent.seton()
class ServerEntity(Entity):

    def __init__(self):
        super(ServerEntity, self).__init__()
