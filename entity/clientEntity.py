# coding:utf-8
from entity.baseEntity import Entity
from component.clientComponent import ClientComponent
from util.conf import CLIENT_CONF


@ClientComponent.seton(config=CLIENT_CONF)
class ClientEntity(Entity):

    def __init__(self):
        super(ClientEntity, self).__init__()