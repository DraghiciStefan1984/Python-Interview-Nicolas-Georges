# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:39:30 2018

@author: Stefan Draghici
"""

def fizzbuzz(number):
    if number%3==0:
        return 'fizz'
    else:
        return 'buzz'

import unittest

class Test(unittest.TestCase):
    def test_func(self):
        self.assertEqual('fizz', fizzbuzz(3))
        self.assertEqual('fizz', fizzbuzz(33))
        self.assertEqual('buzz', fizzbuzz(32))
        self.assertEqual('fizz', fizzbuzz(15))
        self.assertEqual('buzz', fizzbuzz(5))
        
t=Test()
t.test_func()