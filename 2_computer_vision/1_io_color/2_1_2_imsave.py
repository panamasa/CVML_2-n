#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-1-2 画像の読み込み
# 読み込んだsample.jpgをJPEG形式（.jpg）とPNG形式（.png）形式とBMP形式（.bmp）で保存し，結果を確認せよ．
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image

# 'r'ead mode
filename = 'image/sample.tif'
img = Image.open(filename, 'r')

# save images
img.save('result/sample.jpg', 'JPEG')
img.save('result/sample.png', 'PNG')
img.save('result/sample.bmp', 'BMP')
