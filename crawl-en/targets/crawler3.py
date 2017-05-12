#! /bin/sh/env python

import os, sys, logging
import requests
from bs4 import BeautifulSoup

getIPcmd = "ifconfig | awk '{match($0,/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/); ip = substr($0,RSTART,RLENGTH); print ip}' | grep . | sed -n '2p'"
currentIP = os.popen(getIPcmd).read()

header="User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36"

def fetch(url, ip=currentIP, header=header):
    logging.info("fetching ==> %s" % url)
    wget_cmd = 'wget -O - -q --no-check-certificate  --bind-address "%s" --header="%s" %s' % ( ip , header, url )
    buff = os.popen(wget_cmd).read()
    return buff if buff else None
def parse(buff, rule):
    _soup = BeautifulSoup(buff, 'lxml')
    rs = _soup.select(rule)
    return rs if rs else None
def crawler(url, rule, ip=currentIP, header=header):
    logging.info("crawlering ==> %s" % url)
    buff = fetch(url, ip, header)
    rs = parse(buff, rule)
    return rs if rs else None

