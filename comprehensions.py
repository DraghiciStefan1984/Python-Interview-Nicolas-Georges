# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 18:30:47 2018

@author: Stefan Draghici
"""

# list
list_ex=[x**2 for x in range(50)]
print(list_ex)

# set
set_ex=(x**3 for x in range(20) if x%2==0)
for i in enumerate(set_ex):
    print(i)
    
# dict
dict_ex={x: x**4 for x in range(30)}
for i in enumerate(dict_ex):
    print(i)