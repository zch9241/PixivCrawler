# pixiv_crawler_urllib
这是使用`Python@3.8`编写的的高效爬虫。


- 推荐使用最新版本的软件，以避免发生无法预期的错误 
- 本程序(pixiv_crawler)仅供学习交流，最初目的达成后请自行删除，请勿用于商业用途 
- 使用后任何不可知事件都与原作者无关，原作者不承担任何后果 
- 请使用V2Ray版本<=4.31.0，`Shadowsocks`类型，代理`pac`模式进行连接
- main.py使用`urllib`下载，较不稳定。推荐使用_main.py下载插画链接后使用其他下载软件（如`IDM`）下载


### 使用

1.安装第三方库
```
pip install requests
pip install urllib
pip install pyperclip
```

2.打开main.py
- 输入你的cookies(位于(Chrome内核浏览器)F12->应用->Cookie-> " https://www.pixiv.net " ->名称为`PHPSESSID`的值)（注意保护隐私信息）
- 输入下载线程数（默认为5）

3.运行软件
