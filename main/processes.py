# coding:utf-8
from multiprocessing import Process
from multiprocessing.sharedctypes import Array
from util.singleton import singleton
from util import conf


@singleton
class ProcessManager(object):
    '''
    多进程管理
    '''

    def __init__(self):
        self.processes = {}
        self.share = {}
        self.process_args = {}

    def add_process(self, name, target, args):
        new_share = Array('i', [0 for _ in xrange(3)])
        new_share[conf.DAEMON_HEATBEAT] = 3
        new_share[conf.DAEMON_FEEDBACK] = 0
        new_share[conf.DAEMON_COMMAND] = 0
        self.share[name] = new_share
        self.processes[name] = Process(target=target, args=args + (new_share,))
        if name not in self.process_args.keys():
            self.process_args[name] = (target, args)

    def check_heartbeat(self, name):
        print 2
        if self.share[name][conf.DAEMON_HEATBEAT] > 0:
            self.share[name][conf.DAEMON_HEATBEAT] -= 1
        else:
            self.restart_process(name)

    def restart_process(self, name):
        if self.processes[name].is_alive():
            self.stop_process(name)
            del self.processes[name]
            del self.share[name]
        self.add_process(name, self.process_args[name][0], self.process_args[name][1])
        self.run_process(name)

    def get_process_arg(self, name, arg):
        return self.share[name][arg]

    def run_process(self, name):
        self.processes[name].start()

    def run_all_process(self):
        for pro in self.processes.itervalues():
            pro.start()

    def join_all(self):
        for pro in self.processes.itervalues():
            pro.join()

    def stop_process(self, name):
        if name in self.processes:
            self.processes[name].terminate()

    def stop_all_process(self):
        for pro in self.processes.itervalues():
            pro.terminate()


@singleton
class ProcessArgs(object):
    '''
    跨进程的共享数据储存和操作
    '''

    def __init__(self, args=[]):
        self.args = args # 进程共享参数

    def heartbeat(self):
        print 1
        self.args[conf.DAEMON_HEATBEAT] += 1

    def get_feedback(self):
        return self.args[conf.DAEMON_FEEDBACK]

    def get_command(self):
        return self.args[conf.DAEMON_COMMAND]
