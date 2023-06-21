from urllib import request
import json
import jsonpath


def download_file():
    """
    下载文件
    """
    url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }

    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    with open("../text/city.txt", 'w', encoding="utf-8") as f:
        f.write(html)
        print("{}下载完成！".format(f.name))

    analysis_file(html)


def analysis_file(html):
    """
    对获取到的json文件进行解析
    """
    json_file = json.loads(html)
    city_list = jsonpath.jsonpath(json_file, "$..name")

    print(len(city_list))

    content = json.dumps(city_list, ensure_ascii=False)

    with open("../text/city.json", 'w', encoding="utf-8") as f:
        f.write(content)
        print("{}下载完成！".format(f.name))


if __name__ == "__main__":
    download_file()
