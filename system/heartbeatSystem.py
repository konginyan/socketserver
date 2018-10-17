# coding:utf-8
from system.baseSystem import System


class HeartbeatSystem(System):

    def __init__(self):
        super(HeartbeatSystem, self).__init__(interest='heartbeat')

    def update(self, comp, option_comp):
        for client, heartbeat in comp.timeout_window.iteritems():
            heartbeat -= 1
            if heartbeat == 0:
                comp.dead_clients.append(client)
