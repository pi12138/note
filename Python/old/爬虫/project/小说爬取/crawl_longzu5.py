"""
从 longzu5.co 爬取龙族5txt

Author: zyp
Time: 2019-11-04 
"""

from lxml import etree
import requests
import os
import re


URL = "http://longzu5.co"
DOWNLOAD_PATH = 'longzu5/'

def load_page(url):
    """
    获取首页内容
    """
    res = requests.get(url)
    
    return res.content.decode()


def generate_urls(data, start_num):
    """
    生成内容所在的url的列表
    """
    pattern = r'longzu5.co/post/(\w+).html'
    pat = re.compile(pattern)
    result = pat.findall(data)
    result = [int(i) for i in result]
    end_num = 0
    
    if result:
        end_num = int(max(result))
    else:
        raise Exception("查找url失败，没有匹配内容！")
    
    if end_num < start_num:
        raise Exception("开始页面大于结束页面")
    
    url_list = list()
    for number in range(start_num, end_num+1):  
        url = '{}/post/{}.html'.format(URL, number)
        url_list.append(url)

    return url_list


def last_download_file(path):
    """
    判断最后下载的文件,获取最新下载文件的序号
    """
    max_num = 3

    if not os.path.exists(path):
        os.mkdir(path)

        return max_num
    else:
        file_list = os.listdir(path)
        number_list = list()
        try:
            for i in file_list:
               number =  int(i.split('-')[0])
               number_list.append(number)
        except Exception as e:
            print(e)
        
        if number_list:
            max_num = max(number_list)
        
        return max_num


def download_html(urls):
    pat = re.compile(r'<p style="text-indent: 2em;">(.*?)</p>')
    
    for u in urls:
        content = requests.get(u).content.decode()
        if is_error_url(content):
            continue

        num = u.split('/')[-1].split('.')[0]
        try:
            title = re.search(r'<h2 class="post-title">(.*?)</h2>', content).group(1)
        except AttributeError:
            title = get_title(content)

        filename = '{}-{}.txt'.format(num, title)
        filepath = '{}{}'.format(DOWNLOAD_PATH, filename)
        
        text = get_txt_content(content)	
        if not text:
            raise Exception("文章内容为空! {}".format(filename))

        with open(filepath, 'w') as f:
            f.write(text)
            print("{}下载完成".format(filepath))
            
    print("全部文章下载完成")
    return True


def get_txt_content(html):
    html = etree.HTML(html)
    text_list = html.xpath('//p[@style="text-indent: 2em;"]/text()')
    text_list2 = html.xpath('//span[@style]/text()')
    text_list3 = html.xpath('//div[@class="post-body"][1]/p/text()')

    if text_list:
        text = '\n'.join(text_list)
    if text_list2:
        text = '\n'.join(text_list2)
    if text_list3:
        text = '\n'.join(text_list3)

    return text


def get_title(html):
    ele = etree.HTML(html)
    title = ele.xpath('//h2[@class="post-title"]/text()')
    
    if not title:
        with open("longzu5/error.html", "w") as f:
            f.write(html)
        raise Exception("标题为空")
    
    return title[0]


def is_error_url(html):
    """
    某些url页面上不存在
    """
    title = etree.HTML(html).xpath('//title/text()')
    if not title:
        with open("longzu5/error2.html", "w") as f:
            f.write(html)
        raise Exception("出现异常, 已写入到error2.html文件")
    if title[0] == "对不起，页面未找到":
        return True
    return False


if __name__ == "__main__":

    content = load_page(URL)
    num = last_download_file(DOWNLOAD_PATH)
    urls = generate_urls(content, num)
    download_html(urls)

