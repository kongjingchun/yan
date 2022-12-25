# coding:utf-8
# @Create time: 2022/12/1 7:57 下午
# @Author: KongJingchun
# @remark:
import chardet as chardet
from lxml import etree
from bs4 import BeautifulSoup

from BaseRequest.base_request import request
from Util.send_dingding import send_dingding

if __name__ == '__main__':
    url = "https://www.smokingpipes.com/pipe-tobacco/ashton/"
    html = request.run_main(method='get', url=url).text
    soup = BeautifulSoup(html, 'lxml')
    res = str(soup.select('div[data-productID="16412"]'))
    # res = str(soup.select('div[data-productID="16409"]'))
    res1 = BeautifulSoup(res, 'lxml').select('span[class="base-price"]')
    if len(res1):
        send_dingding("烟草：有货")
    else:
        send_dingding("烟草：无货")
