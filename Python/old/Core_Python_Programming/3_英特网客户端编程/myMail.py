from smtplib import SMTP
from poplib import POP3
from time import sleep


SMTPSVR = 'smtp.qq.com'
POP3SVR = 'pop.qq.com'

from_addr = '1558255789@qq.com'
# to_addr = '2059233910@qq.com'
passwd = 'ngqedkkpiesqjeie'
body = """\
    From: {}
    To: {}
    Subject: test msg
    Hello World!
    """.format(from_addr, from_addr)


smtp_obj = SMTP(SMTPSVR)
smtp_obj.login(from_addr, passwd)
errs = smtp_obj.sendmail(from_addr, [from_addr], body)
smtp_obj.quit()

assert len(errs) == 0, errs

sleep(10)

pop_obj = POP3(POP3SVR)
pop_obj.user(from_addr)
pop_obj.pass_(passwd)
rsp, msg, siz = pop_obj.retr(pop_obj.stat()[0])
print(msg)
sep = msg.index('')
recvBody = msg[seq+1:]

assert body == recvBody

