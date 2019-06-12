# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:36:17 2019

@author: User
"""
import urllib.request
import re


url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=92821'

i = 0

c= 'True'

a = urllib.request.urlopen(url)



while i<400 and c!= 'False':
    a = urllib.request.urlopen(url)

    b = str(a.read())
    
    print(b)
    
    pattern = re.compile('and the next nothing is \d{2,5}')
    
    c = str(''.join(pattern.findall(b)))
    d = c.lstrip('and the next nothing is ')
    
    
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+d
    
    i+=1
    


