#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-09-02
# @Author  : wking (wang_king2017@163.com)
# @Link    : www.wking.com
# @Version : $Id$


import re
import jieba
import numpy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 8.0)
from wordcloud import WordCloud#词云包

#加载数据文件
path=r'e:/wecomment.csv'
f=open(path,'r',encoding='utf-8')
data=pd.read_csv(f)
comments=data['comment']
count=23391

#保留文本中的中文词
def Chinese(text):
    cleaned = re.findall(r'[\u4e00-\u9fa5]+',text)  #返回列表
    cleaned = ''.join(cleaned)                      #拼接成字符串
    return cleaned

new_comment=Chinese(str(comments))
segment=jieba.lcut(new_comment)
words_df=pd.DataFrame({'segment':segment})
stopwords=pd.read_csv(r"e://stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')#quoting=3全不引用
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
    #词频分析
words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)

wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80) #指定字体类型、字体大小和字体颜色
word_frequence = {x[0]:x[1] for x in words_stat.head(40000).values}
wordcloud=wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)
wordcloud.to_file("e://wecomment.jpg")