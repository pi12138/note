# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
import asyncio

@asyncio.coroutine
def wget(host):
	print('wget {}'.format(host))
	# 异步请求网络地址
	connect = asyncio.open_connection(host, 80)
	# 注意yield 用法
	reader, writer = yield from connect
	header = "GET / HTTP / 1.0\r\nHost: {}\r\n\r\n".format(host)
	writer.write(header.encode('utf-8'))
	yield from writer.drain()
	while True:
		liner = yield from reader.readline()
		# http协议换行使用\r\n
		if liner == b'\r\n':
			break
		print("{0} header > {1}".format(host, liner.decode('utf-8').rstrip()))
	writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com', 'www.sohu.com', 'www.baidu.com']]
# 'www.163.com' 找不到header？？？
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

