
# +++++++++++++++++++
# +++++ test zone +++
# +++++++++++++++++++

# # seriousness for med field is higher than novels. 
# s=0.9


# # ++++++++++++++++++++++
# # +++++ command zone +++
# # ++++++++++++++++++++++


# 1000
#     each crawl
#         get only definition part
#         extract chinese=>string
#     embed
#         save
#     wash
#         save
# this is only the first impression. 
# another round of more generalized learning should be applied. 


import re
import numpy as np

from web.crawl import get_defcrawl
from chars import get1kdict
dict1k,dict1kem,base1000 = get1kdict()

# dict1kem=np.load('save/dict1kem.npy').item()


# # # washing:
# # kn='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/kn.txt'
# # f=open(kn,'rb')
# # fullarticle=''.join([line.decode().strip() for line in f.readlines()])
# # f.close()

# # for i in range(0,1000):
# #     base=base1000[i]
# #     print(base,i)
# #     b=fullarticle.split(base)
# #     window=4
# #     allrelated=""
# #     for j in range(len(b)):
# #         if len(b[j])>window:
# #             allrelated+=b[j][:window]+b[j][-window:]
# #         elif len(b[j])<window:
# #             allrelated+=b[j][:]

# #     f=open('data-mini/defcrawl/base1000/'+str(i)+base+'.txt','rb')
# #     defcrawl=[l.decode().strip() for l in f.readlines()][0]
# #     invalid_chars=''.join([char for i,char in enumerate(defcrawl) if char not in dict1kem and char!=base])
# #     valid_chars=''.join([char for i,char in enumerate(defcrawl) if char in dict1kem and char!=base])
# #     candi_list=[dict1k[char] for char in allrelated if char in valid_chars]
# #     if len(candi_list)!=0:
# #         # print(dict1kem[base])
# #         dict1kem[base]+=np.array(candi_list).sum(axis=0)
# #         # print(dict1kem[base])
# #         # break

# init with random number>0!!!!!!!!!!!!!!!!!!!!


def cos_sim(a,b):
    return np.dot(a,b)/(np.sqrt(np.dot(a,a))*np.sqrt(np.dot(b,b)))

# # np.save('save/dict1kem_washedup.npy',dict1kem)
dict1kem=np.load('save/dict1kem_washedup.npy').item()
# base='静'
# sort_index = np.argsort(dict1kem[base])
# print("[base1000[i] for i in sort_index[-50:]],:==>\n",[base1000[i] for i in sort_index[-50:]],'\n')
# # print("dict1kem['"+base+"']==>",dict1kem[base])
base='胜'
sort_index = np.argsort(dict1kem[base])
print("[base1000[i] for i in sort_index[-50:]],:==>\n",[base1000[i] for i in sort_index[-50:]],'\n')
# print("dict1kem['"+base+"']==>",dict1kem[base])


a='胜利对'
b='失败错'
va=np.zeros((1000,))
vb=np.zeros((1000,))
for i in range(len(a)):
    va+=dict1kem[a[i]]
    vb+=dict1kem[b[i]]
print(cos_sim(va,vb))

# for i,w in enumerate(dict1kem):
#     sim=cos_sim(dict1kem['静']+dict1kem['安'],dict1kem[w])
#     print(w,':==>',sim) if sim>0.6 else False

# epsi=0
# # epsi=0.0001
# def softmax(x):
#     return np.exp(x)/np.sum(np.exp(x))

# print(softmax(dict1kem['父']+epsi))
# a=np.dot(softmax(dict1kem['父']+epsi),softmax(dict1kem['母']+epsi))
# b=np.dot(softmax(dict1kem['男']+epsi),softmax(dict1kem['女']+epsi))
# print(a)
# print(b)
# print(a/b)

