def translation(object):
    print('[main-translation(info)]: 转化数据...')
    items = []
    for item in object:
        for i in item:
            items.append(i)
    return items

object = [['https://i.pximg.net/img-original/img/2020/04/26/00/17/55/81061426_p0.png'], ['https://i.pximg.net/img-original/img/2020/03/29/05/55/18/80419758_p0.png'], ['https://i.pximg.net/img-original/img/2020/05/29/00/00/20/81925203_p0.png'], ['https://i.pximg.net/img-original/img/2020/07/31/00/02/41/83334063_p0.png'], ['https://i.pximg.net/img-original/img/2020/04/26/00/13/14/81061279_p0.png'], ['https://i.pximg.net/img-original/img/2021/01/19/00/14/00/87148231_p0.png'], ['https://i.pximg.net/img-original/img/2021/02/14/00/39/27/87747928_p0.png'], ['https://i.pximg.net/img-original/img/2021/03/27/00/26/01/88725735_p0.png'], ['https://i.pximg.net/img-original/img/2021/03/13/00/02/35/88401872_p0.png'], ['https://i.pximg.net/img-original/img/2021/01/15/00/27/13/87054253_p0.png'], ['https://i.pximg.net/img-original/img/2021/05/28/01/33/01/90139664_p0.png'], ['https://i.pximg.net/img-original/img/2021/05/28/01/34/38/90139691_p0.png'], ['https://i.pximg.net/img-original/img/2021/07/05/00/15/07/91020676_p0.png'], ['https://i.pximg.net/img-original/img/2021/04/19/00/30/53/89246716_p0.png'], ['https://i.pximg.net/img-original/img/2021/07/13/00/01/30/91205516_p0.png'], ['https://i.pximg.net/img-original/img/2021/11/04/05/28/48/93109671_p0.jpg'], ['https://i.pximg.net/img-original/img/2021/08/11/00/00/17/91881133_p0.png'], ['https://i.pximg.net/img-original/img/2021/10/04/00/53/33/93209817_p0.png'], ['https://i.pximg.net/img-original/img/2021/11/02/00/05/21/93858219_p0.png'], ['https://i.pximg.net/img-original/img/2021/11/04/05/29/47/93902033_p0.jpg'], ['https://i.pximg.net/img-original/img/2021/11/13/00/00/09/94091950_p0.png',
'https://i.pximg.net/img-original/img/2021/11/13/00/00/09/94091950_p1.png', 'https://i.pximg.net/img-original/img/2021/11/13/00/00/09/94091950_p2.png']]

print(translation(object))