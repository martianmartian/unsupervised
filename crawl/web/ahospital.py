import urllib.parse



def url_list():
    root='http://www.a-hospital.com/w/'
    f=open('web/ahospital.html','rb')
    l=[root+urllib.parse.quote_plus(i.decode().strip()) for i in f.readlines()]
    return l[:1]

