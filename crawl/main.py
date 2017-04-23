

# # +++++++++++++++++++
# # +++++ test zone +++
# # +++++++++++++++++++

# # seriousness for med field is higher than novels. 
# s=0.9



# # step 1:
# #     embed
# # step 2:
# #     wash/remember
# # step 3:
# #     permanent memory
# # step 4:
# #     what else?

# # if resulting units:
#     # a,b,c,d,e,f,g, ...
#         # ?!softmax counts
#         # if y[i]>threshold
#             # use as a def word
#             # 


import re
import numpy as np

from chars import get1kdict
dict1k,dict1kem,base1000 = get1kdict()
defcrawl='''本人，己身：～己。～家。～身。～白。～满。～诩。～馁。～重（zhòng ）。～尊。～谦。～觉（jué ）。～疚。～学。～圆其说。～惭形秽。～强不息。
从，由：～从。～古以来。
当然：～然。～不待言。～生～灭。放任～流。假如：～非圣人，外宁必有内忧。又如:自戕(戕害自己;自杀);自呈(自首;认罪);自敝(自己困败);自各儿(自己);自凛(自身寒微);自引(自行引退;自杀)
自决 自若 自由 躬自 自足 自财 自扰 自鬻 空自 自拘 自爱 自定 自卑 独自 自省 自屈 自举 自奇 自古 自然假如：～非圣人，外宁必有内忧。〈介〉自己,自我;本身 [self;oneself;one’s own]
亲自 [
'''
invalid_chars=''.join([char for i,char in enumerate(defcrawl) if char not in dict1kem and char!="自"])
valid_chars=''.join([char for i,char in enumerate(defcrawl) if char in dict1kem and char!="自"])
candidate=[dict1k[char] for i,char in enumerate(valid_chars)]
dict1kem['自']+=np.array(candidate).sum(axis=0)
# print("\ndict1kem['自'][0:10]:==> ", dict1kem['自'][0:10],'\n')


kn='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/kn.txt'
f=open(kn,'rb')
fullarticle=''.join([line.decode().strip() for line in f.readlines()])
f.close()

b=fullarticle.split('自')
del fullarticle
window=1
allrelated=""
for i in range(len(b)):
    if len(b[i])>window:
        allrelated+=b[i][:window]+b[i][-window:]
    elif len(b[i])<window:
        allrelated+=b[i][:]

candi_list=[dict1k[char] for char in allrelated if char in valid_chars]
dict1kem['自']+=np.array(candi_list).sum(axis=0)


sort_index = np.argsort(dict1kem['自'])
print("[base1000[i] for i in sort_index[-50:]],:==>\n",[base1000[i] for i in sort_index[-50:]],'\n')
print("invalid_chars,:==> \n",invalid_chars,'\n')
print("valid_chars,:==> \n",valid_chars,'\n')
print("dict1kem['自']==>",dict1kem['自'])


