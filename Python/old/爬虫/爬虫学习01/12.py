# 使用cookie爬取

from urllib import request, error

url = 'http://www.renren.com/968602505/profile'
# 设置请求头中的cookie
headers = {
    'Cookie':'anonymid=jo6sr79k40ag06; depovince=GW; _r01_=1; JSESSIONID=abceyx-bq_4DU-9dr6SBw; ick_login=7f43805c-bc93-47ca-b9e0-cecad75ba079; t=d08a96e004756fa380b281cfdd4a438c5; societyguester=d08a96e004756fa380b281cfdd4a438c5; id=968602505; xnsid=1316c59f; jebecookies=8d0ea731-ba5d-4b0e-ae1a-9a73f9c6001e|||||; wp_fold=0; jebe_key=677bb307-0e02-4841-bef6-440071dd690f%7C7471263abebbaff7e175aa883e8f567c%7C1541573100604%7C1'
}

try:
    # 传入网址和请求头
    req = request.Request(url, headers = headers)

    res = request.urlopen(req)
    html = res.read()
    html = html.decode('utf-8',)

    with open("12.html", 'w', encoding='UTF-8') as f:
        f.write(html)

except Exception as e:
    print('error:', e)



