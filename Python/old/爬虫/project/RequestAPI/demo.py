from urllib import parse
import requests


class RequestAPI:
    """
    使用requests库调用api接口
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_token(self, url):
        self.host = self.get_host(url)
        self.token = self.get_token()
        self.headers = {
            'Authorization': 'jwt {}'.format(self.token)
        }

    def get_host(self, url):
        parobj = parse.urlparse(url)
        host = '{}://{}/'.format(parobj.scheme, parobj.netloc)
        return host

    def get_token(self):
        token_url = self.host+'jwt-token-auth/'
        params = {
            'username': self.username,
            'password': self.password
        }
        res = requests.post(token_url, params)

        if res.status_code == 200:
            token = res.json().get('token', None)

            if token is None:
                raise Exception('身份认证失败')

            return token

        raise Exception("状态码为: {}".format(res.status_code))

    def test_T2_42(self, url):
        """
        测试 
        T2_42   可下载和分享成长记录册
        """
        self.set_token(url)
        res = requests.get(url, headers=self.headers)

        if res.status_code == 200:
            pdf_url = res.json().get('url', None)

            if pdf_url is None:
                raise Exception('获取pdf url失败')
            
            filename = res.json().get('filename', None)
            self.download_pdf(pdf_url, filename)

    @staticmethod
    def download_pdf(url, filename):
        res = requests.get(url)

        if res.status_code != 200:
            raise Exception("获取pdf内容失败")

        with open('./file/{}'.format(filename), 'wb') as f:
            f.write(res.content)
        
        print("下载 {} 成功".format(filename))


if __name__ == "__main__":
    cn_url = 'https://www.taidii.cn/jwt-token-auth/'
    dev_url = 'https://dev.taidii.cn/'

    # url = "https://dev.taidii.cn/api/student/62818/save_portfoliov4/?student_portfolio_id=6337"
    # username = 'ysk001'
    # password = '123456'
    params = {

    }

    # cn数据
    # 可达
    # url = "https://www.taidii.cn/api/student/75072/save_portfoliov4/?student_portfolio_id=13525"
    # username = 'kd'
    # password = '123456'

    # 张小小
    # url = "https://www.taidii.cn/api/student/80850/save_portfoliov4/?student_portfolio_id=13255"
    # username = 'zxx'
    # password = '123456'

    # 张悠悠
    url = "https://www.taidii.cn/api/student/71753/save_portfoliov4/?student_portfolio_id=13256"
    username = 'zyy'
    password = '123456'

    obj = RequestAPI(username, password)
    obj.test_T2_42(url)

