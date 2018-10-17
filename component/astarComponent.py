from component.baseComponent import Component
from common.math.point import Grid, Position


class AstarComponent(Component):
    '''
    A* 算法寻路
    '''
    
    def __init__(self, map, diag_able):
        super(AstarComponent, self).__init__(sign='navigate')
        self.start = Position()
        self.goal = Position()
        self.diag_able = diag_able
        self.map = map
        self.width = len(map)
        self.height = len(map[0])
        self.solution = None
        self.init_grid()

    def init_grid(self):
        for x in self.width:
            for y in self.height:
                reachable = self.map[x][y] > 0
                self.map[x][y] = Grid(1, reachable)

    def get_curruent_grid(self, cur):
        return self.map[cur.x][cur.y] if cur.isvaild() else None

    def find_surround_pos(self, cur):
        grids =[]
        if cur.x - 1 >= 0 and cur.y - 1 >= 0 and self.diag_able:
            grids.append(Position(cur.x-1, cur.y-1))  # up-left
        if cur.y - 1 >= 0:
            grids.append(Position(cur.x, cur.y-1))  # up
        if cur.x + 1 < self.width and cur.y - 1 >= 0 and self.diag_able:
            grids.append(Position(cur.x+1, cur.y-1))  # up-right
        if cur.x - 1 >= 0:
            grids.append(Position(cur.x-1, cur.y))  # left
        if cur.x + 1 < self.width:
            grids.append(Position(cur.x+1, cur.y))  # right
        if cur.x - 1 >= 0 and cur.y + 1 < self.height and self.diag_able:
            grids.append(Position(cur.x-1, cur.y+1))  # down-left
        if cur.y + 1 < self.height:
            grids.append(Position(cur.x, cur.y+1))  # down
        if cur.x + 1 < self.width and cur.y + 1 < self.height and self.diag_able:
            grids.append(Position(cur.x+1, cur.y+1))  # down-right
        return grids
