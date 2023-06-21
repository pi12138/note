'''
這是一个失败的案例
破解有道词典
爬取信息失败
'''

from urllib import request, parse
import json

# content = input("please a word:")
# url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# 删去'_o'就可以爬取？？？？
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'


data = {
    'i': 'teacher',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1541686273987',
    'sign': '4d33f6a3a03467bbde2f119a98526b2a',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTIME',
    'typoResult': 'false'
}

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
#     'Cookie': 'OUTFOX_SEARCH_USER_ID=730791509@42.231.133.157; OUTFOX_SEARCH_USER_ID_NCOO=88323846.16032994; _ntes_nnid=b3cac80312fb8695af7479132d55c2fe,1535974440367; fanyi-ad-id=52077; fanyi-ad-closed=1; P_INFO=m18790065681; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abckaugSJhOsZhmWVwOBw; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1541684362479'
# }
# data编码
data = parse.urlencode(data).encode()

try:
    # rsp = request.urlopen(url)
    req = request.Request(url, data, method='POST')
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    html = json.loads(html)
    print(html)
except Exception as e:
    print('error:', e)