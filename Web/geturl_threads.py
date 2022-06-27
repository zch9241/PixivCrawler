import json
import queue
import requests
import threading
import time


class geturl(object):
    """
    # get
    - uid: 画师id
    - cookie: 你的cookie (1)all?lang=zh;(2)details?illust_id=***&ref=&lang=zh
    """
    def __init__(self, uid):
        self.headers = {
            'accept': 'application/json',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en,en-US;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'cookie': 'first_visit_datetime_pc=2022-01-03+13%3A15%3A32; p_ab_id=6; p_ab_id_2=0; p_ab_d_id=1472835414; yuid_b=QEmAJ2I; privacy_policy_agreement=3; c_type=22; privacy_policy_notification=0; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=71963925=1^9=p_ab_id=6=1^10=p_ab_id_2=0=1^11=lang=zh=1; PHPSESSID=71963925_2UK0nnz2gOuCOJM24va7PZLsOZZukXvx; device_token=09a4ab004ad51c02f7d70cd321cce048; __utmz=235335808.1655889206.115.5.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; _ga=GA1.2.118181462.1641183337; __utma=235335808.118181462.1641183337.1656050938.1656050938.143; _ga_75BBYNYN9J=GS1.1.1656050644.2.1.1656051748.0; tag_view_ranking=RTJMXD26Ak~uusOs0ipBx~9ODMAZ0ebV~Lt-oEicbBr~jhuUT0OJva~LJo91uBPz4~KvAGITxIxH~RNN9CgGExV~r0q4yFTWtg~BSkdEJ73Ii~QLvl6kE4lC~D0nMcn6oGk~vLP3DMasD_~75zhzbk0bS~2bq8SNVWly~eVxus64GZU~cFYMvUloX0~VLDgZNuX1x~VSI71mhgdM~nQRrj5c6w_~Xs-7j6fVPs~Cc23GhmKNc~GX7J0_CPTv~Mg6bq-SpX8~PwDMGzD6xn~mFW848gK6h~pa4LoD4xuT~LVSDGaCAdn~jH0uD88V6F~ETjPkL0e6r~K8esoIs2eW~v7Qz4joCBq~sb_gmFpDzp~-sp-9oh8uv~kGYw4gQ11Z~lH5YZxnbfC~BtXd1-LPRH~t2ErccCFR9~jyw53VSia0~2pZ4K1syEF~1Xn1rApx2-~hW_oUTwHGx~qWFESUmfEs~G04tXVOkHP~_pwIgrV8TB~0xsDLqCEW6~aKhT3n4RHZ~vSWEvTeZc6~E9anU9DdS_~OOsvVvWvg6~HLWLeyYOUF~zASPXsXKdt~v6KNtCPEKI~CrFcrMFJzz~Ptpn09xujs~nRp2ZLPLbj~4ZEPYJhfGu~KkXUHnIeIl~66pgV3BU1a~TV3I2h_Vd8~gzY20gtW1F~ykNnpw2uh5; __cf_bm=xnT.Q_v5mVa0XPLLYLZVLqbl8oE.qcPjL_Cw_MUEZUQ-1656238091-0-AQ5QOCt54+RIUssD/j8Kkax0s3fqSvcOYcqR8roOBGEYQKnjQLA3ZlaGt2V8ERTLsNxVJy+x1ybZxw2Bw7X1d4CN+sG+XLnQ1MTv3m2/zjgnp6QJhZmp+P7U8t5sEm7TkwBaa11x0sh7KLKTy8jwK/y44DLjgm8owJwE14p+MYAMV6pWLG/7KogYr8noo2/TDQ==',
            'dnt': '1',
            'referer': 'https://www.pixiv.net/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
            'x-user-id': '71963925'
        }
        self.headers_details = {
            
        }
        self.uid = uid


    def get_allurl(self):
        """
        # get_allurl
        return: 画师的全部插画url
        """
        print('[geturl-getallurl(info)]: 加载中...')
        picurl_all = requests.get(url = "https://www.pixiv.net/ajax/user/" + self.uid +"/profile/all?lang=zh", headers = self.headers)
        resdict = json.loads(picurl_all.content)['body']['illusts']
        return [key for key in resdict]

    def get_eachpic_originalurl(self, pid):
        """
        # get_eachpic_originalurl
        - pids: 插画id
        """
        resdicts = []
        #获取接口数据

        #print('[geturl-get_eachpic_originalurl(info)]: 正在获取(id):',pid,end = '')

        url = "https://www.pixiv.net/touch/ajax/illust/details?illust_id=" + pid + "&ref=https%3A%2F%2Fwww.pixiv.net%2Fusers%2F" + self.uid + "&lang=zh"
        pic_details = requests.get(url = url,headers = self.headers)
        #获取该页下的插画数量（若为多张，则将"p0"改为"px"）
        pagenum_response = json.loads(pic_details.content)['body']['illust_details']['page_count']
            
        # pagenum_response的返回值为str类型
        if pagenum_response == '1':
            #print('{<%s>}' % pagenum_response)
            resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
            resdicts.append(resdict)
        else:
            #print('<%s>' % pagenum_response)
            resdict = json.loads(pic_details.content)['body']['illust_details']['url_big']
            resdicts.append(resdict)
            for num in range(1, int(pagenum_response)):
                resdict_more = resdict.replace('p0','p' + str(num)) #改为str类型，避免报错
                resdicts.append(resdict_more)
        return resdicts

    def get_allpic_originalurl(self, thread_num):
        """
        # get_allpic_originalurl
        - thread_num: 线程数量
        """
        print('[geturl-get_allpic_originalurl(info)]: 加载中...')

        queues = queue.Queue()
        orginalurl_list = []
        #获取画师插画id
        allurls = geturl(uid = self.uid).get_allurl()

        print("[geturl-get_allpic_originalurl(info)]: 插画队列长度: ", len(allurls))
        items = len(allurls)

        def threaded_get():
            #获取所有原图url
            while True:
                item = queues.get()
                url = allurls.pop()
                time.sleep(0.1)
                originalurl = geturl(uid = self.uid).get_eachpic_originalurl(pid = url)
                #print(originalurls)
                orginalurl_list.append(originalurl)
                queues.task_done()
        print('[geturl-get_allpic_originalurl(info)]: %s 个线程启动...' % int(thread_num))
        for t in range(int(thread_num)):
            th = threading.Thread(target = threaded_get, daemon = True).start()
        for item in range(items):
            queues.put(item = item)
        queues.join()
        print('[geturl-get_allpic_originalurl(info)]: 数据收集完成...')
        return orginalurl_list
