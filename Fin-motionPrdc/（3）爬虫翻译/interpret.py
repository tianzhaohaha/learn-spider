#获取页面中局部的数据
#需求仅是翻译结果，根据输入字符不同，页面会进行局部刷新
#ALL对应的是当前页面中所有请求对应的数据包，这里需要XHR请求

#point1:
#-POST请求（携带了参数）
#如何使用requests发送post请求

#point2
#相应数据是一组json数据

import requests
import json
post_url = 'https://fanyi.baidu.com/sug'#从抓包工具中查看的
#step1:post请求参数处理
word = input('enter a word:')
data = {
    'kw':word
}
#step2:进行UA伪装
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'

}

#step3:进行查找
response = requests.post(url = post_url,data= data,headers = headers)

#step4:获取相应数据,调用json方法，返回的事obj，若确认服务器相应数据是json类型的才行
#在response Headers里content-Type里查找
dic_obj=response.json()
fileName = word+'.json'
fp = open(fileName,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)

print('over!')

