from lxml import etree
import requests
import re
import csv


class RankSpider():
    def __init__(self, url):
        self.url = url
    
    def load_page(self):
        """
        加载页面内容
        """
        res = requests.get(self.url)
        return res.content.decode()

    def get_content(self, res):
        """
        获取需要的排名内容
        """
        title = re.search(r'<h3 class="post-title">(.*)</h3>', res)
        html = etree.HTML(res)
        head = html.xpath('//thead/tr/th/text()')[:4]
        select_head = html.xpath('//thead/tr/th[5]/select/option/text()')
        body = html.xpath('//tbody/tr')
        body = self.get_body(body)

        rank_info = dict()
        rank_info['title'] = title.group(1)
        rank_info['head'] = head + select_head
        rank_info['body'] = body

        return rank_info
        
    def get_body(self, body):
        """
        获取tbody中主要的排名数据
        """
        data_list = list()
        for tr in body:
            data = tr.xpath('./td/text()')  
            school = tr.xpath('./td/div/text()')
            data.insert(1, school[0])
            data_list.append(data)
        
        return data_list

    def save(self, data, format_="txt"):
        """
        保存数据
        """
        title = data.get('title', 'file')
        head = data.get('head')
        body = data.get('body')

        if format_ == "txt":
            with open('{}.txt'.format(title), 'w') as f:
                head = ",".join(head)
                f.write(head+'\n')
                for b in body:
                    body = ','.join(b)
                    f.write(body+'\n')
        elif format_ == "csv":
            with open('{}.csv'.format(title), 'w') as f:
                csv_write = csv.writer(f)
                csv_head = head
                csv_write.writerow(csv_head)
                for b in body:
                    csv_b = b
                    csv_write.writerow(csv_b)

        return "success"


if __name__ == "__main__":
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    rs = RankSpider(url)
    res = rs.load_page()
    content = rs.get_content(res)
    rs.save(content, "csv")