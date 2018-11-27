# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:21:16 2017

@author: wking
"""

# !/usr/bin/python3.4
# -*- coding: utf-8 -*-


# 百度指数的抓取
# 截图教程：http://www.myexception.cn/web/2040513.html
#
# 登陆百度地址：https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F
# 百度指数地址：http://index.baidu.com

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pytesseract
# 打开浏览器
def openbrowser():
    global browser

    # https://passport.baidu.com/v2/?login
    url = "https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F"
    #url ="https://index.baidu.com/?tpl=trend&type=0&area=59&time=20151101%7C20151231&word=%D0%C2%C0%CB%CE%A2%B2%A9"
    # 打开谷歌浏览器
    # Firefox()
    # Chrome()
    browser = webdriver.Chrome("E:/download/chromedriver_win32/chromedriver.exe")
    # 输入网址
    browser.get(url)
    # 打开浏览器时间
    # print("等待10秒打开浏览器...")
    # time.sleep(10)

    # 找到id="TANGRAM__PSP_3__userName"的对话框
    # 清空输入框
    browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
    browser.find_element_by_id("TANGRAM__PSP_3__password").clear()

    # 输入账号密码
    # 输入账号密码
    account = []
    try:
        fileaccount = open("E:/download/chromedriver_win32/account.txt")
        accounts = fileaccount.readlines()
        for acc in accounts:
            account.append(acc.strip())
        fileaccount.close()
    except Exception as err:
        print(err)
        input("请正确在account.txt里面写入账号密码")
        exit()
    browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(account[0])
    browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys(account[1])

    # 点击登陆登陆
    # id="TANGRAM__PSP_3__submit"
    browser.find_element_by_id("TANGRAM__PSP_3__submit").click()

    # 等待登陆10秒
    # print('等待登陆10秒...')
    # time.sleep(10)
    print("等待网址加载完毕...")

    select = input("请观察浏览器网站是否已经登陆(y/n)：")
    while 1:
        if select == "y" or select == "Y":
            print("登陆成功！")
            print("准备打开新的窗口...")
            # time.sleep(1)
            # browser.quit()
            break

        elif select == "n" or select == "N":
            selectno = input("账号密码错误请按0，验证码出现请按1...")
            # 账号密码错误则重新输入
            if selectno == "0":

                # 找到id="TANGRAM__PSP_3__userName"的对话框
                # 清空输入框
                browser.find_element_by_id("TANGRAM__PSP_3__userName").clear()
                browser.find_element_by_id("TANGRAM__PSP_3__password").clear()

                # 输入账号密码
                account = []
                try:
                    fileaccount = open("E:/download/chromedriver_win32/account.txt")
                    accounts = fileaccount.readlines()
                    for acc in accounts:
                        account.append(acc.strip())
                    fileaccount.close()
                except Exception as err:
                    print(err)
                    input("请正确在account.txt里面写入账号密码")
                    exit()

                browser.find_element_by_id("TANGRAM__PSP_3__userName").send_keys(account[0])
                browser.find_element_by_id("TANGRAM__PSP_3__password").send_keys(account[1])
                # 点击登陆sign in
                # id="TANGRAM__PSP_3__submit"
                browser.find_element_by_id("TANGRAM__PSP_3__submit").click()

            elif selectno == "1":
                # 验证码的id为id="ap_captcha_guess"的对话框
                input("请在浏览器中输入验证码并登陆...")
                select = input("请观察浏览器网站是否已经登陆(y/n)：")

        else:
            print("请输入“y”或者“n”！")
            select = input("请观察浏览器网站是否已经登陆(y/n)：")


def getindex(keyword,city):
    openbrowser()
    time.sleep(2)

    # 这里开始进入百度指数
    # 要不这里就不要关闭了，新打开一个窗口
    # http://blog.csdn.net/DongGeGe214/article/details/52169761
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("https://index.baidu.com");'
    browser.execute_script(js)
    # 新窗口句柄切换，进入百度指数
    # 获得当前打开所有窗口的句柄handles
    # handles为一个数组
    handles = browser.window_handles
    # print(handles)
    # 切换到当前最新打开的窗口
    browser.switch_to_window(handles[-1])
    # 在新窗口里面输入网址百度指数
    # 清空输入框
    browser.find_element_by_id("schword").clear()
    # 写入需要搜索的百度指数
    browser.find_element_by_id("schword").send_keys(keyword)
    # 点击搜索
    # <input type="submit" value="" id="searchWords" onclick="searchDemoWords()">
    browser.find_element_by_id("searchWords").click()
    time.sleep(2)
    # 最大化窗口
    browser.maximize_window()
    # 构造天数
    #sel = '//a[@rel="' + str(day) + '"]'
    #browser.find_element_by_xpath(sel).click()
    # 太快了
    #确定城市
    browser.find_element_by_xpath('//span[@class="holdText"]').click()
    browser.find_element_by_xpath('//a[@href="#902"]').click()
    browser.find_element_by_xpath('//a[@href="#'+str(city)+'"]').click()
    browser.find_element_by_xpath('//a[@href="#cust"]').click()
    #确定时间
    #时间开始点
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[1]/span[2]/span[1]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[1]/span[2]/span[1]/div/a[5]').click()
    #browser.find_element_by_xpath('//a[@href="#2015"]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[1]/span[2]/span[2]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[1]/span[2]/span[2]/ul/li[2]/a[5]').click()
    #browser.find_element_by_xpath('//a[@href="#11"]').click()
    
    #时间结束点
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[2]/span[2]/span[1]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[2]/span[2]/span[1]/div/a[5]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[2]/span[2]/span[2]').click()
    browser.find_element_by_xpath('//div[@class="rangePanel"]/div[2]/span[2]/span[2]/ul/li[2]/a[6]').click()
    browser.find_element_by_xpath('//input[@value="确定"]').click()
    time.sleep(2)
    # 滑动思路：http://blog.sina.com.cn/s/blog_620987bf0102v2r8.html
    # 滑动思路：http://blog.csdn.net/zhouxuan623/article/details/39338511
    # 向上移动鼠标80个像素，水平方向不同
    # ActionChains(browser).move_by_offset(0,-80).perform()
    # <div id="trend" class="R_paper" style="height:480px;_background-color:#fff;"><svg height="460" version="1.1" width="954" xmlns="http://www.w3.org/2000/svg" style="overflow: hidden; position: relative; left: -0.5px;">
    # <rect x="20" y="130" width="914" height="207.66666666666666" r="0" rx="0" ry="0" fill="#ff0000" stroke="none" opacity="0" style="-webkit-tap-highlight-color: rgba(0, 0, 0, 0); opacity: 0;"></rect>
    # xoyelement = browser.find_element_by_xpath('//rect[@stroke="none"]')
    xoyelement = browser.find_elements_by_css_selector("#trend rect")[2]
    num = 0
    # 获得坐标长宽
    # x = xoyelement.location['x']
    # y = xoyelement.location['y']
    # width = xoyelement.size['width']
    # height = xoyelement.size['height']
    # print(x,y,width,height)
    # 常用js:http://www.cnblogs.com/hjhsysu/p/5735339.html
    # 搜索词：selenium JavaScript模拟鼠标悬浮
    x_0 = 444.9
    y_0 = 0

    # 储存数字的数组
    index = []
    try:
        # webdriver.ActionChains(driver).move_to_element().click().perform()
        # 只有移动位置xoyelement[2]是准确的
        for i in range(28):
            # 坐标偏移量???
            ActionChains(browser).move_to_element_with_offset(xoyelement,x_0,y_0).perform()
            x_0 = x_0 + 20
            # 构造规则
            '''if day == 7:
                x_0 = x_0 + 202.33
            elif day == 30:
                x_0 = x_0 + 41.68
            elif day == 90:
                x_0 = x_0 + 13.64
            elif day == 180:
                x_0 = x_0 + 6.78'''
                

            time.sleep(2)
            # <div class="imgtxt" style="margin-left:-117px;"></div>
            imgelement = browser.find_element_by_xpath('//div[@id="viewbox"]')
            # 找到图片坐标
            locations = imgelement.location
            print(locations)
            # 找到图片大小
            sizes = imgelement.size
            print(sizes)
            # 构造指数的位置
            rangle = (int(locations['x'] + sizes['width']*19/72), int(locations['y'] -160+ sizes['height']/2), int(locations['x'] + sizes['width']*53/72),
          int(locations['y']-160 + sizes['height']))
            # 截取当前浏览器
            path = "E:/download/chromedriver_win32/" + str(num)
            browser.save_screenshot(str(path) + ".png")
            # 打开截图切割
            img = Image.open(str(path) + ".png")
            jpg = img.crop(rangle)
            jpg.save(str(path) + ".jpg")

            # 将图片放大一倍
            # 原图大小91.29
            jpgzoom = Image.open(str(path) + ".jpg")
            (x, y) = jpgzoom.size
            x_s = 91*2
            y_s = 29*2
            out = jpgzoom.resize((x_s, y_s), Image.ANTIALIAS)
            out.save(path + 'zoom.jpg', 'png', quality=95)

            # 图像识别
            try:
                image = Image.open(str(path) + "zoom.jpg")
                code = pytesseract.image_to_string(image)
                if code:
                    index.append(code)
                else:
                    index.append("")
            except:
                index.append("")
            num = num + 1

    except Exception as err:
        print(err)
        print(num)

    print(index)
    # 日期也是可以图像识别下来的
    # 只是要构造rangle就行，但是我就是懒
    file = open("E:/download/chromedriver_win32/index.txt","w")
    for item in index:
        file.write(str(item) + "\n")
    file.close()

if __name__ == "__main__":
    # 每个字大约占横坐标12.5这样
    # 按照字节可自行更改切割横坐标的大小rangle
    keyword = input("请输入查询关键字：")
    sel = int(input("请输入你要查询的城市代码："))
    city = 10000
    
    if sel == 0:
        city =2 
        #贵阳
    elif sel == 1:
        city = 59
        #遵义
    elif sel == 2:
        city = 4
        #六盘水
    elif sel == 3:
        city = 3
        #黔南
    elif sel == 4:
        city = 426
        #毕节
    elif sel == 5:
        city = 424
        #安顺
    elif sel == 6:
        city = 422
        #铜仁
    elif sel == 7:
        city = 61
        #黔东南
    elif sel == 8:
        city = 588
        #黔西南
    getindex(keyword,city)
