# -*- coding: utf-8 -*-

"""
Created on 18-12-6

@author: 260240

@requirements: PyCharm 2018.2.4; Python 3.6.0 |Anaconda 4.3.1 (64-bit)

@decription:将txt标注文件分成两组，有眼镜和无眼镜
"""


newTxt = "glass.txt"
newf = open(newTxt, "a+")
newNoTxt = "noGlass.txt"
newNof = open(newNoTxt, "a+")
f = open("/home/260240/PycharmProjects/glasses_detection/list_attr_celeba.txt")
line = f.readline()

while line:
    array = line.split()
    if array[16] == "-1":
        new_context = array[0] + '\n'
        newNof.write(new_context)
    else:
        new_context = array[0] + '\n'
        newf.write(new_context)
    line = f.readline()

f.close()
newf.close()
newNof.close()
