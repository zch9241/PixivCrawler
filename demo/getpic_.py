#单线程备份
import os
import time
from urllib import request
from urllib import error

import Web.geturl as geturl
import Web.proxy as proxy


#代理`pac`
proxy.proxy().socks()

class getpic(object):
    def makedir(self):
        """
        # makedir
        - 根据当前时间创建文件夹以存储图片
        """
        try:
            os.mkdir("./pixiv_crawler/pic")
        except FileExistsError:
            pass

        time_now = time.strftime('[%j] %H-%M-%S',time.localtime())
        dir_path = "./pixiv_crawler/pic/" + time_now
        os.mkdir(dir_path)
        dir__path = dir_path.replace('.','')
        dir___path = dir__path.replace('/','\\')
        return str(dir___path) + '\\'

    def get_main(self, uid, cookie):
        """
        # get_main
        - 远程下载图片
        - uid: 要爬取的用户ID
        - cookie: 你的cookie 提示：位于(Chrome内核浏览器)F12->应用->Cookie-> " https://www.pixiv.net " ->名称为`PHPSESSID`的值
        """
        project_path = os.getcwd()
        dir_path = getpic().makedir()
        #获取原图链接
        original_urls = geturl.geturl(uid = uid, cookie = cookie).get_allpic_originalurl()

        for original_url in original_urls:
            opener=request.build_opener()
            #headers
            opener.addheaders=[("User-Agent", "Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36")]
            opener.addheaders=[("Cookie", str(cookie))]
            opener.addheaders=[("Referer", "https://www.pixiv.net")]

            request.install_opener(opener)

            pic_name = original_url.split(sep = "/")[-1]

            rel_path = str(project_path) + str(dir_path) + str(pic_name)

            print('[getpic-main(info)]: 正在下载: ', pic_name)
            getpic().auto_down(url = original_url ,filename = rel_path)
            #request.urlretrieve(url = original_url,filename = rel_path)
    def auto_down(self, url, filename):
        """
        # auto_down
        - 避免下载的图片不完整
        """
        try:
            request.urlretrieve(url,filename)
        except error.ContentTooShortError:
            print('[getpic-auto_down(warn)]: 下载不完整，重新连接...')
            getpic().auto_down(url,filename)

