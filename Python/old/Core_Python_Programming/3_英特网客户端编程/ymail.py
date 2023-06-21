from io import StringIO
from imaplib import IMAP4_SSL
from platform import python_version
from poplib import POP3_SSL, error_proto
from socket import error


release = python_version()
if release > '2.6.2':
    from smtplib import SMTP_SSL, SMTPServerDisconnected
else:
    SMTP_SSL = None

SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'
IMAP4SVR = 'imap.qq.com'

from_addr = '1558255789@qq.com'
to_addr = '2059233910@qq.com'
passwd = 'ngqedkkpiesqjeie'

headers = [
    'From: {}'.format(from_addr),
    'To: {}'.format(', '.join(to_addr)),
    'Subject: test SMTP send via 465/SSL',
]
body = [
    'hello',
    'world!',
]
msg = '\r\n\r\n'.join(('\r\n'.join(headers), '\r\n'.join(body)))


def get_subject(msg, default='(no Subject line)'):
    """
    get_subject(msg) - iterate over 'msg' looking for
    Subject line; return if found otherwise 'defalut'
    """
    for line in msg:
        if line.startswith('Subject:'):
            return line.rstrip()
        if not line:
            return default


# SMTP 
print('*** Doing SMTP send via SSL...')
if SMTP_SSL:
    try:
        s = SMTP_SSL(SMTPSVR, 465)
        s.login(from_addr, passwd)
        s.sendmail(from_addr, [to_addr], msg)
        s.quit()

        print("     SSL mail sent!")
    except SMTPServerDisconnected:
        print('     error: server unexpectedly disconnected... try again')
else:
    print('     error: SMTP_SSL requires 2.6.3+')


# POP
print('*** Doing POP recv...')
try:
    s = POP3_SSL(POP3SVR, 995)
    s.user(from_addr)
    s.pass_(passwd)
    rv, msg, sz = s.retr(s.stat()[0])
    s.quit()

    line = get_subject(msg)
    print('     error: Received msg via POP: {}'.format(line))
except error_proto:
    print('     error: POP for QQ!Mail Plus subscribers only')


# IMAP
print('*** Doing IMAP recv...')
try:
    s = IMAP4_SSL(IMAP4SVR, 993)
    s.login(from_addr, passwd)
    rsp, msgs = s.select('INBOX', True)
    rsp, data = s.fetch(msgs[0], '(RFC822)')
    line = get_subject(StringIO(data[0][1]))
    s.close()
    s.logout()
    print('     Received msg via IMAP: {}'.format(line))
except error:
    print('     error: IMAP for QQ!Mail Plus subscribers only')