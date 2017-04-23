
# import os

# # root='/Users/martian2049/Desktop/unsupervised/crawl/2txt/名侦探柯南/'
# # root='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/dict_1.txt'
# string=''
# for _,_,files in os.walk(root):
#     for file in files:
#         if file.endswith('.txt'):
#             f=open(root+file,'rb')
#             print(file)
#             for i in f.readlines():
#                 try:
#                     string+=i.decode("gbk")
#                 except ValueError:
#                     continue
#             f.close()



# # out='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/kn.txt'
# outf=open(root,'w')
# outf.write(string)
# outf.close()

