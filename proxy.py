import requests
from threading import Thread
from os import system
from time import sleep


proxies = []
proxies_checked = []

myip = requests.get('http://ipinfo.io/json').json()['ip']

def check(p):
    proxies = {
        'http': 'http://'+p,
        'https': 'https://'+p,
    }
    try:
        r = requests.get('http://ipinfo.io/json', proxies=proxies,timeout=5).json()
        if r['ip'] != myip:
            proxies_checked.append(p)
    except:
        exit()

def get(api):

    r = requests.get(api,timeout=5)
    proxies.append(str(r.text).replace('\r','').split('\n'))



http_api = [
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://api.openproxylist.xyz/http.txt",
     "http://alexa.lr2b.com/proxylist.txt",
    "https://multiproxy.org/txt_all/proxy.txt",
     "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
    "https://openproxylist.xyz/http.txt",
    "https://proxyspace.pro/http.txt",
    "https://proxyspace.pro/https.txt",
    "https://rootjazz.com/proxies/proxies.txt",
    "https://www.proxy-list.download/api/v1/get?type=https",
]
for api in http_api:
    get(api)

system('cls')
for proxy in proxies:
    for p in proxy :
        Thread(target=check,args=(p,)).start()

sleep(120)

f = open('proxy.txt','w')
for proxy in proxies_checked:
    f.write(proxy + '\n')
f.close()