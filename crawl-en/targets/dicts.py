import numpy as np
import re
import itertools
import urllib.request
import urllib.parse
from pyquery import PyQuery as pq

import os,sys
where=os.getcwd()
sys.path.append(where)



def get1kdict(dictpath):
    f=open(dictpath,'rb')
    w1k=[i.decode().strip() for i in f.readlines()]
    f.close()
    mat1k=np.zeros((1000,1000),dtype=np.int)
    mat1k[np.arange(1000),np.arange(1000)]=1
    vec1k=dict((j,mat1k[i]) for i,j in enumerate(w1k))
    vec1kem=dict((j,np.zeros((1000),dtype=np.int)) for i,j in enumerate(w1k))
    print('w1k[100:110]:',w1k[100:110])
    return vec1k,vec1kem,w1k

def getAsave(dicturlroot,word,savedir,scrapper):
    savetodir=savedir+word+'/'
    if not os.path.exists(savetodir):
        os.makedirs(savetodir)
    savefile=savetodir+scrapper.__name__+'.html'
    print(word,scrapper.__name__)

    url=dicturlroot+word
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    req = urllib.request.Request(url, headers = headers)
    try:
        res = urllib.request.urlopen(req)
        html=res.read().decode()
        txt = scrapper(html)
        # print(txt)
        out=open(savefile,'w')
        out.write(txt)
        out.close()
        res.close()
    except ValueError:
        print("'===== broke !! ====: ")
        print(word,' @ ',scrapper.__name__)
        print('=========')

dicts={
    'mw':'https://www.merriam-webster.com/dictionary/',
    'vocabulary':'https://www.vocabulary.com/dictionary/',
    'dictionary':'http://www.dictionary.com/browse/',
    'oxford':'https://en.oxforddictionaries.com/definition/',
    'thefree':'http://www.thefreedictionary.com/',
    'yourdic':'http://www.yourdictionary.com/',
    'cambridge':'http://dictionary.cambridge.org/dictionary/english/',
    'collins':'https://www.collinsdictionary.com/us/dictionary/english/'
}

def mw(html):
    defs = pq(html)('.card-primary-content').html()
    return defs

def vocabulary(html):
    para=pq(pq(html)('.main')[1]).html()
    defs=pq(pq(html)('.main')[2]).html()
    return para+defs

def dictionary(html):
    defs=""
    for i,each in enumerate(pq(html)('.def-set')):
        defs+=pq(each).html()
    return defs

def oxford(html):
    defs=""
    for i,each in enumerate(pq(html)('.gramb')):
        defs+=pq(each).html()
    for i,each in enumerate(pq(html)('.etymology')):
        defs+=pq(each).html()
    return defs

def thefree(html):
    defs=pq(html)('#Definition').html()
    return defs

def yourdic(html):
    defs=pq(html)('#definitions_panel').html()
    return defs

def cambridge(html):
    defs=""
    for i,each in enumerate(pq(html)('.entry-body')):
        defs+=pq(each).html()
    return defs

def collins(html):
    defs=pq(html)('.homograph-entry').html()
    return defs


# dictpath='dicts1000.txt'
# vec1k,vec1kem,w1k=get1kdict(dictpath)



savedir='dicts/'
w='place'
dicturlroot='https://www.collinsdictionary.com/us/dictionary/english/'
scrapper=collins

getAsave(dicturlroot,w,savedir,scrapper)
# for i,dicturlroot in enumerate(dicts):
#     for j,w in enumerate(w1k):
#         # url=dicturlroot+w
#         getAsave(dicturlroot,w,savedir)







