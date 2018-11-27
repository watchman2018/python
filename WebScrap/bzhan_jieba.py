#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time      :2018/3/17 19:12
#@Author    :watchman2018
#@File      :bzhan.py
import os
import jieba
import jieba.analyse
import xlwt  # 写入Excel表的库
import sys
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf8')
tokens = []
stop_words = []
stop_words_file_list = [
    "stop_words/hit_stop_words.txt",
    "stop_words/baidu_stop_words.txt",
    "stop_words/zh_cn_stop_words.txt",
]
for file_path in stop_words_file_list:
    with open(os.path.join(os.path.dirname(__file__), file_path)) as f:
        lines = f.readlines()
        for line in lines:
            stop_words.append(line.strip().decode('utf-8'))
with open(os.path.join(os.path.dirname(__file__), "xueqiu.txt")) as f:
    lines = f.readlines()
    for line in lines:
        clean_line = line.strip().decode('utf-8')
        if len(clean_line) > 0:
            seg_list = jieba.cut(clean_line)
            for seg in seg_list:
                if seg not in stop_words:
                    tokens.append(seg)
counter = Counter(tokens)
for a in counter.most_common(10):
    print(a[0] + '\t' + str(a[1]))

