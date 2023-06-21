# 对url进行参数编码的方法
# 使用parse模块
from urllib import request, parse

# 注意下面网址最后的's?'
# url中使用的是http，不能用https
url = 'http://www.baidu.com/s?'

word = input("Please enter the keyword you want to search:")

keyword = {
	'wd':word
}

# help(parse.urlencode)
# urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=<function quote_plus at 0x00000280BCEE2E18>)
#     Encode a dict or sequence of two-element tuples into a URL query string.

#     If any values in the query arg are sequences and doseq is true, each
#     sequence element is converted to a separate parameter.

#     If the query arg is a sequence of two-element tuples, the order of the
#     parameters in the output will match the order of parameters in the
#     input.

#     The components of a query arg may each be either a string or a bytes type.

#     The safe, encoding, and errors parameters are passed down to the function
#     specified by quote_via (encoding and errors only if a component is a str).

# 对内容进行url编码
print("keyword:", keyword)

keyword = parse.urlencode(keyword)

print("new_keyword:", keyword)

# 原url和编码后的keywo组成新的new_url
new_url = url + keyword

print("new_url:", new_url)

# with request.urlopen(new_url) as f:
# 	html = f.read()
# 	print(f.geturl())
# 	print(html.decode())
response = request.urlopen(new_url)
print("url:", response.geturl())
html = response.read()
print(html.decode())