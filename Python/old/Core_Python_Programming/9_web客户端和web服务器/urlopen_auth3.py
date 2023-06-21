import urllib.request, urllib.error, urllib.parse

LOGIN = 'wesley'
PASSWD = "you'llNeverGuess"
URL = 'http://localhost'
REALM = 'Secure Archive'


def handler_version(url):
    hdlr = urllib.request.HTTPBasicAuthHandler()
    hdlr.add_password(REALM, urllib.parse.urlparse(url)[1], LOGIN, PASSWD)
    opener = urllib.request.build_opener(hdlr)
    urllib.request.install_opener(opener)

    return url

def request_version(url):
    # from base64 import encodestring
    from base64 import encodebytes

    req = urllib.request.Request(url)
    b64str = encodebytes(bytes('{}:{}'.format(LOGIN, PASSWD), 'utf-8'))[:-1]
    # b64str = encodestring(bytes('{}:{}'.format(LOGIN, PASSWD), 'utf-8'))[:-1]
    req.add_header('Authorization', "Basic {}".format(b64str))

    return req

for funcType in ('handler', 'request'):
    print('*** Using {}:'.format(funcType.upper()))
    url = eval('{}_version'.format(funcType))(URL)
    f = urllib.request.urlopen(url)
    print(str(f.readline(), 'utf-8'))
    f.close()