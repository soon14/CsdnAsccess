import re
import requests

def get(url):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    html = requests.get(url, headers = head)
    html = html.text
    table = re.findall(r'<table .*?>(.*?)</table>', html, re.S)
    trlist = re.findall(r'<tr class.*?>(.*?)</tr>', str(table), re.S)
    tdlist = re.findall(r'<td>(.*?)</td>', str(trlist), re.S)
    iplist = {}
    j = 0
    i = 0
    while i < len(tdlist):
        iplist[j] = tdlist[i]
        i+=6
        j+=1
    return iplist