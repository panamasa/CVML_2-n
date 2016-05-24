#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CNNを作成した。get_image_tensorのオブジェクトを作成してデータセットを読み込む。
読み込んだデータセットをCNNに投げる。
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


#1_1_1
output = 'Hello Python'
print(output)

#1_1_2
print('len=', len(output))

#1_1_3
import sys
param = sys.argv
output = param[1]
print(output)
print('len of word{}'.format(len(output)))

