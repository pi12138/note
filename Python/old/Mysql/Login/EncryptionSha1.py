# coding:utf-8

"""对输入的密码进行sha1加密"""

# from hashlib import sha1
import hashlib

password = input('input password:')

s1 = hashlib.sha1()

s1.update(password.encode())
print(s1.hexdigest())


