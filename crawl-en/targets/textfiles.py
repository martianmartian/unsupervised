import os,sys
where=os.getcwd()
sys.path.append(where)


import re
import itertools
import urllib.parse
import urllib.request
from urllib.request import Request,urlopen

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#         # break


def getAsave(urlroot,filename,savedir,savename):
    url=urlroot+filename
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    req = urllib.request.Request(url, headers = headers)
    try:
        res = urllib.request.urlopen(req)
        stuff=res.read().decode()
        out=open(savedir+savename,'w')
        out.write(stuff)
        out.close()
        res.close()
    except ValueError:
        print("this one broke")
        print(savename)

# urlroot='http://www.textfiles.com/stories/100west.txt'
urlroot='http://www.textfiles.com/stories/'
f=open('textfiles.txt','rb')
ids=[i.decode().strip() for i in f.readlines()]
f.close()
savedir='textfiles/'
# url=urlroot+str(ids[0])
# print(url)

for i,filename in enumerate(ids[377:]):
    savename=str(i+377)+"_"+filename.split('.')[0]+'.txt'
    print(savename)
    getAsave(urlroot,filename,savedir,savename)





