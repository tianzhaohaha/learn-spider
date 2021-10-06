#爬取糗事百科中所有糗事板块下糗图
#类似动态：作者，文字，图片
import requests
#从图片地址爬取图片
#下面的地址是随意写的
url = 'https://pic.qiushibaike.com/system/pictures/12474/124747983/medium/YTJ4LMT9K3Y7A9V0.jpg'
#图片返回的数据为二进制形式
img_data = requests.get(url = url).content
#text-字符串，content-二进制，json-对象类型的数据
with open('./糗图.jpg','wb') as fp:
    fp.write(img_data)