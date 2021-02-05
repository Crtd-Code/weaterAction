#!/usr/bin/python3
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import random
import os
SKEY=os.environ.get('SKEY') #CoolPush酷推KEY
def getlovewords():
    # 获取情话
    texts=[]
    for page in range(1,89):
        url = 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_{}.html'.format(page)
        response = requests.get(url)
        soup=BeautifulSoup(response.text,'lxml')
        lovewordslist=soup.find('div',class_='list-short-article').find_all('a',target='_blank')
        texts.extend([lovewordslist[i].text for i in range(len(lovewordslist))])
    todaywords = texts[random.randint(0, len(texts) - 1)]  # 随机选取其中一条情话
    return todaywords
def CoolPush(info): #CoolPush酷推
    # cpurl = 'https://push.xuthus.cc/group/'+spkey   #推送到QQ群
    # cpurl = 'https://push.xuthus.cc/send/' + SKey  # 推送到个人QQ
    api='https://push.xuthus.cc/send/{}'.format(SKEY)
    print(api)
    print(info)
    requests.post(api, info.encode('utf-8'))
if __name__ == '__main__':
    info='晚安❤老婆\n'+getlovewords()
    CoolPush(info)
