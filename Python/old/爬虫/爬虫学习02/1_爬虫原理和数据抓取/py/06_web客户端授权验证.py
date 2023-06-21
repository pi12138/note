from urllib import request

user_name = "root"
user_password = "Zhou19981118"
webserver = "http://203.195.129.175/"

pwd_mgr = request.HTTPPasswordMgrWithDefaultRealm()
pwd_mgr.add_password(None, webserver, user_name, user_password)
httpauth_handler = request.HTTPBasicAuthHandler(pwd_mgr)

opener = request.build_opener(httpauth_handler)

req = request.Request(webserver)

response = opener.open(req)

print(response.read().decode())