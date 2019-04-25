#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date:   2019-04-03 15:23:07


# jsondata=  {
#      "YII_CSRF_TOKEN":"7999a8cceacef9b8a08206ae1a1a1d5e3e5ff8e1","taskId":"61","templateId":"5","zhijianTag":"0","formData":{"content":{"suifangxinxi|ECOGpingfen|fenzhi":{"0|0|0":""},"suifangxinxi|tijianfucha|yingxiangxuefucha|empty":{"0|0|0|0":"empty"},"suifangxinxi|jubufufa|empty":{"0|0|0":"empty"},"suifangxinxi|yuanchuzhuanyi|empty":{"0|0|0":"empty"},"suifangxinxi|hualiao|empty":{"0|0|0":"empty"},"suifangxinxi|fangliao|empty":{"0|0|0":"empty"},"suifangxinxi|jibenqingkuang|tizhongzhi":{"0|0|0":""},"suifangxinxi|huanzheshentizhuangkuang":{"0|0":""}},"result":{"suifangjieguo":"成功","shengcunzhuangtai":"生存","shujulaiyuanid":{"0":"1"}}},
#      "taskStatus":"107","timeStamp":"1554270074.1762","blockType":"0","remark":"","commentType":"0","informType":"1","oldInformType":"0","informTypeTel":"651","zhaomuyuxuanType":"1","oldZhaomuyuxuanType":"0","zhaomuyuxuanTypeTel":"651","oldIsRisk":"0","isRisk":"0","turnStatus":"0","0":0.19780015945435}
# for key in jsondata:
#     print(key+":"+str(jsondata[key]))
#     
#     

#     

import time
import requests
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

url = 'http://test2.linkdoc.com:8322/task/index/submit'
# print time.time()


playload={
    "Hm_lvt_7d158d1c2764fe0e1631d71fdbc97022":"1548394011",
    "user_ticket":"ticket_1_5cad57f979803",
    "YII_CSRF_TOKEN":"7999a8cceacef9b8a08206ae1a1a1d5e3e5ff8e1", 
    "taskId": "396",
    "templateId": "1",
    "formData[content][suifangxinxi|ECOGpingfen|fenzhi][0|0|0]": "0",
    "formData[content][suifangxinxi|tijianfucha|yingxiangxuefucha|empty][0|0|0|0]": "empty",
    "formData[content][suifangxinxi|hualiao|empty][0|0|0]": "empty",
    "formData[content][suifangxinxi|fangliao|empty][0|0|0]": "empty",
    "formData[content][suifangxinxi|baxiang|empty][0|0|0]": "empty",
    "formData[content][suifangxinxi|jibenqingkuang|tizhongzhi][0|0|0]": "",
    "formData[content][suifangxinxi|bushi|empty][0|0|0]": "empty",
    "formData[content][suifangxinxi|huanzheshentizhuangkuang][0|0]": "",
    "formData[result][suifangjieguo]": "成功",
    "formData[result][shengcunzhuangtai]": "生存",
    "formData[result][shujulaiyuanid][]": "1",
    "blockType": "0"



}


r = requests.post(url, data=playload)

print r.status_code
print r.text
# print time.time()
# 
# 
# 
# 
# 
# 
# 
