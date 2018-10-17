# coding:utf-8
from system.baseSystem import System


class FsyncSystem(System):

    def __init__(self):
        super(FsyncSystem, self).__init__(interest='fsync', option_interest=['server'])

    def update(self, comp, option_comp):
        '''
        将帧广播出去
        '''
        for client in option_comp['server'].client_dict.itervalues():
            all_frame = ''.join(frame for frame in comp.frame_list)
            client.send_frame_buff += all_frame
            option_comp['server'].write_list.append(client.connection)