# Author: zch9241 <github.com/zch9241><zch2426936965@gmail.com>
# 
# License: Apache-2.0 license
# 
# version: 3.0
# 
# 版权声明: 该软件(PixivCrawler)为「Author」所有，转载请附上本声明。保留所有权利。
# 
# 版本更新说明：
# v1.0: 程序首个版本
# v1.1: 增加下载pixiv限制内容的功能(修改用户headers:请在模块Web.geturl_threads中的geturl类__init__函数中添加你的headers(全部))
# v2.0-Beta: null
# v3.0

import json
import os
import re
import threading
import time

import requests
import urllib3
from tqdm import tqdm


def GetAllPages():
    illust_url_alllangzh = 'https://www.pixiv.net/ajax/user/' + illustrator_id + '/profile/all?lang=zh'
    #https://www.pixiv.net/ajax/user/4405891/profile/all?lang=zh
    html = requests.get(url = illust_url_alllangzh, headers = win_headers, proxies = proxies, verify = False).content.decode('utf-8')
    s = list(json.loads(html)['body']['illusts'].keys())

    print('[GetAllPages(function)]: info: 成功获取插画详情页链接 长度: {}'.format(len(s)))
    return s

def GetUserName():
    global AllPages
    global proxies
    global illustrator_id

    andr_headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,en-US;q=0.6',
        'cookie': cookie,
        'dnt': '1',
        'referer': 'https://www.pixiv.net/artworks/'+ AllPages[0],
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-user-id': '71963925'
    }

    user_url = 'https://www.pixiv.net/touch/ajax/illust/details?illust_id=' + AllPages[0] + '&ref=&lang=zh'
    html = requests.get(url = user_url, headers = andr_headers, proxies = proxies, verify = False).content.decode('utf-8')
    name = json.loads(html)['body']['author_details']['user_name']
    Name = name + '({})'.format(illustrator_id)
    return Name


def GetAllPagePicUrl():
    global AllPages
    global AllOrgPicUrlList
    global proxies

    s = requests.session()

    while len(AllPages) > 0:
        pageurl = AllPages.pop()
        andr_headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,en-US;q=0.6',
        'cookie': cookie,
        'dnt': '1',
        'referer': 'https://www.pixiv.net/artworks/'+ pageurl,
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; FRD-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-user-id': '71963925'
        }

        html_ = s.get('https://www.pixiv.net/touch/ajax/illust/details?illust_id=' + pageurl + '&ref=&lang=zh', headers = andr_headers, proxies = proxies, verify = False).content.decode('utf-8')
        #html_ = requests.get('https://www.pixiv.net/touch/ajax/illust/details?illust_id=94641543&ref=&lang=zh', headers = andr_headers, proxies = proxies).content.decode('utf-8')
        picnum = int(json.loads(html_)['body']['illust_details']['page_count'])
        first_org_pic_url = str(json.loads(html_)['body']['illust_details']['url_big'])
        #https://i.pximg.net/img-original/img/2021/12/08/11/57/01/94641543_p0.jpg
        first_picname = first_org_pic_url.split('/')[-1]
        left_str = first_org_pic_url.replace(first_picname, '')


        AllOrgPicUrlList.append(first_org_pic_url)

        for i in range(1, picnum):
            str_to_del = re.findall(re.compile(r'\_p+(.*?)\.+'), first_picname)[0]
            pic_name = first_picname.replace(str_to_del, str(i))
            AllOrgPicUrlList.append(left_str + pic_name)

