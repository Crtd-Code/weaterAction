import requests
from bs4 import BeautifulSoup
import random
import os
import time
from lxml import etree
SKEY=os.environ.get('SKEY') #CoolPush酷推KEY
ips = []  # 装载有效 IP
def getIP():
    for i in range(1, 5):
        headers = {
            "User-Agent": UserAgent().chrome  # chrome浏览器随机代理
        }
        ip_url = 'http://www.xiladaili.com/gaoni/{}/'.format(i)
        html = requests.get(url=ip_url, headers=headers).text
        seletor = etree.HTML(html)
        ip_list = seletor.xpath('/html/body/div/div[3]/div[2]/table/tbody/tr/td[1]/text()')
        for i in range(len(ip_list)):
            ip = "http://" + ip_list[i]
            # 设置为字典格式
            proxies = {"http": ip}
            try:
                # 使用上面的IP代理请求百度，成功后状态码200
                baidu = requests.get("http://myip.ipip.net/", proxies=proxies,timeout=3)
                if baidu.status_code == 200:
                    print(proxies,baidu.text)
                    ips.append(proxies)
            except:
                print('错误')

        print("正在准备IP代理，请稍后。。。")
def getlovewords():
        # getIP()
    headers={
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Mobile Safari/537.36'
    }
    # 获取情话
    texts=[]
    for page in range(1,2):
        time.sleep(3)
        # proxy = ips[random.randint(0, len(ips) - 1)]
        # print(proxy)
        url = 'https://www.duanwenxue.com/huayu/tianyanmiyu/list_{}.html'.format(page)
        try:
            response = requests.get(url,headers=headers)
            soup=BeautifulSoup(response.text,'lxml')
            lovewordslist=soup.find('div',class_='list-short-article').find_all('a',target='_blank')
            # print(lovewordslist)
            texts.extend([lovewordslist[i].text for i in range(len(lovewordslist))])
        except:
            print("连接失败")
    if(len(texts)==0):
        print("情话集合为空")
        return
    else:
        todaywords = texts[random.randint(0, len(texts) - 1)]  # 随机选取其中一条情话
        return todaywords
def CoolPush(info): #CoolPush酷推
    # cpurl = 'https://push.xuthus.cc/group/'+spkey   #推送到QQ群
    # cpurl = 'https://push.xuthus.cc/send/' + SKey  # 推送到个人QQ
    api='https://push.xuthus.cc/send/{}'.format(SKEY)
    print(info)
    r=requests.post(api, info.encode('utf-8'))
    if(r.status_code==200):
        print("推送成功")
if __name__ == '__main__':
    str1='晚安❤老婆\n'+getlovewords()
    str2='晚安❤老婆\n'+getlovewords()
    str3='晚安❤老婆\n'+getlovewords()
    print(str1)
    print(str2)
    print(str3)
    CoolPush(str1)
    CoolPush(str2)
    CoolPush(str3)
