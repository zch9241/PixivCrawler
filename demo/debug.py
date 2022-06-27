
import requests

proxies = {
    'http': '127.0.0.1:7890',
    'https': '127.0.0.1:7890'
}
headers = {'referer': 'https://www.pixiv.net'}
html = requests.get(url= ' https://i.pximg.net/img-original/img/2015/11/11/22/37/04/53503407_p0.jpg',proxies=proxies,headers = headers)
{'Server': 'nginx', 'Date': 'Mon, 27 Jun 2022 03:50:13 GMT', 'Content-Type': 'image/jpeg', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=31536000', 'Expires': 'Tue, 27 Jun 2023 03:50:13 GMT', 'Last-Modified': 'Sat, 17 Dec 2016 15:00:13 GMT', 'X-Content-Type-Options': 'nosniff', 'Age': '0', 'Via': 'http/1.1 f011 (second)'}
{'Server': 'nginx', 'Date': 'Mon, 27 Jun 2022 04:15:16 GMT', 'Content-Type': 'image/jpeg', 'Content-Length': '1051590', 'Connection': 'keep-alive', 'Cache-Control': 'max-age=31536000', 'Expires': 'Tue, 27 Jun 2023 04:07:47 GMT', 'Last-Modified': 'Wed, 11 Nov 2015 13:37:05 GMT', 'X-Content-Type-Options': 'nosniff', 'Age': '310', 'Via': 'http/1.1 f004 (second)', 'Accept-Ranges': 'bytes'}