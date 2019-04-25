#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date:   2019-04-04 13:23:07
# 
import os
import time

screen_cap = "adb shell screencap -p /sdcard/1.png"
pic_name = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))


pull = "adb pull /sdcard/1.png ./%s.png" % pic_name
check_device = "adb devices"


if len(os.popen(check_device).read()) > 26:
    try:
        os.system(screen_cap)
        os.system(pull)
# 　　　　adb exec-out screencap -p > {pic_name}.png
        print("success!")
    except:
        print("---------------------------sorry! cant screencap ~---------------------")
else:
    print("-------------------sorry! device was not found!-----------------------")