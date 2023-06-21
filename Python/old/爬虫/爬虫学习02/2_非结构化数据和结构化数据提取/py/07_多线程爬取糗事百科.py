from urllib import request
from queue import Queue
from lxml import etree
import threading
import json
import time


class ThreadSpide(threading.Thread):
    """
    多线程爬虫类
    """
    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadSpide, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue

        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }

    
    def run(self):
        print("{}启动".format(self.thread_name))
        while not SPIDER_EXIT:
            try:
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/text/page/"+ str(page) + "/"
                req = request.Request(url, headers=self.headers)
                response = request.urlopen(req)
                html = response.read().decode()

                time.sleep(1)

                self.data_queue.put(html)

            except Exception as e:
                print("ThreadSpide run error: {}".format(e))

        print("{}结束".format(self.thread_name))


class ThreadParse(threading.Thread):
    """
    多线程解析类
    """
    def __init__(self, thread_name, data_queue, filename, lock):
        super(ThreadParse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.filename = filename
        self.lock = lock
    

    def run(self):
        print("{}启动".format(self.thread_name))
        while not PARSE_EXIT:
            try:
                html = self.data_queue.get(block=False)
                self.parse(html)

            except Exception as e:
                print("ThreadParse run error:{}".format(e))

        print("{}结束".format(self.thread_name))


    def parse(self, html):
        """
        解析html页面提取数据
        """
        html = etree.HTML(html)

        node_list = html.xpath("//div[contains(@id, 'qiushi_tag_')]")
        for node in node_list:
            # xpath返回的查询结果是一个列表
            author = node.xpath('.//h2')[0].text
            content = node.xpath(".//div[@class='content']/span")[0].text
            vote = node.xpath('.//div[@class="stats"]/span[1]/i')[0].text
            comments = node.xpath('.//div[@class="stats"]/span[2]/a/i')[0].text

            qiushi = {
                "作者": author,
                "内容": content,
                "好笑": vote,
                "评论": comments,
            }

            with self.lock:
                self.filename.write(json.dumps(qiushi, ensure_ascii=False) + "\n")


SPIDER_EXIT = False
PARSE_EXIT = False


def main():
    page_queue = Queue(maxsize=3)

    for i in range(1, 3+1):
        page_queue.put(i)
    
    data_queue = Queue()

    spider_list = ["采集线程1号", "采集线程2号", "采集线程3号"]
    thread_spider = []
    for thread_name in spider_list:
        thread = ThreadSpide(thread_name, page_queue, data_queue)
        thread.start()
        thread_spider.append(thread)

    filename = open("../text/糗事百科文本/qiushi.json", 'a', encoding="utf-8")
    lock = threading.Lock()

    parse_list = ["解析线程1号", "解析线程2号", "解析线程3号"]
    thread_parse = []
    for thread_name in parse_list:
        thread = ThreadParse(thread_name, data_queue, filename, lock)
        thread.start()
        thread_parse.append(thread)

    while not page_queue.empty():
        pass
    
    global SPIDER_EXIT
    SPIDER_EXIT = True

    for thread in thread_spider:
        thread.join()
    
    while not data_queue.empty():
        pass
    
    global PARSE_EXIT
    PARSE_EXIT = True

    for thread in thread_parse:
        thread.join()
    
    with lock:
        filename.close()


if __name__ == "__main__":
    main()