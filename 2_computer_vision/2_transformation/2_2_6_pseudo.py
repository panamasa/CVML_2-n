#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-2-6 疑似カラー
# imageディレクトリにあるgray_sample.pngを疑似カラーで表現された画像を作成せよ．
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image
import numpy as np

def hist_equalization(ary):
    hist, bins = np.histogram(ary.flatten(), bins=256)
    cdf = hist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    ary_eq = np.interp(ary.flatten(), bins[:-1], cdf).reshape(ary.shape)
    return ary_eq

def pseudo_color(ary):
    lut = np.ndarray((256, 3), dtype=np.uint8)
    for v in xrange(256):
        r = 0 if v<= 127 else 3.5*v-446.5 if 127<v<=191 else 255
        g = 3.5*v if v<=63 else 255 if 63<v<=191 else -3.5*v+896.5
        b = 255 if v<=63 else -3.5*v+444.5 if 63<v<=127 else 0
        lut[v] = [r, g, b]
    ary_pseudo = np.zeros((ary.shape[0], ary.shape[1], 3), dtype=np.uint8)
    for c in xrange(ary.shape[0]):
        for r in xrange(ary.shape[1]):
            ary_pseudo[c,r] = lut[ary[c,r]]
    return ary_pseudo

filename = 'image/gray_sample.png'
img = Image.open(filename, 'r')
ary_img = np.asarray(img, dtype=np.uint8)
ary_img = hist_equalization(ary_img)

# output image array
ary_pseudo = pseudo_color(ary_img)
img_pseudo = Image.fromarray(ary_pseudo)
img_pseudo.save('result/pseudo_color.png')
