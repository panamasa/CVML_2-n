#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
03:文字数カウント
    英語のみ、日本語対応両方示しておきます
"""

import sys

string = sys.argv[1]
print string, len(string)

# 日本語を含めて行う場合はこうなります
string_jp = sys.argv[2]
string_jp = unicode( string_jp , "utf-8")

print string_jp, len(string_jp)
