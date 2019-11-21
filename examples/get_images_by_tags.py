# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:27:42 2019

@author: r0772291


从instagram中抓取和目标主题相关的数据
理想的排序方式：
先抓取一段时间内的数据，按照热度进行排序，取一段时间内前x条数据
"""

from context import Instagram # pylint: disable=no-name-in-module
import time
import pymongo
import datetime
from time import sleep
import threading
# 连接数据库
client = pymongo.MongoClient(host='localhost', port=27017) #连接本地mongodb数据库
DATABASE = client["Instagram_test"]

#登陆账号
instagram = Instagram()
instagram.with_credentials('mollyc773', 'qq767138291', 'path/to/cache/folder')
instagram.login()

#设置数据的开始时间
#startTime = time.mktime(time.strptime("2019/11/21 16:50:00","%Y/%m/%d %H:%M:%S"))
#endTime = time.mktime(time.strptime("2019/11/21 16:55:00","%Y/%m/%d %H:%M:%S"))
# 要获取的主题
SUBJECTS = ["Cocacola","Chevron","Cocacola","Intel","UrbanOutfitters", "Dow Jones", "Nasdaq", "S&P500","KBC Bank", "Nestle"]
#arr, medias = instagram.get_medias_by_tag(tag=SUBJECTS[0], count=100, max_id='', min_timestamp=startTime)

#arr, medias = instagram.get_medias_by_tag(tag=SUBJECTS[0], count=100, max_id='', min_timestamp=startTime)
#instagram.get_current_top_medias_by_tag_name(SUBJECTS[0])
def insertData(START_TIME, ONESUBJECT):
    collection = DATABASE[ONESUBJECT]
    medias = instagram.get_medias_by_tag(ONESUBJECT, count=500, min_timestamp=START_TIME) #获取从指定时间到现在的数据
    for one in medias:
        oneImage = {}
        oneImage['urlToImage'] = one.__dict__["image_high_resolution_url"]
        oneImage['publishedAt'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(one.__dict__["created_time"]))
        oneImage['content'] = one.__dict__["caption"]
        oneImage['likes'] = one.__dict__["likes_count"]
        oneImage['url'] = one.__dict__["link"]
        
        collection.insert_one(oneImage)
    print ('%r has been completed!'%ONESUBJECT)
    
class MyThread(threading.Thread):
    def __init__(self, func, args, name='', ):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
        self.result = None
        
    def run(self):
        print('开始子进程{}'.format(self.name))
        self.result = self.func(self.args[0], self.args[1])
        print("结果: {}".format(self.result))
        print('结束子进程{}'.format(self.name))    
    
    
if __name__ == "__main__":
    while True:
        now = datetime.datetime.now()
        startTime = now+datetime.timedelta(hours=-1)
        startTime = time.mktime(time.strptime(str(startTime)[:19], "%Y-%m-%d %H:%M:%S"))
        endTime = now
        if now.minute == 15:
            threads = []
            for oneColl in SUBJECTS:
                t = MyThread(insertData, (startTime, oneColl))
                threads.append(t)
                
            for t in threads:
                t.start()
            for t in threads:
                t.join()

        sleep(60) 


# 测试没一个函数的作用
'''
# 1. 根据id返回账户， 不太对  
account = instagram.get_account_by_id('16495588565') 

# 2. 根据id返回用户名
username = instagram.get_username_by_id('16495588565') 
'''    
    
    
    
    
    


