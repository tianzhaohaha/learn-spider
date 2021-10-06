from bs4 import BeautifulSoup
import requests


url = "http://guba.eastmoney.com/list,600519.html"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400"
}

page_text = requests.get(url = url, headers = header).text

soup = BeautifulSoup(page_text, 'lxml')

print(soup)
#print(soup.a)
#print(soup.div)#soup.TagName返回的事第一次出现的标签!!!标签？？？

#print(soup.find('div'))==print(soup.div)
#print(soup.find('div', class_= 'articleh normal_post odd'))#class要跟一个_，这样他就不是一个参数名称而是一个关键字了
#print(soup.find_all('a'))
#print(soup.select('div'))
#print(soup.select('body > div > div > div')[1])


#print(soup.select('body > div > div > div')[1].text)#即便不是直系的文本内容也可以获取
#print(soup.select('body > div > div .content'))#所以加上空格是在当前标签下不管往下深入几层都会找到content？


#print(soup.select('.gbbody > #mainbody > #articlelistnew >.articleh>span>a')[0]["title"])#ok

#with open('./test.html','w',encoding='utf-8') as fp:
#   fp.write(response)



