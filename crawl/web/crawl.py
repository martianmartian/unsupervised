import re
import itertools
import urllib.request



def getChinese(string):
    string=''.join(string)
    string = re.findall(r'[\u4e00-\u9fff]+',string)
    return string


def crawlurl(url):
    with urllib.request.urlopen(url) as response:
        html = response.read()
        chs = getChinese(html.decode())
        return chs
