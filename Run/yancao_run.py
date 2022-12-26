# coding:utf-8
# @Create time: 2022/12/1 7:57 下午
# @Author: KongJingchun
# @remark:
import time

import chardet as chardet
from lxml import etree
from bs4 import BeautifulSoup

from BaseRequest.base_request import request
from Util.send_dingding import send_dingding

yan_list = {
    "https://www.smokingpipes.com/pipe-tobacco/esoterica/": ["1994", "2018", "2015", "2014", "2198", "2194", "2024",
                                                             "2193", "2019", "2199", "2201", "1996", "2017", "2021",
                                                             "1995", "2026", "2195", "2197", "2016", "2023", "2022",
                                                             "215752", "2196", "1997", "2025", "2200"],
    "https://www.smokingpipes.com/pipe-tobacco/fribourg-treyer/": ["284"],
    "https://www.smokingpipes.com/pipe-tobacco/gawith-hoggarth/": ["6044"],
    "https://www.smokingpipes.com/pipe-tobacco/germain/": ["215753", "215757", "2417", "215754", "215755", "2007",
                                                           "2012", "2418", "2416", "2011", "2010", "2419", "2013",
                                                           "2009"],
    "https://www.smokingpipes.com/pipe-tobacco/gawith-hoggarth/bulk/": ["8579", "4011", "8578"],
    # "https://www.smokingpipes.com/pipe-tobacco/ashton/":["16413"]
}

if __name__ == '__main__':
    yans = []
    for key, values in yan_list.items():
        html = request.run_main(method='get', url=key).text
        for value in values:
            soup = BeautifulSoup(html, 'lxml')
            res = str(soup.select('div[data-productID="' + value + '"]'))
            res1 = BeautifulSoup(res, ''
                                      'lxml').select('span[class="base-price"]')
            if len(res1):
                yans.append(key)
            else:
                print(key + "无货")
    if len(yans):
        msg = "烟草：有货"
        for i in yans:
            msg = msg + "    地址:" + i
        send_dingding(msg, isall=True)
    else:
        c_time = time.strftime("%H:%M:%S", time.localtime())  # 将本地时间转换为字符串，并格式化为 时：分：秒
        if c_time[3:5] == '00':
            send_dingding("烟草：无货")
