import json
import queue
import requests
import threading
import time


class geturl(object):
    """
    # get
    - uid: 画师id
    - cookie: 你的cookie 提示:位于(Chrome内核浏览器)F12->应用->Cookie-> " https://www.pixiv.net " ->名称为`PHPSESSID`的值
    """
    def __init__(self, uid, cookie):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept-Language": "zh-CN,zh;q=0.9", 
            "Dnt": "1", 
            "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36", 
            "Cookie": str(cookie)
        }
        self.uid = uid
        self.cookie = cookie

    def get_allurl(self):
        """
        # get_allurl
        return: 画师的全部插画url
        """
        print('[geturl-getallurl(info)]: 加载中...')
        picurl_all = requests.get(url = "https://www.pixiv.net/ajax/user/" + self.uid +"/profile/all?lang=zh", headers = self.headers)
        resdict = json.loads(picurl_all.content)['body']['illusts']
        return [key for key in resdict]

    def get_eachpic_originalurl(self, pid):
        """
        # get_eachpic_originalurl
        - pids: 插画id
        """
        resdicts = []
        #获取接口数据

        #print('[geturl-get_eachpic_originalurl(info)]: 正在获取(id):',pid,end = '')

        url = "https://www.pixiv.net/touch/ajax/illust/details?illust_id=" + pid + "&ref=https%3A%2F%2Fwww.pixiv.net%2Fusers%2F" + self.uid + "&lang=zh"
        pic_details = requests.get(url = url,headers = self.headers)
        #获取该页下的插画数量（若为多张，则将"p0"改为"px"）
        pagenum_response = json.loads(pic_details.content)['body']['illust_details']['page_count']
            
        # pagenum_response的返回值为str类型
        if pagenum_response == '1':
            #print('{<%s>}' % pagenum_response)
            resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
            resdicts.append(resdict)
        else:
            #print('<%s>' % pagenum_response)
            resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
            resdicts.append(resdict)
            for num in range(1, int(pagenum_response)):
                resdict_more = resdict.replace('p0','p' + str(num)) #改为str类型，避免报错
                resdicts.append(resdict_more)
        return resdicts

    def get_allpic_originalurl(self, thread_num):
        """
        # get_allpic_originalurl
        - thread_num: 线程数量
        """
        print('[geturl-get_allpic_originalurl(info)]: 加载中...')

        queues = queue.Queue()
        orginalurl_list = []
        #获取画师插画id
        allurls = geturl(uid = self.uid, cookie = self.cookie).get_allurl()

        print("[geturl-get_allpic_originalurl(info)]: 插画队列长度: ", len(allurls))
        items = len(allurls)

        def threaded_get():
            #获取所有原图url
            while True:
                item = queues.get()
                url = allurls.pop()
                time.sleep(0.1)
                originalurl = geturl(uid = self.uid, cookie = self.cookie).get_eachpic_originalurl(pid = url)
                #print(originalurls)
                orginalurl_list.append(originalurl)
                queues.task_done()
        print('[geturl-get_allpic_originalurl(info)]: %s 个线程启动...' % int(thread_num))
        for t in range(int(thread_num)):
            th = threading.Thread(target = threaded_get, daemon = True).start()
        for item in range(items):
            queues.put(item = item)
        queues.join()
        print('[geturl-get_allpic_originalurl(info)]: 数据收集完成...')
        return orginalurl_list
