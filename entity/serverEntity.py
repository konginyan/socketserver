# coding:utf-8
from entity.baseEntity import Entity
from component.selectComponent import SelectComponent
from component.heartbeatComponent import HeartbeatComponent

@SelectComponent.decorate
@HeartbeatComponent.decorate
class ServerEntity(Entity):

    def __init__(self):
        super(ServerEntity, self).__init__()

if __name__ == '__main__':
    s = ServerEntity()