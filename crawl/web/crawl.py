import re
import itertools
import urllib.request
import urllib.parse
from pyquery import PyQuery as pq

def getChinese(st):
    st=''.join(st)
    l = re.findall(r'[\u4e00-\u9fff]+',st)
    return ''.join(l)


def crawlurl(url,elname=None):
    chs=''
    with urllib.request.urlopen(url) as response:
        html = response.read()
        # find elname with
        if elname!=None:
            d = pq(html)
            query = d(elname)
            chs += getChinese(query.html())
        return chs

def get_defcrawl(char):
    theurl='http://dict.baidu.com/s?wd='+urllib.parse.quote_plus(char)
    chs = crawlurl(theurl,elname='.tab-content')
    return chs