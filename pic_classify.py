# -*- coding: utf-8 -*-

"""
Created on 18-12-6

@author: 260240

@requirements: PyCharm 2018.2.4; Python 3.6.0 |Anaconda 4.3.1 (64-bit)

@decription:根据处理后的txt文件将图片分类
"""


import os
import shutil

nof = open("noGlass.txt")
hasf = open("glass.txt")

noLine = nof.readline()
hasLine = hasf.readline()

list = os.listdir("/home/260240/PycharmProjects/glasses_detection/img_align_celeba")
hasGo = True
noGo = True
for i in range(0, len(list)):
    imgName = os.path.basename(list[i])
    if os.path.splitext(imgName)[1] != ".jpg":
        continue
    noArray = noLine.split()
    if len(noArray) < 1:
        noGo = False
    hasArray = hasLine.split()
    if len(hasArray) < 1:
        hasGo = False
    if noGo and (imgName == noArray[0]):
        oldname = "/home/260240/PycharmProjects/glasses_detection/img_align_celeba/"+imgName
        newname = "/home/260240/PycharmProjects/glasses_detection/noGlass/"+imgName
        shutil.move(oldname, newname)
        noLine = nof.readline()
    elif hasGo and (imgName == hasArray[0]):
        oldname = "/home/260240/PycharmProjects/glasses_detection/img_align_celeba/"+imgName
        newname = "/home/260240/PycharmProjects/glasses_detection/hasGlass/"+imgName
        shutil.move(oldname, newname)
        hasLine = hasf.readline()
    if i % 100 == 0:
        print(imgName)

nof.close()
hasf.close()
