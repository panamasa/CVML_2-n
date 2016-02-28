#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-1-3 グレースケール画像を作る
# imageディレクトリにあるlena.tifを読み込み，その画像のグレースケール画像を作成し，結果を保存せよ．
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image

# 'r'ead mode
filename = 'image/lena.tif'
img = Image.open(filename, 'r')

# convert to Grayscale using Pillow function
img_gray_pil = img.convert('L')
img_gray_pil.save('result/lena_gray_pil.png')

# convert to Grayscale using Numpy
import numpy as np
# get numpy array (32 bit float) from PIL Image object
ary_color = np.asarray(img, dtype=np.float32)
# NTSC YIQ Color Model Conversion ( Y = 0.2999*R + 0.587*G * 0.114*B)
ary_gray = 0.2999 * ary_color[:,:,0] + 0.587 * ary_color[:,:,1] + 0.114 * ary_color[:,:,2]
# back to PIL Image object (8 bit unsigned int)
img_gray_np = Image.fromarray(np.uint8(ary_gray))
img_gray_np.save('result/lena_gray_np.png')
