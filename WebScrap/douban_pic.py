# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 20:28:42 2017

@author: wking
"""
from bs4 import BeautifulSoup
import requests

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "爬取失败！！！"

def fillPicList(picname_list,html):
    soup1=BeautifulSoup(html,"html.parser")#也可使用lxml
    soup=soup1.find("ol",{"class","grid_view"})
    for movie_li in soup.find_all("li"):
        pic=movie_li.find("img").get('src')#获取Src对应的链接
        picname_list.append(pic) 

def savePic(picname_list):
      root="E://pic//"
      try:
          for pic in picname_list:
              path=root+pic.split('/')[-1]
              c=requests.get(pic)
              with open (path,'wb')as f:
                   f.write(c.content)#获取链接内容——图片
                   f.close()     
          print("文件已经保存")
      except:
          print("爬取失败")

def main():
    picname_list=[]
    url1="https://movie.douban.com/top250?start="
    for i in range(0,10):
        url=url1+str(i*25)
        html=getHTMLText(url)
        fillPicList(picname_list,html)
        savePic(picname_list)
main()
                  
                
          
          
              
              
                  
                   
          
            
      
            
               
            


    
   
        
   

    