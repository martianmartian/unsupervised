
# +++++++++++++++++++
# +++++ test zone +++
# +++++++++++++++++++






# # ++++++++++++++++++++++
# # +++++ command zone +++
# # ++++++++++++++++++++++
from web.crawl import crawlurl
from web.ahospital import url_list

for url in url_list():
    print(crawlurl(url))
# url='http://www.a-hospital.com/w/%E5%91%BC%E5%90%B8%E7%97%85%E5%AD%A6/%E8%83%B8%E8%85%94%E7%A7%AF%E6%B6%B2'
# chs = crawlurl(url)
# print(chs)



