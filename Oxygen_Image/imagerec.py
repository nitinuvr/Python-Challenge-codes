# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:01:47 2019

@author: User
"""

if __name__=="__main__":
    import imageio
    import matplotlib.pyplot as plt
    import sys
    import numpy
    numpy.set_printoptions(threshold=sys.maxsize)
    
    
    pic = imageio.imread("oxygen.png")
    
    grvalstr= str(pic[50,:608, 0])
    grvalstr = grvalstr[1:-1]
    grvallist = grvalstr.split()
    for char in grvallist:
        char = chr(int(char))
        print(char, end = '')
    print(grvallist)
    