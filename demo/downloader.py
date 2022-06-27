import time
import requests
from tqdm import tqdm
import os

def Down():
    s = requests.session()
    chunk_size = 1024 # 每次下载数据区块大小(B)
    res = s.get(
        url = 'https://i.pximg.net/img-original/img/2021/12/08/11/57/01/94641543_p0.jpg', 
        headers = {'referer': 'https://www.pixiv.net'}, 
        #proxies={'http': '127.0.0.1:10809','https': '127.0.0.1:10809'}, #v2ray
        proxies={'http': '127.0.0.1:7890','https': '127.0.0.1:7890'},#clash
        stream=True)
    content_size = int(res.headers['content-length'])
    content_size_ = content_size // 1024
    it = res.iter_content(chunk_size = chunk_size)
    with open('test.jpg', 'wb') as f:
        for chunk in tqdm(
            iterable=it,
            total=content_size_,
            unit='KB',
            desc=None,
            leave=False
            ):

            f.write(chunk)
        f.close()

    #确保文件被完整下载
    local_file_size = list(os.stat('test.jpg'))[6]

