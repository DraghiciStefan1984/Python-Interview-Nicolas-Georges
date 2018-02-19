#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:35:18 2018

@author: user
"""

# TDD requires the developer to write the test first and then the implementation
import unittest

def function(number):
    if number<0:
        return 'negative'
    elif number==0:
        return 'zero'
    else:
        return 'positive'

class UnitTest(unittest.TestCase):
    def test_number_less_than_zero(self):
        result=function(-5)
        expected='negative'
        self.assertEqual(expected, result)
        self.assertEqual(expected, function(-1))
        self.assertEqual(expected, function(-100))
        
    def test_number_otherwise(self):
        self.assertEqual('positive', function(1))
        self.assertEqual('zero', function(0))
        
test=UnitTest()
test.test_number_less_than_zero()
test.test_number_otherwise()