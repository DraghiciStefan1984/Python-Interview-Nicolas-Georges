#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 12:04:13 2018

@author: user
"""

import unittest

# create a class that inherrits from TestCase
class MyUnitTest(unittest.TestCase):
    # the testing method must start with "test"
    def tests_that_pass(self):
        # make assertions
        self.assertTrue(True)
        self.assertTrue(1==1)
        self.assertFalse(1==8)
        
    def tests_that_fail(self):
        self.assertFalse(1==1)
        
    def test_equal(self):
        self.assertEqual(1, 2)
        self.assertEqual(1, 1)
        
myTest=MyUnitTest()
print(myTest.tests_that_pass())
print(myTest.tests_that_fail())
print(myTest.test_equal())