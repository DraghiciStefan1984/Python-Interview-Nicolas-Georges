# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:40:46 2018

@author: Stefan Draghici
"""

class MyClass(object):
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def double_nums(self, x, y):
        return self.x*2+self.y*2
    
myClass=MyClass(18, 38)
myClass.double_nums(33, 22)
