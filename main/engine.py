# coding:utf-8
import signal
from util import conf
from util.timer import Timer
from main.processes import ProcessManager, ProcessArgs

from system.baseSystem import SystemManager
from system.selectSystem import SelectSystem
from system.handlerSystem import HandlerSystem

from entity.serverEntity import ServerEntity


# def init_base_client(sysm):
#     sysm.register_entity(ClientEntity())
#     sysm.register_system(ClientSystem())
#     sysm.update()

def init_server_proc(sysm, share=None):
    '''
    启动服务器 ecs 系统进程
    '''
    if share: ProcessArgs(share)
    sysm.register_entity(ServerEntity())
    sysm.register_system(SelectSystem())
    Timer().add_task(ProcessArgs().heartbeat, conf.DAEMON_HEATBEAT_RATE, True)
    sysm.update()

def init_daemon_proc(share=None):
    '''
    启动守护进程
    '''
    if share: ProcessArgs(share)
    sysm = SystemManager()
    ProcessManager().add_process('server', init_server_proc, (sysm,))
    ProcessManager().run_all_process()
    Timer().add_task(lambda name='server': ProcessManager().check_heartbeat(name), conf.DAEMON_HEATBEAT_RATE, True)
    Timer().run_ever()


if __name__ == '__main__':
    '''
    主程序启动主进程
    '''
    ProcessManager().add_process('server_daemon', init_daemon_proc, ())
    ProcessManager().run_all_process()
    ProcessManager().join_all()
