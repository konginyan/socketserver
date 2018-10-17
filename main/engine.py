# coding:utf-8
import sys, os
from system.baseSystem import SystemManager
from system.selectSystem import SelectSystem
from system.handlerSystem import HandlerSystem
from system.clientSystem import ClientSystem

from entity.serverEntity import ServerEntity
from entity.clientEntity import ClientEntity


def init_base_client(sysm, conf):
    sysm.register_entity(ClientEntity())
    sysm.register_system(ClientSystem())
    sysm.update()

def init_base_server(sysm, conf):
    sysm.register_entity(ServerEntity())
    sysm.register_system(SelectSystem())
    sysm.update()


if __name__ == '__main__':
    '''
    主函数启动 ecs 系统
    '''
    sysm = SystemManager()

    # 注册 entity
    sysm.register_entity(ServerEntity())

    # 注册 system
    sysm.register_system(SelectSystem())

    # 启动
    sysm.update()