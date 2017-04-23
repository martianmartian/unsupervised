
import numpy as np
fullarticle="""回以职业笑容…「哪里，谢谢你们的支持了…」
    过去每年都是这样自的情景，新一自然都是欣然接受并笑著答礼。
    隔了好一会，女孩们才心满意足，带著兴奋的心情，漾著笑意快步离去。
    新一看著她们离开，自随手也要把那个巧克力收起来。
    「………」兰无声无息地走到新一身旁。"""
fullarticle=np.array(fullarticle)
b=fullarticle.split('自')
del fullarticle

window=4
allrelated=""
for i in range(len(b)):
    if len(b[i])>window:
        allrelated+=b[i][:window]+b[i][-window:]
    elif len(b[i])<window:
        allrelated+=b[i][:]
print(allrelated[window:-window])