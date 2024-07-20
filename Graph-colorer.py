# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 20:35:42 2024

@author: rwstu
"""
import math
import networkx
def ndigit(number,index,base):
    return math.floor(number/base**index)%base
number=128
index=7
base=2
cube=[0,0,0,0,0,0]
color_code={0:'Red',1:'Green',2:'Blue'}
for i in range(0,3**6):
    cube=[color_code[ndigit(i,j,3)] for j in range(0,6)]
    print(sum([i=='Blue' for i in cube]))