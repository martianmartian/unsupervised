import numpy as np

def get1kdict():
    root='/Users/martian2049/Desktop/unsupervised/crawl/data-mini/char.txt'
    f=open(root,'rb')
    chars=[i.decode().strip() for i in f.readlines()]
    f.close()

    mat1k=np.zeros((1000,1000),dtype=np.int)
    mat1k[np.arange(1000),np.arange(1000)]=1
    dict1k=dict((j,mat1k[i]) for i,j in enumerate(chars[0]))
    dict1kem=dict((j,np.zeros((1000),dtype=np.int)) for i,j in enumerate(chars[0]))

    return dict1k,dict1kem,chars[0]