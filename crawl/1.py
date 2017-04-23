
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

import re
import numpy as np

from web.crawl import get_defcrawl
from chars import get1kdict
dict1k,dict1kem,base1000 = get1kdict()
for i in range(945,len(base1000)):
    base=base1000[i]
    print(base,i)
    defcrawl=get_defcrawl(base)
    f=open('data-mini/defcrawl/'+str(i)+base+'.txt','w')
    f.write(defcrawl)
    f.close()
#     invalid_chars=''.join([char for i,char in enumerate(defcrawl) if char not in dict1kem and char!=base])
#     valid_chars=''.join([char for i,char in enumerate(defcrawl) if char in dict1kem and char!=base])
#     candidate=[dict1k[char] for i,char in enumerate(valid_chars)]
#     dict1kem[base]+=np.array(candidate).sum(axis=0)
#     # print("\ndict1kem["+base+"][0:10]:==> ", dict1kem[base][0:10],'\n')

# # save all embeddings here:
# np.save('save/dict1kem.npy',dict1kem)
# newdict1kem=np.load('save/dict1kem.npy').item()
# print(newdict1kem['我'])

