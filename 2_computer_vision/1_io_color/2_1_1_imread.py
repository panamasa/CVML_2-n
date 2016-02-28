#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 問題2-1-1 画像の読み込み
# imageディレクトリにあるsample.tifを読み込み，その画像サイズとカラーチャンネル数を取得せよ．
# Pillowでの解答例
# Author: Daiki SHIMADA a.k.a kantoku

from PIL import Image

# 'r'ead mode
filename = 'image/sample.tif'
img = Image.open(filename, 'r')

# get image size and color channel
height, width = img.size
channel = img.mode
print 'height', height
print 'width', width
print 'channel', channel
