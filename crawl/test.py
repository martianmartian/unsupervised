import re
root='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/'
f=open(root+'novel.txt','rb')

one=''
for l in f.readlines():
    one+=l.decode()

one = re.findall(r'[\u4e00-\u9fff]+',one)
one = ''.join(one)
print(one)