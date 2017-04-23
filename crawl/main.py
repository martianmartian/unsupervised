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

defcrawl='''自百度一下182*****431|手机版|我的词典用百度汉语查看更全面更权威的汉语知识，在百度汉语中查看“自”拼音zì部首自五笔THD笔顺ノ丨フ一一一生词本基本释义详细解释本人，己身：～己。～家。～身。～白。～满。～诩。～馁。～重（zhòng）。～尊。～谦。～觉（jué）。～疚。～学。～圆其说。～惭形秽。～强不息。从，由：～从。～古以来。当然：～然。～不待言。～生～灭。放任～流。假如：～非圣人，外宁必有内忧。其他信息五笔THD四角26000仓颉HBU五行火笔画数6郑码NL字结构单一结构部件拆解丿、目注音ㄗˋ统一码81EA相关组词自决自若自由躬自自足自财自扰自鬻空自自拘自爱自定自卑独自自省自屈自举自奇自古自然相关字信八力及孔字热搜字亟亦冢匙处方©2017Baidu使用百度前必读百度首页问题反馈关注微博用户QQ群：484758177'''

import numpy as np
from chars import get1kdict
dict1k,dict1kem = get1kdict()

def embed_char(char,string,char_vec,base_mat):
    candidate=[base_mat[j] for i,j in enumerate(string) if j in base_mat and j!=char]
    char_vec+=np.array(candidate).sum(axis=0)

# candidate=[dict1k[j] for i,j in enumerate(defcrawl) if j in dict1kem and j!="自"]
# dict1kem['自']+=np.array(candidate).sum(axis=0)
embed_char('自',defcrawl,dict1kem['自'],dict1k)
print("\ndict1kem['自'][0:10]:==> ", dict1kem['自'][0:10],'\n')


# import re
# kn='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/kn1.txt'
# f=open(kn,'rb')
# ffulls=''.join([line.decode().strip() for line in f.readlines()])
# f.close()
# ffulls=re.findall(r'[\u4e00-\u9fff]+[,;，。]',ffulls)
# print("ffulls[:10]:==> ", ffulls[:10],'\n')


