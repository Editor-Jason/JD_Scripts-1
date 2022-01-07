import requests,os,json

cookie=''#pt_key=xxx;pt_pin=xxx;

url='https://wq.jd.com/deal/recvaddr/getrecvaddrlistV3?adid=&locationid=undefined&callback=cbLoadAddressListA&reg=1&encryptversion=1&r=0.7347212362931181&sceneval=2'
headers={
    "accept":"*/*",
    "accept-encoding":"gzip, deflate, br",
    "accept-language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ca;q=0.5",
    "cookie":cookie,
    "referer":"https://wqs.jd.com/",
    "sec-ch-ua":'" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":'"Windows"',
    "sec-fetch-dest":"script",
    "sec-fetch-mode":"no-cors",
    "sec-fetch-site":"same-site",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34"
    }
response=requests.get(url=url,headers=headers)
response=response.text.replace('cbLoadAddressListA(','').replace(')','')
for i in range(len(json.loads(response)['list'])):
    print(f'第{str(i+1)}个收获地址信息:')
    print('\n姓名:'+json.loads(response)['list'][i]['name'])
    print('\n地址:'+json.loads(response)['list'][i]['addrfull']+'\n\n')
os.system('pause')
