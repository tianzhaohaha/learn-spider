
#UA检测:门户网站的服务器回检测对应请求的载体身份表示，若为某一款浏览器，则正常请求，反之若为一个爬虫程序的话。。。
#则服务器很可能拒绝请求
# UA=User-Agent
#故要进行UA伪装：将爬虫对应的UA信息伪装成某一款浏览器
import requests
#step1:构建一个动态url
url = 'https://www.sogou.com/web?'
#将URL携带的参数封装到字典中
kw = input('enter a query:')
param = {
    'query':kw
}
headers= {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'

}


#对指定的URL发起请求，且此URL经过处理
response= requests.get(url = url, params= param,headers = headers)
page_text = response.text
FileName = kw+'.html'
with open(FileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)

print(FileName,'successfully save')