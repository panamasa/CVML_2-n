#coding:utf-8:wq
import cv2
from PIL import Image
import matplotlib.pyplot as plt

#####画像読み込み,1はRGB読み込み#####
img = cv2.imread('sample.tif', 1)

#####画像のサイズ,チャネル数表示#####
print "(縦サイズ, 横サイズ, チャネル数) = ",
print img.shape


#####拡張子を指定して画像保存#####
cv2.imwrite('sample.jpg', img)
cv2.imwrite('sample.png', img)
cv2.imwrite('sample.bmp', img)

#####グレースケールで画像を保存#####
gray_img = cv2.imread('lena.tif', 0)
#gray_lena = cv2.cvtColor(gray_img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('gray_scale_lena.png', gray_img)

#####ヒストグラム作成と保存#####
plt.hist(gray_img, bins = 256)
plt.xlim(0, 256)
plt.title('histogram',size=16)
plt.xlabel("pixel values")
plt.ylabel("frequency")
plt.savefig("histgram.png")

