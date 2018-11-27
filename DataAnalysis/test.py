# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:21:02 2017

@author: wking
"""
# -*- coding: utf-8 -*-

class transCookie:
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        '''
        将从浏览器上Copy来的cookie字符串转化为Scrapy能使用的Dict
        :return:
        '''
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict

if __name__ == "__main__":
    cookie = 'll="118254"; bid=YhjAuTuwIEU; viewed="1027666"; gr_user_id=e81464af-6f8a-4f24-b54e-72169b248e0d; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1512475903%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=7217D8FF50F11D17D338D2DDC0271A3F|6a7a85ff1136f45918994eaf03e7991b; ps=y; ap=1; push_noty_num=0; push_doumail_num=0; __utma=30149280.187883215.1512467993.1512467993.1512475899.2; __utmb=30149280.1.10.1512475899; __utmc=30149280; __utmz=30149280.1512467993.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1390399399.1512475903.1512475903.1512475903.1; __utmb=223695111.0.10.1512475903; __utmc=223695111; __utmz=223695111.1512475903.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=c3d88406c1868f83.1512475903.1.1512479011.1512475903.; _pk_ses.100001.4cf6=*; ck=sdz7; ue="wangkun91@163.com"; dbcl2="60923793:pjA2WeG5Wfg"'
    trans = transCookie(cookie)
    print trans.stringToDict()



