#-*- coding:utf-8 -*-
import random
import string
import io,os
from faker import Factory

def genSizeFile(fileName, fileSize):
    #file path
    filePath="D:\\1002file\\"+str(fileName)+".dcm"

    # 生成固定大小的文件
    # date size
    ds=0
    with io.open(filePath, 'r+') as f:
        while ds<fileSize:
            fake = Factory().create('zh_CN')
            f.write(fake.address())
            # f.write("\n")
            ds=os.path.getsize(filePath)
    # print(os.path.getsize(filePath))

if __name__ == '__main__':
    for i in range(1):
        filename=random.randint(20, 150)
        # print type(i)
        # s = str(i)
        # print type(i)
        # g = s.zfill(5) 
        genSizeFile(i,filename*1024)
