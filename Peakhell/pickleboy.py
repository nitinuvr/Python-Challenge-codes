# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:50:34 2019

@author: User
"""
import pickle


pickfile = open("banner.p", "rb")

b = pickle.load(pickfile)


for sentence in b:
    print("".join([x*y for x,y in sentence]))


pickfile.close()