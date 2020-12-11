# -*- coding: utf8 -*-
import requests 
from bs4 import BeautifulSoup

def pushinfo(info,specific):
    headers={   
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'ContentType': 'text/html'
    }
    requests.session().get("https://sc.ftqq.com/SCU115905Tbf2fb0877564b2e119d4c1ad98e00f065f72eb61909c9SCKEY.send?text=" + info + "&desp=" + specific,headers=headers)


def main(*args):
    headers={
        'Cookie': 'htVD_2132_saltkey=iXcejXqj; htVD_2132_lastvisit=1607688097; BAIDU_SSP_lcr=https://www.baidu.com/link?url=wAJy93H90lrcoCAxQOmtZmNxZJhWruca2oZIxkUv7vp9CoQ7tYuT3_6faU_1Qyro&wd=&eqid=de2fcab400000541000000065fd36ee1; Hm_lvt_46d556462595ed05e05f009cdafff31a=1607692007; htVD_2132_con_request_uri=https%3A%2F%2Fwww.52pojie.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dindex.php; htVD_2132_client_created=1607692041; htVD_2132_client_token=2425F77E4C2DC830967C2662F3E90C13; htVD_2132_ulastactivity=1607692041%7C0; htVD_2132_auth=48d7gM2cp26Dw03M5zs2ggaSNkpuDiySbPuAx6mQW0SRjlEEXFsehk1TDeP3fB6sqcMc7b%2FKmwMsRdNcB9p5XXQFB5JW; htVD_2132_connect_login=1; htVD_2132_connect_is_bind=1; htVD_2132_connect_uin=2425F77E4C2DC830967C2662F3E90C13; htVD_2132_stats_qc_login=3; htVD_2132_sid=0; htVD_2132_checkpm=1; htVD_2132_lastcheckfeed=1041729%7C1607692042; htVD_2132_checkfollow=1; htVD_2132_nofavfid=1; htVD_2132_lastact=1607692051%09home.php%09task; Hm_lpvt_46d556462595ed05e05f009cdafff31a=1607692052' ,
        'ContentType':'text/html;charset=gbk'
    }
    requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2',headers=headers)
    a=requests.session().get('https://www.52pojie.cn/home.php?mod=task&do=draw&id=2',headers=headers)
    b=BeautifulSoup(a.text,'html.parser')          
    c=b.find('div',id='messagetext').find('p').text

    if "您需要先登录才能继续本操作"  in c: 
        pushinfo("Cookie失效", c)
    elif "恭喜"  in c:
        pushinfo("吾爱破解签到成功",c)
    else:
        pushinfo("吾爱破解签到失败",c)
    print(c)


if __name__ == '__main__':
    main()
