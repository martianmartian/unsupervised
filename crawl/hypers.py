import matplotlib.pyplot as plt
import numpy as np


def fr(x):
    '''when x>10, fr -> 0'''
    return 1/(1+np.exp(x-6))

def pm(x):
    '''when x>8, pm = 1 '''
    return ((1/(1+np.exp(-x+6)))>0.95)*1


if __name__ == '__main__':
    x=np.linspace(-5,15,100)
    plt.plot(x,fr(x))
    plt.plot(x,pm(x))
    plt.grid()
    plt.show()