# coding:utf-8
from entity.baseEntity import Entity
from component.astarComponent import AstarComponent
from component.moveComponent import MoveComponent


@AstarComponent.seton()
@MoveComponent.seton()
class PlayerEntity(Entity):

    def __init__(self):
        super(PlayerEntity, self).__init__()
