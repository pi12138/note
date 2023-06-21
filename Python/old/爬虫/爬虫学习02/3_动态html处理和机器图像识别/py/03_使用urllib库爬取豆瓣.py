"""
因为豆瓣电影排行榜内容使用ajax加载的，如果只是简单访问 url "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=" 得到的只是这个页面的一个框架html，并没有需要的实质性的内容
经过抓包分析，发现内容数据在 url "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20" 中, 返回的是json格式数据
其实获取电影排行榜内容就是获取其中的json数据，通过改变url里的 interval_id、start、limit几个参数便可以获取到json数据
"""

from urllib import request
import json


class DouBanMovieSpide:
    """
    豆瓣电影剧情片排行榜
    """
    def __init__(self):
        self.url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
    

    def load_page(self):
        """
        加载页面，获取json数据
        """
        try:
            req = request.Request(self.url, headers=self.headers)
            response = request.urlopen(req)
            html = response.read().decode()

            # print(type(html))     # > <class 'str'>

            self.parse_page(html)
        except Exception as e:
            print("load_page error:{}".format(e))


    def parse_page(self, html):
        """
        解析html页面，实际上就是提取json数据
        """
        try:
            text = json.loads(html)

            movie_list = []

            for t in text:
                rating = t['rating'][0]
                rank = t['rank']
                title = t['title']

                movie_info = {
                    "rating": rating,
                    "rank": rank,
                    "title": title,
                }

                movie_list.append(movie_info)

            self.write_info(movie_list)
        except Exception as e:
            print("parse_page error:{}".format(e))


    def write_info(self, movie):
        """
        将提取出来的json数据存储到json文件中
        """
        with open("../text/doubanmovie.json", 'w', encoding="utf-8") as f:
            f.write(json.dumps(movie, ensure_ascii=False))
        print("write success")


if __name__ == "__main__":
    dbm = DouBanMovieSpide()
    dbm.load_page()
