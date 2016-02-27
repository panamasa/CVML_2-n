#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
