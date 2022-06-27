# PixivCrawler
这是使用`Python@3.10`编写的的高效爬虫。


- 推荐使用最新版本的软件，以避免发生无法预期的错误 
- 本程序(PixivCrawler)仅供学习交流，最初目的达成后请自行删除，请勿用于商业用途 
- 使用后任何不可知事件都与原作者无关，原作者不承担任何后果 
- 建议使用稳定的梯子，使用V2RayN或Clash for Windows客户端，具体事宜在使用说明具体介绍
- 短时大量请求可能导致IP被短时间封禁，望知悉


## 使用
### 一、运行环境
- Python 3.10
- （建议）Visual Studio Code
- Windows 10/11

### 二、第三方库
```
(cmd)
pip install requests
pip install tqdm
pip install urllib3
```

### 三、配置设置
`config`为程序设置(ln: 216)
- 必选项: cookies, proxies
- 剩余为可选项
- P.S. 代理设置请根据自己客户端的实际情况而定，端口可能会有所改动  `example: 127.0.0.1:xxxx`
```
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
```
