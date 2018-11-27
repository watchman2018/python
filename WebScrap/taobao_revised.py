#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-13
# @Author  : wking (wang_king2017@163.com)
# @Link    : www.wking.com
# @Version : $Id$
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 21:48:43 2017
"""
import requests
import re
import csv
def getHtmlText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("爬取失败！！！")

def parsePage(booklist,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        loc=re.findall(r'\"item_loc\"\:\".*?\"', html)
        sales=re.findall(r'\"view_sales\"\:\".*?\"', html)
        comment=re.findall(r'\"comment_count\"\:\".*?\"', html)
        for i in range(len(plt)):  
           price=eval(plt[i].split(':')[1])
           location=eval(loc[i].split(':')[1])
           salescount=eval(sales[i].split(':')[1])
           commentcount=eval(comment[i].split(':')[1])
           booklist.append([price,location,salescount,commentcount])                    
    except:
        print("定位错误！！！")
def printBookList(booklist):
    tplt="{0:^2}\t{1:^3}\t{2:^10}\t{3:>10}\t{4:>5}"
    print(tplt.format("序号","价格","商品位置","商品销量","评论人数"))
    count=0
    for i in booklist:
        count=count+1
        print(tplt.format(count,i[0],i[1],i[2],i[3]))

def saveBookList(booklist):
    csvFile=open(r"E:/taobao.csv",'w+')
    try:
        write=csv.writer(csvFile,lineterminator='\n')
        write.writerow(["序号","价格","商品位置","商品销量","评论人数"])
        n=0
        for i in booklist:
            n=n+1
            write.writerow([n,i[0],i[1],i[2],i[3]])
    finally:
        csvFile.close()
def main():
    goods="围城"
    booklist=[]
    url1="https://s.taobao.com/search?q="+goods
    for i in range(0,1):
        try:
            url=url1+'&s'+str(i*44)
            html=getHtmlText(url)
            parsePage(booklist,html)
        except:
            continue
    printBookList(booklist)
    saveBookList(booklist)
main()  
    
