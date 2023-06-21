"""

"""

import requests

url = "http://www.baidu.com"

response = requests.get(url)

print(response.text)
print(type(response))
print(response.url)
print(response.content)
print(response.content.decode())
