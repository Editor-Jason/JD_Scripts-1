import requests
import threading
import json
import time
import sys
import os

#https://github.com/Hyper-Beast/JD_Scripts


#userid和token打开个人资料设置在链接里就能看到了，phone就是手机号，不确定填别人的行不行，个人资料里必须填好餐馆信息那些要不然无法兑换，随便填就行
#中午12点开始跑差不多，一般在下午2-3点补货，自己注意青龙的脚本最长运行时间是多少


userid=''
token=''
phone=''
giftid='62'#633电信15积分10元，631移动45积分30元，62联通7积分5元，61联通3积分2元


def printf(text):
    print(text)
    sys.stdout.flush()

printf('太太乐兑换开始运行，补货前程序不会有任何信息输出')

def getstockamount():
    url=f'https://www.ttljf.com/ttl_site/giftApi.do?giftId={giftid}&mthd=giftDetail&userId={userid}'
    headers={
        'Host':'www.ttljf.com',
        'Accept':'*/*',
        'Cookie':'agreePrivacy=false; JSESSIONID=9FEE883D1880639CDFFF76F1790EF4D5',
        'User-Agent':'Totole/1.4.8 (iPhone; iOS 15.1.1; Scale/3.00)',
        'Accept-Language':'zh-Hans-CN;q=1',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'
            }
    while True:
        try:
            response=requests.get(url=url,headers=headers)
            if json.loads(response.text)['gifts']['stockAmount']!=0:
                for i in range(20):
                    try:
                        t1 = threading.Thread(target=exchange())
                        t1.start()
                    except:
                        pass
        except:
            pass
        time.sleep(10)
def exchange():
    url=f'https://www.ttljf.com/ttl_site/chargeApi.do?giftId={giftid}&loginToken={token}&method=charge&mobile={phone}&userId={userid}'
    headers={
        'Host':'www.ttljf.com',
        'Accept':'*/*',
        'Cookie':'agreePrivacy=false; JSESSIONID=9FEE883D1880639CDFFF76F1790EF4D5',
        'User-Agent':'Totole/1.4.8 (iPhone; iOS 15.1.1; Scale/3.00)',
        'Accept-Language':'zh-Hans-CN;q=1',
        'Accept-Encoding':'gzip, deflate, br',
        'Connection':'keep-alive'
            }
    try:
        response=requests.get(url=url,headers=headers)
        print(response.text)
        if response.text.find('成功')!=-1:
            printf('太太乐兑换成功')
        else:
            printf(response.text)
    except:
        printf('兑换出错')
getstockamount()