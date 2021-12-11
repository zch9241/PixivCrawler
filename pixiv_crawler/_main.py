#该main.py无下载功能，最后复制链接到剪贴板，请使用IDM或其它软件下载

import pyperclip

import Web.getpic as getpic
import Web.geturl_threads as geturl
import Web.proxy as proxy


def translation(object):
    print('[main-translation(info)]: 转换数据...')
    items = []
    for item in object:
        for i in item:
            items.append(i)
    return items

#代理`pac`
proxy.proxy().socks()
cookie = ""
thread_num = 5


uid = str(input('[main(info)]: 要爬取的用户ID: '))

original_urls = geturl.geturl(uid = uid, cookie = cookie).get_allpic_originalurl(thread_num)
downloadurl = translation(object = original_urls)

with open('./pixiv_crawler/downloadurl','r+') as f:
    for string in downloadurl:
        f.write(string)
        f.write('\r\n')
    f.close()

with open('./pixiv_crawler/downloadurl','r') as f:
    copies = f.read()

pyperclip.copy(copies)

#print(original_urls)
print('[main(info)]: 已下载链接！')
#4103937

