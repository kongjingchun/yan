# coding:utf-8
# @Create time: 2021/8/9 7:34 下午
# @Author: KongJingchun
# @remark:发送请求基类
import requests
import json
# 以下两行去掉Https的警告信息输出
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class BaseRequest:
    def _send_get(self, url, data, cookie, header, verify):
        """
        发送get请求
        :return: Response数据或者cookie
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header, verify=verify)
        return response

    def _send_post(self, url, data, cookie, header, verify):
        """
        发送post请求
        :return: Response数据或者cookie
        """
        response = requests.post(url=url, json=data, cookies=cookie, headers=header, verify=verify)
        return response

    def run_main(self, method, url, date=None, cookie=None,  header=None, verify=False, host="雨"):
        """
        判断请求方式，并发送对应的请求
        :param method: 请求方式：get、post
        :param url: 请求地址
        :param date: 请求数据
        :param cookie: cookie
        :param get_cookie: cookie_key
        :param verify: 跳过https校验
        :return: Response
        """
        if method == "get" or method == "GET":
            response = self._send_get(url, date, cookie,  header, verify)
        else:
            response = self._send_post(url, date, cookie,  header, verify)
        # 如果Response是json格式转换成json格式
        # try:
        #     res = json.loads(res)
        # except:
        #     print("Response 不是json格式")
        return response


request = BaseRequest()
if __name__ == '__main__':
    url = "https://www.smokingpipes.com/pipe-tobacco/ashton/"
    res = request.run_main(method='get', url=url)
    print(res.text)
