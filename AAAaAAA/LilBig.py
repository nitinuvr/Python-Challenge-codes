# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:47:12 2019

@author: User
"""

import re

f = open("text.txt", "r")
read_text = f.read()

f.close()

pattern = re.compile('[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]')

test = pattern.findall(read_text)

print(test)