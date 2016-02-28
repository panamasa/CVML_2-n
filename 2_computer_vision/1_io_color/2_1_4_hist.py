#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-1-4 ヒストグラムを作る
# 前問で作成したグレースケール画像のヒストグラムをプロットし，確認せよ．　　
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image
import numpy as np
import matplotlib
matplotlib.use('Agg') # no use Display Output
import matplotlib.pyplot as plt

# 'r'ead mode
filename = 'result/lena_gray_pil.png'
img = Image.open(filename, 'r')

# plot histogram
hist = np.asarray(img).flatten()
plt.hist(hist, bins=256)
plt.title(filename + ' Histogram')
plt.xlabel('Value')
plt.ylabel('Value')
plt.ylabel('frequency')
plt.savefig('result/hist.png')
