#爬取搜狗首页数据

import requests
#1.指定url
url = 'https://www.sogou.com/'
#2.发起请求(get)
response = requests.get(url=url)
#3.获取相应数据
page_text = response.text

print(page_text)

#4.持久化存储
with open('./sogou.html','w',encoding='utf-8') as  fp:
    fp.write(page_text)

print('over')