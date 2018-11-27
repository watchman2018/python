# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 14:55:41 2018

@author: wking
"""
import xml.etree.ElementTree as ET
import csv
import time

danmu_list=[]
all_list=[]
tree=ET.ElementTree(file=r'D:/Bzhan/all.xml')

def sec2str(seconds):
    seconds = eval(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time = "%02d:%02d:%02d" % (h, m, s)
    return time 

for elem in tree.iter("d"):
    elem1=elem.attrib
    danmu_list=elem1['p'].split(',')
    if elem is None:
        danmu_list.append("")
    else:
        danmu_list.append(elem.text)
    danmu_list[0] = sec2str(danmu_list[0])
    danmu_list[4] = time.ctime(eval(danmu_list[4]))
    all_list.append(danmu_list)



tableheader = ['出现时间', '弹幕模式', '字号', '颜色', '发送时间' ,'弹幕池', '发送者id', 'rowID', '弹幕内容']
with open(r'E:/test1.csv', 'w', newline='', errors='ignore') as f:
    writer = csv.writer(f)
    writer.writerow(tableheader)
    for row in all_list:
        writer.writerow(row)
f.close()      
        
        
        
            
    
