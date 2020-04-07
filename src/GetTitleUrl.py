import requests
import re


def get(url):
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}
    html = requests.get(url, headers=head)
    html = html.text
    text = re.findall(r"<main>(.*?)</main>", html, re.S)
    text1 = re.findall(r'<div class="article-list">(.*)</div>', str(text), re.S)

    titleurls = re.findall(r'<a href="(.*?)" target="_blank">.*?</a>', str(text1), re.S)

    titleurl={}

    length = len(titleurls)
    length2 = int(length/2) 
    i = 0

    for j in range(length2):
        titleurl[j] = titleurls[i]
        i+=2
    return titleurl


