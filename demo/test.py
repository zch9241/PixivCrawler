import os
import json
class data(object):
    def CREAT(self):
        dir_fd = os.open(path = './pixiv_crawler/data/data', flags = os.O_CREAT)
        os.close(fd = dir_fd)
    def RDWR(self,context):
        dir_fd = os.open(path = './pixiv_crawler/data/data', flags = os.O_RDWR|os.O_CREAT)
        if context:
            os.write(dir_fd, bytes(context ,'utf-8'))
            datas = None
        else:
            datas = os.read(dir_fd)
        os.close(fd = dir_fd)
        return datas

with open('./pixiv_crawler/data/data') as f:
    context = json.load(f)['cookie']

print(context)