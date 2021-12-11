import os
import queue
import threading


import Web.getpic as getpic
import Web.geturl as geturl
import Web.proxy as proxy


#代理`pac`
proxy.proxy().socks()
queues = queue.Queue()
cookie = ""
thread_num = 5


project_path = os.getcwd()
dir_path = getpic.getpic().makedir()
savepath = str(project_path) + str(dir_path)

uid = str(input('[main(info)]: 要爬取的用户ID: '))

original_urls = geturl.geturl(uid = uid, cookie = cookie).get_allpic_originalurl()

items = len(original_urls)

def threaded_download(url, cookie, savepath):
    """
    # threaded_download
    - url: 要下载的全部url
    - cookie: 用户cookie
    - savepath: 图片存储文件夹
    """
    while True:
        item = queues.get()
        print('[main(info)]: 当前∨: %s' % item)
        url = original_urls.pop()
        print(len(original_urls))
        getpic.getpic().get_main(url = url,cookie = cookie, savepath = savepath)
        queues.task_done()

for t in range(thread_num):
    th = threading.Thread(target = threaded_download, args = (original_urls, cookie, savepath),daemon = True).start()

for item in range(items):
    queues.put(item = item)
queues.join()

#getpic.getpic().get_main(uid = uid, cookie = cookie)

print('[main(info)]: 下载已完成！')
#4103937

