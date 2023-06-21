'''
从浏览器中复制cookie
手动登录人人网个人页面
'''

import requests
import json

def personal_home(url):
    headers = {
        'Cookie': 'anonymid=jo6sr79k40ag06; depovince=GW; _r01_=1; JSESSIONID=abceyx-bq_4DU-9dr6SBw; ick_login=7f43805c-bc93-47ca-b9e0-cecad75ba079; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7C7471263abebbaff7e175aa883e8f567c%7C1541573100604%7C1%7C1541573369733; __utma=151146938.1258973640.1541599502.1541599502.1541599502.1; __utmc=151146938; __utmz=151146938.1541599502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/968602505/profile; BAIDU_SSP_lcr=https://www.baidu.com/link?url=pE-a7TSMRyq0Ar9Y396lh3i-m-aGnH7o5-AnzoNj_wG&wd=&eqid=fe95f5b000001ee6000000025be2eb00; ick=3d978031-223c-4443-b93b-c62e869b0bdc; id=968608156; XNESSESSIONID=01b1c84d8a80; ver=7.0; jebecookies=bc50350a-65b6-44f8-9167-5ffc14c0a7d5|||||; _de=808C2653025A488A50C4B45F09ACB784; p=cad502da1d6f0f4f5570b7a1284858f96; ap=968608156; first_login_flag=1; ln_uact=13193820382; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=11601cd5f861846855e8d4155add337d6; societyguester=11601cd5f861846855e8d4155add337d6; xnsid=4d6e8b0; loginfrom=null; wp_fold=0; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7Cf32e82e144a38fbd54204d837fb67154%7C1541812070496%7C1%7C1541812002419',

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    rsp = requests.get(url, headers = headers)
    print(type(rsp.text))
    data = rsp.text
    
    with open(r'25.html', 'w', encoding='utf-8') as f:
        f.write(data)
        print("write success!")

if __name__ == '__main__':
    url = 'http://www.renren.com/968608156/profile'
    personal_home(url)