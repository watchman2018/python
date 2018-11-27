# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymysql
import time
import re
import requests
from bs4 import BeautifulSoup
import csv
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败！！！"
                 
def fillUnivList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list,html):
    soup1=BeautifulSoup(html,"html.parser")
    soup=soup1.find("ol",{"class","grid_view"})
    for movie_li in soup.find_all("li"):
        movie_name=movie_li.find("span",{"class":"title"}).get_text()
        #这里用get_text()而不用。string，防止出现空值。
        movie_name_list.append(movie_name)
        movie_rating=movie_li.find("span",{"class":"rating_num"}).get_text()
        movie_rating_list.append(movie_rating)
        movie_comment=movie_li.find("span",{"class":"inq"})
        if movie_comment is None:
            #有些电影没有评论，此处需要判断，以免出现空值。
            movie_comment_list.append('')
        else:
            movie_comment_list.append(movie_comment.get_text())
        #movie_count=movie_li.find('span', {'class': 'rating_num'}).next_sibling().next_sibling().get_text()
        #movie_count_list.append(movie_count)
        movie_count_list.append(re.findall(re.compile(r'<span>(\d*)人评价</span>'),str(movie_li.find_all('div',class_='star')))[0])
def printUnivList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list):
    print("{:<10}\t{:<10}\t{:<20}\t{:<15}".format("电影名称","电影评分","电影评论","评论人数"))
    for i in range(len(movie_name_list)):
        print("{:<10}\t{:<10}\t{:<20}\t{:<15}".format(movie_name_list[i],movie_rating_list[i],movie_comment_list[i],movie_count_list[i]))
        
def saveList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list):
    csvFile=open(r"E:/test.csv",'w+')
    try:
        write=csv.writer(csvFile,lineterminator='\n')
        #防止保存文件是出现空行
        write.writerow(["电影名称","电影评分","电影评论","评论人数"])
        for i in range(len(movie_name_list)):
            write.writerow([movie_name_list[i].encode('gbk', 'ignore').decode('gbk'),movie_rating_list[i].encode('gbk', 'ignore').decode('gbk'),movie_comment_list[i].encode('gbk', 'ignore').decode('gbk'),movie_count_list[i].encode('gbk', 'ignore').decode('gbk')])
    #encode('gbk', 'ignore').decode('gbk') 主要防止保存文件出现乱码
    finally:
        csvFile.close()

def save_to_MySQL(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list):
    print("Mysql文件存储中")
    try:
        conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="test",charset="utf8")
        cursor=conn.cursor()#创建一个游标对象
        print("数据库连接成功")
        cursor.execute('Drop table if EXISTS MovieTOP250')
        time.sleep(3)
        cursor.execute('''create table if not EXISTS MovieTop250(id INT(10),movie_name_list VARCHAR(200),movie_rating_list VARCHAR(200),movie_comment_list VARCHAR(200),movie_count_list VARCHAR(200))''')
        for i in range(len(movie_name_list)):
            sql='insert into MovieTop250(id,movie_name_list,movie_rating_list,movie_comment_list,movie_count_list) VALUES(%s,%s,%s,%s,%s)'
            parm=(i+1,movie_name_list[i],movie_rating_list[i],movie_comment_list[i],movie_count_list[i])
            cursor.execute(sql,parm)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    print("MySQL数据库存储结束！！！")

def main():
    movie_name_list=[]
    movie_rating_list=[]
    movie_comment_list=[]
    movie_count_list=[]
    url1="https://movie.douban.com/top250?start="
    for i in range(0,10):
        url=url1+str(i*25)
        html=getHTMLText(url)
        fillUnivList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list,html)
    #printUnivList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list)
    saveList(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list)
    #save_to_MySQL(movie_name_list,movie_rating_list,movie_comment_list,movie_count_list)
main()

