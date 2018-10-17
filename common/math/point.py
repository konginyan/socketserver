# coding:utf-8


class Grid(object):

    INF = -1

    def __init__(self, weight, reachable):
        self.cost = Grid.INF
        self.weight = weight
        self.previous = None
        self.reachable = reachable
    
    def visited(self):
        return self.cost == Grid.INF


class Position(object):

    INVAILD = -1

    def __init__(self, x=Position.INVAILD, y=Position.INVAILD):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def isvaild(self):
        return not (self.x == Position.INVAILD or self.y == Position.INVAILD)
    
    def set_invaild(self):
        self.x=Position.INVAILD
        self.y=Position.INVAILD
