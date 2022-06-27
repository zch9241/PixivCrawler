# Author: zch9241 <github.com/zch9241><zch2426936965@gmail.com>
# 
# 版权声明：该软件（pixiv_crawler）为「zch」所有，转载请附上本声明。保留所有权利。
# Apache 2.0
# 
# version: 1.1
# 
# 版本更新说明：
# v1.0 程序首个版本
# v1.1 增加下载pixiv限制内容的功能(修改用户headers:请在模块Web.geturl_threads中的geturl类__init__函数中添加你的headers(全部))
# 
# 注意：该main.py无下载功能，最后复制链接到剪贴板（若无效，请打开downloadurl（记事本）复制链接），请使用IDM或其它软件下载
# 

import pyperclip


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
#proxy.proxy().socks()

thread_num = 10 #设置线程数（默认为10）


uid = str(input('[main(info)]: 要爬取的用户ID: '))

original_urls = geturl.geturl(uid = uid).get_allpic_originalurl(thread_num)
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

