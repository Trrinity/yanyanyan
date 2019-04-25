#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
from xpinyin import Pinyin
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

# pin = Pinyin()
# test1 = pin.get_pinyin('大河向东流)   #默认分割符为-
# print(test1)

# test2 = pin.get_pinyin("大河向东流", "")
# print(test2)









# import re

# def versionCompare(v1, v2):
#     v1_check = re.match("\d+(\. \d+){0,2}", v1)
#     v2_check = re.match("\d+(\.\d+){0,2}", v2)
#     if v1_check is None or v2_check is None or v1_check.group() != v1 or v2_check.group() != v2:
#         return "版本号格式不对，正确的应该是x.x.x,只能有3段"
#     v1_list = v1.split(".")
#     v2_list = v2.split(".")
#     v1_len = len(v1_list)
#     v2_len = len(v2_list)
#     if v1_len > v2_len:
#         for i in range(v1_len - v2_len):
#             print(i)
#             v2_list.append("0")
#     elif v2_len > v1_len:
#         for i in range(v2_len - v1_len):
#             print(i)
#             v1_list.append("0")
#     else:
#         pass
#     for i in range(len(v1_list)):
#         if int(v1_list[i]) > int(v2_list[i]):
#             return "v1大"
#         if int(v1_list[i]) < int(v2_list[i]):
#             return "v2大"
#     return "相等"
 
# # 测试用例
# if __name__ == '__main__':
        
#     print(versionCompare("", ""))
#     print(versionCompare("1.0.a", "d.0.1"))
#     print(versionCompare("1.0.1", "1.0.1"))
#     print(versionCompare("1.0.2", "1.0.1"))
#     print(versionCompare("1.0.1", "1.0.2"))
#     print(versionCompare("1.0.11","1.0.2"))
#     




def versionCompare(v1,v2):
    l_1 =v1.split('.')
    l_2 = v2.split('.')
    c =0
    while True:
        if c == len(l_1) and c==len(l_2):
            return 0
        if len(l_1)==c:
            l_1.append(0)
        if len(l_2)==c:
            l_2.append(0)
        if int(l_1[c])>int(l_2[c]):
            return 1
        elif int(l_1[c])<int(l_2[c]):
            return -1
        c+=1
if __name__ == '__main__':
    print(versionCompare("", ""))
    print(versionCompare("1.0.a", "d.0.1"))
    print(versionCompare("1.0.1", "1.0.1"))
    print(versionCompare("1.0.2", "1.0.1"))
    print(versionCompare("1.0.1", "1.0.2"))
    print(versionCompare("1.0.11","1.0.2"))
    
