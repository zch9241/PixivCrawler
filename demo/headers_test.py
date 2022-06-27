raw = """
:authority: www.pixiv.net
:method: GET
:path: /ajax/user/4405891/profile/all?lang=zh
:scheme: https
accept: application/json
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7,en-US;q=0.6
cookie: first_visit_datetime_pc=2022-01-03+13%3A15%3A32; p_ab_id=6; p_ab_id_2=0; p_ab_d_id=1472835414; yuid_b=QEmAJ2I; privacy_policy_agreement=3; c_type=22; privacy_policy_notification=0; a_type=0; b_type=1; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=71963925=1^9=p_ab_id=6=1^10=p_ab_id_2=0=1^11=lang=zh=1; PHPSESSID=71963925_2UK0nnz2gOuCOJM24va7PZLsOZZukXvx; device_token=09a4ab004ad51c02f7d70cd321cce048; __utmz=235335808.1655889206.115.5.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; __cf_bm=xnT.Q_v5mVa0XPLLYLZVLqbl8oE.qcPjL_Cw_MUEZUQ-1656238091-0-AQ5QOCt54+RIUssD/j8Kkax0s3fqSvcOYcqR8roOBGEYQKnjQLA3ZlaGt2V8ERTLsNxVJy+x1ybZxw2Bw7X1d4CN+sG+XLnQ1MTv3m2/zjgnp6QJhZmp+P7U8t5sEm7TkwBaa11x0sh7KLKTy8jwK/y44DLjgm8owJwE14p+MYAMV6pWLG/7KogYr8noo2/TDQ==; __utmc=235335808; _ga=GA1.2.118181462.1641183337; _gid=GA1.2.1166170450.1656238608; tag_view_ranking=RTJMXD26Ak~uusOs0ipBx~9ODMAZ0ebV~Lt-oEicbBr~jhuUT0OJva~LJo91uBPz4~KvAGITxIxH~RNN9CgGExV~K8esoIs2eW~r0q4yFTWtg~BSkdEJ73Ii~QLvl6kE4lC~D0nMcn6oGk~vLP3DMasD_~75zhzbk0bS~2bq8SNVWly~eVxus64GZU~cFYMvUloX0~4QveACRzn3~FgXjOGAbwK~VLDgZNuX1x~VSI71mhgdM~nQRrj5c6w_~Xs-7j6fVPs~Cc23GhmKNc~GX7J0_CPTv~Mg6bq-SpX8~PwDMGzD6xn~mFW848gK6h~pa4LoD4xuT~LVSDGaCAdn~jH0uD88V6F~ETjPkL0e6r~v7Qz4joCBq~sb_gmFpDzp~-sp-9oh8uv~kGYw4gQ11Z~lH5YZxnbfC~BtXd1-LPRH~Itu6dbmwxu~t2ErccCFR9~jyw53VSia0~2pZ4K1syEF~1Xn1rApx2-~hW_oUTwHGx~qWFESUmfEs~G04tXVOkHP~_pwIgrV8TB~0xsDLqCEW6~aKhT3n4RHZ~vSWEvTeZc6~E9anU9DdS_~OOsvVvWvg6~HLWLeyYOUF~zASPXsXKdt~v6KNtCPEKI~CrFcrMFJzz~Ptpn09xujs~nRp2ZLPLbj~4ZEPYJhfGu~KkXUHnIeIl~66pgV3BU1a~TV3I2h_Vd8~gzY20gtW1F~ykNnpw2uh5; _ga_75BBYNYN9J=GS1.1.1656238578.3.1.1656238617.0; __utma=235335808.118181462.1641183337.1656238620.1656238620.153
dnt: 1
referer: https://www.pixiv.net/users/4405891/illustrations?p=1
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36
x-kl-ajax-request: Ajax_Request
x-user-id: 71963925
"""

print(raw.split(': '))
