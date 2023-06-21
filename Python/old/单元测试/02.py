# 编写服务器的测试文件，检验服务器是否正常工作

import unittest
import requests


class ServerTest(unittest.TestCase):
	def setUp(self):
		self.url = "http://127.0.0.1:9999"

	def test_server(self):
		res = requests.get(self.url)

		self.assertTrue(hasattr(res, "text"))
		self.assertEqual(res.text, "GET success")
		

if __name__ == "__main__":
	unittest.main()