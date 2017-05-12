import os,sys
where=os.getcwd()
sys.path.append(where)


import re
import itertools
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen


# urlroot='https://www.gutenberg.org/files/1/1.txt'
urlroot='https://www.gutenberg.org/files/'
f=open('novels1000.txt','rb')
ids=[i.decode().strip() for i in f.readlines()]
f.close()

url=urlroot+str(ids[0])+'/'+str(ids[0])+'.txt'
print(url)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
req = urllib.request.Request(url, headers = headers)
res = urllib.request.urlopen(req)
# with urllib.request.urlopen(req) as res:
#     # txt=res.read()
#     # print(txt)
#     print(res.read())