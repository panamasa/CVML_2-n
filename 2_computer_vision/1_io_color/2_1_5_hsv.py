#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-1-5 HSV色空間
# imageディレクトリにあるsample.tifを読み込み，HSV色空間に変換した後以下の画像をそれぞれ作成し，結果を確認せよ．  
# Pillowとmatplotlibによる解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image
import numpy as np
import matplotlib

# 'r'ead mode
filename = 'image/sample.tif'
img = Image.open(filename, 'r')
ary_img = np.asarray(img, dtype=np.float32)
ary_img /= 255.

# get HSV color array
ary_hsv = matplotlib.colors.rgb_to_hsv(ary_img)

# 1. 赤色の画素が緑色に，緑色の画素が青色に，青色の画素が赤色になるように全画素の色相を等しく変更した画像
ary_h_changed = ary_hsv.copy()
ary_h_changed[:,:,0] += 1. / 3.
ary_h_changed -= ary_h_changed > 1.
ary_h_changed = matplotlib.colors.hsv_to_rgb(ary_h_changed) * 255
img_h_changed = Image.fromarray(np.uint8(ary_h_changed))
img_h_changed.save('result/sample_change_hue.png')

# 2. 全画素の彩度に対し，全画素で一定の0~1までの乱数値を掛けて彩度を変更した画像
ary_s_changed = ary_hsv.copy()
ary_s_changed[:,:,1] *= np.random.rand()
ary_s_changed = matplotlib.colors.hsv_to_rgb(ary_s_changed) * 255
img_s_changed = Image.fromarray(np.uint8(ary_s_changed))
img_s_changed.save('result/sample_change_sat.png')

# 3. 全画素の明度に対し，画素毎に異なる0.5~0.8までの乱数を足して明度を変更した画像（値の飽和に注意すること）
ary_v_changed = ary_hsv.copy()
ary_v_changed[:,:,2] += np.random.rand(ary_v_changed.shape[0], ary_v_changed.shape[1]) * 0.3 + 0.5
ary_v_changed = ary_v_changed.clip(max=1.0)
ary_v_changed = matplotlib.colors.hsv_to_rgb(ary_v_changed) * 255
img_v_changed = Image.fromarray(np.uint8(ary_v_changed))
img_v_changed.save('result/sample_change_val.png')
