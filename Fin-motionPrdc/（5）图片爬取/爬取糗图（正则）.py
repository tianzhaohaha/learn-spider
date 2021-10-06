import requests
import re
import os

url = 'https://www.qiushibaike.com/imgrank/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'
}
#创建一个文件夹保存图片
if not os.path.exists('./qiutuLibs'):
    os.mkdir('./qiutuLibs')

#使用通用爬虫对url页面进行爬取
page_text = requests.get(url = url,headers = headers).text

#使用聚焦爬虫将页面中所有的糗图进行解析对img里的src图片地址爬取
ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'

img_src_list = re.findall(ex, page_text, re.S)#re.S代表数据解析型爬取？

#我们对list地址逐一请求就可以了
for src in img_src_list:
    src = 'https:'+src#拼接https：组合为完整的图片地址
    img_data = requests.get(url = src, headers = headers).content
    #生成图片名称
    img_name = src.split('/')[-1]
    #图片存储路径
    img_path = './qiutuLibs/'+img_name

    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name,'save!')



