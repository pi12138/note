"""
问题
	一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些字符清理掉。
解决方案
	文本清理问题会涉及到包括文本解析与数据处理等一系列问题。
在非常简单的情形下，你可能会选择使用字符串函数 (比如 str.upper() 和 str.lower() ) 将文本转为标准格式。
使用 str.replace() 或者 re.sub() 的简单替换操作能删除或者改变指定的字符序列。
你同样还可以使用 2.9 小节的 unicodedata.normalize() 函数将 unicode文本标准化。
然后，有时候你可能还想在清理操作上更进一步。比如，你可能想消除整个区间上的字符或者去除变音符。
为了这样做，你可以使用经常会被忽视的 str.translate()方法。为了演示，假设你现在有下面这个凌乱的字符
"""

text1 = "pýtĥöñ\fis\tawesome\r\n"

print(text1)			# > "pýtĥöñis      awesome\r\n"

remap = {
	ord('\f') : ' ',
	ord('\t') : ' ',
	ord('\r') : None,
	ord('\n') : None,
}

# 另一种写法
# inputTab = "\f\t\r"
# outputTab = "   " 
# tranTab = text1.maketrans(inputTab, outputTab)
# text2 = text1.translate(tranTab)

text2 = text1.translate(remap)

print(text2)			# > pýtĥöñ is awesome
print(remap)			# > {12: ' ', 9: ' ', 13: None, 10: None}


"""
正如你看的那样，空白字符 \t 和 \f 已经被重新映射到一个空格。回车字符 r 直
接被删除。
你可以以这个表格为基础进一步构建更大的表格。比如，让我们删除所有的和音
符：
"""


import unicodedata
import sys

trans_map = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))


text3 = unicodedata.normalize('NFD', text2)		# > pýtĥöñ is awesome
text4 = text3.translate(trans_map)				# > python is awesome

print(text3)
print(text4)
# print(trans_map)				# 返回会一个 Unicode 和音符作为键，对应的值全部为None 的字典 。

"""
	上面例子中，通过使用 dict.fromkeys() 方法构造一个字典，每个 Unicode 和音
符作为键，对应的值全部为 None 。
	然后使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。然后再
调用 translate 函数删除所有重音符。同样的技术也可以被用来删除其他类型的字符
(比如控制字符等)。
	作为另一个例子，这里构造一个将所有 Unicode 数字字符映射到对应的 ASCII 字
符上的表格：
"""


digitmap = {c:ord('0')+unicodedata.digit(chr(c)) for c in range(sys.maxunicode) if unicodedata.category(chr(c)) == "Nd"}

print(len(digitmap))	# > 580

content1 = "\u0661\u0662\u0663"
content2 = content1.translate(digitmap)

print(content1)			# > "١٢٣"
print(content2)			# > "123"



"""
	另一种清理文本的技术涉及到 I/O 解码与编码函数。这里的思路是先对文本做一
些初步的清理，然后再结合 encode() 或者 decode() 操作来清除或修改它。比如：
"""

str1 = "pýtĥöñ is awesome\n"
str2 = unicodedata.normalize('NFD', str1)
str3 = str2.encode('ascii', 'ignore').decode('ascii')

print(str1)			# > "pýtĥöñ is awesome\n"
print(str2)			# > "pýtĥöñ is awesome\n"
print(str3)			# > "python is awesome\n"


"""
	这里的标准化操作将原来的文本分解为单独的和音符。接下来的 ASCII 编码/解码
只是简单的一下子丢弃掉那些字符。当然，这种方法仅仅只在最后的目标就是获取到文
本对应 ACSII 表示的时候生效。
"""

"""
讨论
	文本字符清理一个最主要的问题应该是运行的性能。一般来讲，代码越简单运行越
快。对于简单的替换操作，str.replace() 方法通常是最快的，甚至在你需要多次调用
的时候。比如，为了清理空白字符，你可以这样做：
"""

s = "pýtĥöñ\fis\tawesome\r\n"

def clean_spaces(s):
	s = s.replace('\r', ' ')
	s = s.replace('\t', ' ')
	s = s.replace('\f', ' ')
	s = s.replace('\n', '')

	return s 

print(clean_spaces(s))		# > pýtĥöñ is awesome

"""
	如果你去测试的话，你就会发现这种方式会比使用 translate() 或者正则表达式
要快很多。
	另一方面，如果你需要执行任何复杂字符对字符的重新映射或者删除操作的话，
tanslate() 方法会非常的快。
	从大的方面来讲，对于你的应用程序来说性能是你不得不去自己研究的东西。不幸
的是，我们不可能给你建议一个特定的技术，使它能够适应所有的情况。因此实际情况
中需要你自己去尝试不同的方法并评估它。
	尽管这一节集中讨论的是文本，但是类似的技术也可以适用于字节，包括简单的替
换，转换和正则表达式。
"""

"""
实例
	清除文本字符与和音符
"""

def clean_characters(content):
	"""清除字符"""
	import unicodedata

	content = content.replace('\r', ' ')
	content = content.replace('\t', ' ')
	content = content.replace('\f', ' ')
	content = content.replace('\n', '')

	content = unicodedata.normalize("NFD", content)
	content = content.encode('ascii', 'ignore').decode('ascii')

	return content

text = "pýtĥöñ\fis\tawesome\r\n"

print(clean_characters(text))		# > "	python is awesome"
