# -*- coding: utf-8 -*-

"""
Created on 18-12-6

@author: 260240

@requirements: PyCharm 2018.2.4; Python 3.6.0 |Anaconda 4.3.1 (64-bit)

@decription:
"""
import face_recognition
import tensorflow as tf
import cv2
import time
a = time.time()
img = []
img = face_recognition.load_image_file("/home/260240/PycharmProjects/img_auto_cut/2/2.jpg")
face_locations = face_recognition.face_locations(img)
for face_location in face_locations:
    top, right, bottom, left = face_location
    width = right - left
    height = bottom - top
    # 方形人脸
    if (width > height):
        right -= (width - height)
    elif (height > width):
        bottom -= (height - width)
    face_image = img[top:bottom, left:right]
    reshaped_img = cv2.resize(face_image, (100, 100))
b = time.time()
print(b - a)

face_dict = {0: 'Has Glass', 1: 'No Glass'}
with tf.Session() as sess:
    data = []
    data = [reshaped_img]
    saver = tf.train.import_meta_graph('./model/model.ckpt.meta')
    saver.restore(sess, tf.train.latest_checkpoint('./model/'))
    graph = tf.get_default_graph()
    x = graph.get_tensor_by_name("x:0")
    feed_dict = {x: data}

    logits = graph.get_tensor_by_name("logits_eval:0")

    classification_result = sess.run(logits, feed_dict)

    # 打印出预测矩阵
    print(classification_result)
    # 打印出预测矩阵每一行最大值的索引
    print(tf.argmax(classification_result, 1).eval())
    # 根据索引通过字典对应人脸的分类
    output = []
    output = tf.argmax(classification_result, 1).eval()
    print("face is belong to:"+face_dict[output[0]])
cv2.namedWindow('', 2)
cv2.imshow('', img)
cv2.waitKey()
