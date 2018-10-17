# coding:utf-8
import Queue
from system.baseSystem import System


class AstarSystem(System):

    def __init__(self):
        super(AstarSystem, self).__init__(interest='navigate', option_interest=['move'])

    def update(self, comp, option_comp):
        if comp.start.isvaild() and comp.goal.isvaild():
            comp.solution = self.locate(comp)
            if option_comp.has_key('move'):
                pass
            comp.start.set_invaild()
            comp.goal.set_invaild()

    def locate(self, comp):
        visited = Queue.Queue(comp.width * comp.height)
        comp.start.cost = 0
        visited.put(comp.start)

        while not visited.empty():
            cur = visited.get_nowait()
            cur_grid = comp.get_curruent_grid(cur)
            if cur == comp.goal:
                return cur  # 得到最优解

            next_pos = comp.find_surround_pos(cur)
            for pos in next_pos:
                next_grid = comp.get_curruent_grid(pos)
                if next_grid.reachable:
                    new_cost = cur_grid.cost + next_grid.weight
                    if next_grid.visited() or new_cost < next_grid.cost:
                        next_grid.previous = cur
                        visited.put(pos)

        return None  # 无法到达
