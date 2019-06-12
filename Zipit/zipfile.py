# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:51:17 2019

@author: User
"""

import re
import zipfile


file_name = '90052.txt'

f = open(file_name, 'r')
arch = zipfile.ZipFile('channel.zip', 'r')

trim = 0
while trim!=None:
    
    f = open(file_name,  'r')
    readfile = f.read()
    
    comm = arch.getinfo(file_name).comment
    nobi = comm.decode('ascii')
    
    print(nobi, end = '')
    
    pattern = re.compile('Next nothing is \d{2,5}')

    found = str(''.join(pattern.findall(readfile)))


    trim = found.lstrip('Next nothing is ')


    f.close()
    
    file_name = trim+'.txt'
    

