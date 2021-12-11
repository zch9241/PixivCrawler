import json
import requests


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
        print('[geturl-getallurl(info)]: 加载中...（若时间过长，请重启程序）')
        picurl_all = requests.get(url = "https://www.pixiv.net/ajax/user/" + self.uid +"/profile/all?lang=zh", headers = self.headers, verify = False)
        resdict = json.loads(picurl_all.content)['body']['illusts']
        return [key for key in resdict]

    def get_eachpic_originalurl(self, pids):
        """
        # get_eachpic_originalurl
        - pids: 插画id
        """
        print('[geturl-get_eachpic_originalurl(info)]: 加载中（时间可能较长）...')
        resdicts = []
        # 获取接口数据
        for pid in pids:
            print('[geturl-get_eachpic_originalurl(info)]: 正在获取(id):',pid,end = '')

            url = "https://www.pixiv.net/touch/ajax/illust/details?illust_id=" + pid + "&ref=https%3A%2F%2Fwww.pixiv.net%2Fusers%2F" + self.uid + "&lang=zh"
            try:
                pic_details = requests.get(url = url,headers = self.headers)
            except requests.exceptions.SSLError:
                while True:
                    print('[geturl-get_eachpic_originalurl(warn)]: <SSLEOFError> 重新连接...')
                    pic_details = pic_details = requests.get(url = url,headers = self.headers)
            
            #获取该页下的插画数量（若为多张，则将"p0"改为"px"）
            pagenum_response = json.loads(pic_details.content)['body']['illust_details']['page_count']
            
            # pagenum_response为str类型
            if pagenum_response == '1':
                print('{<%s>}' % pagenum_response)
                resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
                resdicts.append(resdict)
            else:
                print('<%s>' % pagenum_response)
                resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
                resdicts.append(resdict)
                for num in range(1, int(pagenum_response) + 1):
                    resdict_more = resdict.replace('p0','p' + str(num)) #改为str类型，避免报错
                    resdicts.append(resdict_more)
        
        return resdicts

    def get_allpic_originalurl(self):
        """
        # get_allpic_originalurl
        """
        print('[geturl-get_allpic_originalurl(info)]: 加载中...')
        #获取画师插画id
        allurls = geturl(uid = self.uid,cookie = self.cookie).get_allurl()

        print("[geturl-get_allpic_originalurl(info)]: 插画队列长度: ", len(allurls))

        #获取所有原图url
        originalurls = geturl(uid = self.uid,cookie = self.cookie).get_eachpic_originalurl(pids = allurls)
        print(originalurls)

        return originalurls