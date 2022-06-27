import re

str_to_del = re.findall(re.compile(r'\_p+(.*?)\.+'), 'https://i.pximg.net/img-original/img/2021/12/08/11/57/01/94641543_p0.jpg')
print(str_to_del)