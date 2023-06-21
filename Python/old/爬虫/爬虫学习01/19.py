# var t = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10));
# salt: t
# sign: n.md5("fanyideskweb" + e + t + "6x(ZHw]mwzX#u0V7@yfwK")
# 分析：
#       e代表要翻译的字符串
#       
#
from urllib import request, parse
import time
import random
import hashlib
import json



def getSalt():
    salt1 = int(time.time() * 1000)
    salt2 = random.randint(0, 10)

    salt = str(salt1) + str(salt2)

    return salt


def getSign(content, salt):
    sign1 = 'fanyideskweb'
    sign4 = '6x(ZHw]mwzX#u0V7@yfwK'
    sign2 = content
    sign3 = salt
    
    # 此处不用哈希也能爬取？？？？
    # sign = sign1 + sign2 + sign3 + sign4
    sign = hashlib.md5((sign1 + sign2 + sign3 + sign4).encode()).hexdigest()

    return sign


if __name__ == '__main__':
    content = input("please a word:")

    salt = getSalt()
    sign = getSign(content, salt)

    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    data = parse.urlencode(data).encode()
    # print(data)
    try:
        # 去掉'_o'才能爬取？？？？为什么
        # url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        # print('1')
        req = request.Request(url, data = data, headers = headers, method = 'POST')
        # print('2')
        rsp = request.urlopen(req)
        # print('3')
        html = rsp.read().decode()
        html = json.loads(html)
        # print('4')
        print(html)
        # print("5")

    except Exception as e:
        print("error:", e)