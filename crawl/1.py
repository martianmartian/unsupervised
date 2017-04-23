
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
for i in range(len(base1000)):
    defcrawl=get_defcrawl(base1000[i])
    print(defcrawl)
    break