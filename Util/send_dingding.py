# coding:utf-8
# @Create time: 2021/9/15 5:14 下午
# @Author: KongJingchun
# @remark:发送钉钉报警消息
import datetime
import json
import os
import time

import requests


def send_dingding(message, isall=False):
    """
    发送钉钉消息
    :param isall: 是否@所有人
    :param message: 消息内容
    :return: 无
    """
    # 根据路径判断报警钉钉群
    url = 'https://oapi.dingtalk.com/robot/send?access_token=e2039a48f2e846028878df208d8423277269c29dde97d6e38a84c8e822535496'
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }

    data = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "atMobiles": [
                "wh949wl",  # 机器人发送信息@的用户
            ],
            "isAtAll": isall  # 是否@所有人
        }
    }

    # 发送请求
    resp = requests.post(url,
                         data=json.dumps(data).encode('utf8'),
                         headers=headers,
                         verify=False
                         )
    print(resp.json())


if __name__ == '__main__':
    send_dingding("烟草：测试")
