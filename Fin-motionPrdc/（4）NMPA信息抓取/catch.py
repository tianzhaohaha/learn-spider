#但是NMPA页面的数据并非可以根据http://scxk.nmpa.gov.cn:81/xk/请求到，
# --因为这些数据是动态加载出来的
# --页面中对应的企业信息数据是ajax动态请求到的
# --关注json数据里面的ID信息
# --http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=f0ec03b4a6a64823b5362e8d3504ec6d
# --http://scxk.nmpa.gov.cn:81/xk/itownet/portal/dzpz.jsp?id=01c43d44e5f1461cbbb57c0e4959b7b5
#关注域名会发现，每家企业信息url只有ID不一样
#ID值可以从首页对应的XHR请求到的json串得到
#所以根据每家企业的ID值，可以拼接成每家企业信息的URL值

#ID可以从首页xhr请求得到
import requests
import json
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

#参数处理
data = {
    'on':'true',
    'page': '1',
    'pageSize':'15',
    'productName':'',
    'conditionType': '1',
    'applyname':'',
    'applysn':'',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3776.400 QQBrowser/10.6.4212.400'
}
json_ids = requests.post(url=url,headers = headers,data = data).json()#此时json是一个字典,id在list对应的value值

id_list = []#存储企业🆔
for dic in json_ids['list']:
    id_list.append(dic['ID'])
all_data_list = []#存储企业数据
#获取企业详情数据
post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data={
        'id':id
    }
    detail_json = requests.post(url=post_url,headers = headers,data=data).json()
    all_data_list.append(detail_json)

#持久化存储
fp = open('./alldata.json','w',encoding='utf-8')
json.dump(all_data_list,fp=fp,ensure_ascii=False)
print('over!')