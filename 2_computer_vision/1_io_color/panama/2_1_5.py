#coding:utf-8
import cv2
import random
import numpy as np

#####画像読み込み#####
img = cv2.imread('sample.tif', 1)

#####変換先配列#####
img_hsv = np.zeros(img.shape, dtype=np.uint8)
img_hue = np.zeros(img.shape, dtype=np.uint8)
img_satu = np.zeros(img.shape, dtype=np.uint8)
img_value = np.zeros(img.shape, dtype=np.uint8)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imwrite('hsv_sample.tif', img_hsv)

#print img_hsv

for i in range(5):
    for j in range(8):
        for k in range(3):
            if(k == 0):
                #if((img_hsv[i][j][k] % 120) ==0):
                img_hue[i][j][k] = (img_hsv[i][j][k] + 60) % 180
                img_satu[i][j][k] = img_hsv[i][j][k]
                img_value[i][j][k] = img_hsv[i][j][k]
            
            elif(k == 1):
                img_hue[i][j][k] = img_hsv[i][j][k]
                img_satu[i][j][k] = img_hsv[i][j][k] * random.random()
                img_value[i][j][k] = img_hsv[i][j][k]

            else:
                img_hue[i][j][k] = img_hsv[i][j][k]
                img_satu[i][j][k] = img_hsv[i][j][k]
                img_value[i][j][k] = img_hsv[i][j][k] if (img_hsv[i][j][k] + (255 * random.uniform(0.5, 0.8))) > 255 else img_hsv[i][j][k] + (255 * random.uniform(0.5, 0.8))

#print img_hsv
#print img_hue
#print img_value

#####画像書き出し#####
img_hue = cv2.cvtColor(img_hue, cv2.COLOR_HSV2BGR)
img_satu = cv2.cvtColor(img_satu, cv2.COLOR_HSV2BGR)
img_value = cv2.cvtColor(img_value, cv2.COLOR_HSV2BGR)
cv2.imwrite('hue_sample.tif', img_hue)
cv2.imwrite('satu_sample.tif', img_satu)
cv2.imwrite('value_sample.tif', img_value)
