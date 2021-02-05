import requests
#推送标题
text='天气推送'
#推送内容
desp='你好呀'
#Server酱的SCKEY
sckey = 'SCU120580T45a16bea7f3739f7654203489fbe69115fa8d55bbed50'#在发送消息页面可以找到
url = 'https://sc.ftqq.com/%s.send?text=%s&desp=%s'%(sckey,text,desp)
print(url)
requests.get(url)
