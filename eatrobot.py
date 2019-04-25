#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def alert(con):
    url = "https://oapi.dingtalk.com/robot/send"
    querystring = {"access_token":"c518ef92b11445ef993c6d9c8408987483e5492b1705326fcff4ba0f524a0054"}

    data = {
        "msgtype" : "text",
        "text" : {
            "content" : con,
            "at" : {
                'isAtAll' : True
            }
        }
    }
    json_str = json.dumps(data)
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=json_str, headers=headers, params=querystring)

    print(response)
    print(response.text)

if __name__ == "__main__":
    alert("吃饭啦！！")