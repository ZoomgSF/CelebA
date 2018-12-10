# -*- coding: utf-8 -*-

"""
Created on 18-12-6

@author: 260240

@requirements: PyCharm 2018.2.4; Python 3.6.0 |Anaconda 4.3.1 (64-bit)

@decription:将图片人脸框出并保存
"""

from PIL import Image
import face_recognition
import os

# for (int i = 1; i <= 10; i++)
list = os.listdir("/home/260240/PycharmProjects/glasses_detection/noGlass")
for i in range(0, 10001):
    imgName = os.path.basename(list[i])
    if os.path.splitext(imgName)[1] != ".jpg":
        continue

    image = face_recognition.load_image_file(imgName)

    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        # print("A face is located at pixel location Top: {},
        #  Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        width = right - left
        height = bottom - top
        if width > height:
            right -= (width - height)
        elif height > width:
            bottom -= (height - width)
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save('face%s' % imgName)