def Downloader():
    global AllOrgPicUrlList
    global DownloadFailedUrl
    global proxies
    global user_path
    global chunk_size
    global times

    s = requests.session()
    ThreadName = threading.current_thread().name

    def main_downloader(downloadurl):
        current_len = len(AllOrgPicUrlList)
        filename = downloadurl.split('/')[-1]
        filedownload_path = user_path + filename

        def key():
            """
            验证响应头中是否存在'content-length'字段
            """
            for _ in range(times):
                response = s.get(
                url = downloadurl, 
                headers = {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,en-US;q=0.6',
                    'cache-control': 'max-age=0',
                    'dnt': '1',
                    'referer': 'https://www.pixiv.net',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
                    }, 
                proxies = proxies,
                stream = True,
                verify = False    #ProxyError
                )
                try:
                    response.headers['content-length']
                    break
                except KeyError:
                    time.sleep(5)
                    print('[Downloader-main-key(function)]: warn: 不存在content-length键。重试。 请求: {}'.format(downloadurl))
                    continue
                
            return response
        
        response = key()
        content_size = int(response.headers['content-length'])
            
        content_size_ = content_size // 1024
        it = response.iter_content(chunk_size = chunk_size)
        with open(filedownload_path, 'wb') as f:
            bar = tqdm(
                iterable=it,
                total=content_size_,
                colour = 'blue',
                unit='KB',
                leave=False
                )
            for chunk in bar:
                bar.set_description('{} 正在下载 {} ,还剩 {} '.format(ThreadName, filename, current_len))
                f.write(chunk)
            f.close()

        #确保文件被完整下载
        local_file_size = list(os.stat(filedownload_path))[6]
        if local_file_size < content_size:
            DownloadFailedUrl.append(downloadurl)
            print('[Downloader-main(function)]: warn: {} 未完全下载 ({} / {})'.format(filename, local_file_size, content_size))
        local_file_size = 0


    while len(AllOrgPicUrlList) > 0:
        url = AllOrgPicUrlList.pop()
        main_downloader(downloadurl = url)

    while len(DownloadFailedUrl) > 0:
        url_ = DownloadFailedUrl.pop()
        main_downloader(downloadurl = url_)

    s.close()



class jutils():
    def mk_download_path(path):
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
    def mk_user_path(name):
        try:
            os.mkdir(download_path + name)
        except FileExistsError:
            pass
        user_path = download_path + name + '\\'
        return user_path


if __name__ == '__main__':
    #------------config------------
    #禁用InsecureRequestWarning
    urllib3.disable_warnings(urllib3.connectionpool.InsecureRequestWarning)
    #你的用户cookie
    cookie = ''

    ##代理设置
    #(若使用V2Ray，请用 # 注释Clash for windows相关代理，取消V2Ray的注释)

    # V2Ray
    #proxies = {
    #    'http': '127.0.0.1:10809',
    #    'https': '127.0.0.1:10809'
    #}

    # Clash for windows
    proxies = {
        'http': '127.0.0.1:7890',
        'https': '127.0.0.1:7890'
    }
    #下载文件的保存位置
    download_path = os.getcwd() + '.\\Downloads\\'
    #网页端解析插画链接的线程数
    analysis_thread_num = 5
    #下载线程数
    download_thread_num = 3
    #每次下载的分块
    chunk_size = 1024
    #重试次数
    times = 5
    #------------config------------

    AllOrgPicUrlList = []
    DownloadFailedUrl = []
    analysis_thread_list = []
    download_thread_list = []

    #illustrator_id = '219976'
    illustrator_id = str(input('[main(input)]: 请输入画师id(仅需int类型): '))
    win_headers = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,en-US;q=0.6',
        'cookie': cookie,
        'dnt': '1',
        'referer': 'https://www.pixiv.net/users/' + illustrator_id + '/illustrations?p=1',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'x-kl-ajax-request': 'Ajax_Request',
        'x-user-id': '71963925'
    }

    jutils.mk_download_path(path = download_path)

    AllPages = GetAllPages()
    user_path = jutils.mk_user_path(name = GetUserName())

    for th in range(analysis_thread_num):
        th = threading.Thread(target = GetAllPagePicUrl)
        analysis_thread_list.append(th)
    for a in analysis_thread_list:
        a.start()
    for b in analysis_thread_list:
        b.join()
    

    for th_ in range(download_thread_num):
        th_ = threading.Thread(target = Downloader)
        download_thread_list.append(th_)
    for c in download_thread_list:
        c.start()
    for d in download_thread_list:
        d.join()

    print('[main]: info: 所有插画下载完成...总耗时')

    os.system('pause')

