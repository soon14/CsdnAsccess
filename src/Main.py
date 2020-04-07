import requests
import time
import threading

from src import GetTitleUrl
from src import GetIp


head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
url = ""    #放入URL


def run(iplist, titleurl, num):
    while True:
        i = 0
        while i < len(iplist):
            j = i
            j%=len(titleurl)
            ip = {"http": iplist[i]}
            requests.get(titleurl[j], headers=head, proxies=ip)
            print("时间：" + time.asctime(time.localtime(time.time())), end=" ")
            print("线程："+str(num), end=' ')
            print("使用IP："+iplist[i], end=" ")
            print("访问博客："+titleurl[j])
            i+=1

if __name__ == '__main__':
    titleurl = GetTitleUrl.get(url)
    iplist1 = GetIp.get("https://www.xicidaili.com/nn/1")
    iplist2 = GetIp.get("https://www.xicidaili.com/nn/2")
    iplist3 = GetIp.get("https://www.xicidaili.com/nn/3")
    iplist4 = GetIp.get("https://www.xicidaili.com/nn/4")
    iplist5 = GetIp.get("https://www.xicidaili.com/nn/5")
    iplist6 = GetIp.get("https://www.xicidaili.com/nn/6")
    t1 = threading.Thread(target=run, args=(iplist1, titleurl, 1,))
    t2 = threading.Thread(target=run, args=(iplist2, titleurl, 2,))
    t3 = threading.Thread(target=run, args=(iplist3, titleurl, 3,))
    t4 = threading.Thread(target=run, args=(iplist4, titleurl, 4,))
    t5 = threading.Thread(target=run, args=(iplist5, titleurl, 5,))
    t6 = threading.Thread(target=run, args=(iplist6, titleurl, 6,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()