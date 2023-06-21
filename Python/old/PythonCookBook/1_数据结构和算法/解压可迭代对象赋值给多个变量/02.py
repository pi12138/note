'''
另外一种情况，假设你现在有一些用户的记录列表，每条记录包含一个名字、邮
件，接着就是不确定数量的电话号码。你可以像下面这样分解这些记录：

'''

def test(info):
    name,email,*phone = info
    print('name:',name)
    print("email:",email)
    print('phone:',phone)



info = ['zyp','1558255789@qq.com','13193820382','18790065681','15938278008']

test(info)