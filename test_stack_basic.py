#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Hagay Onn
# Date:    15 April 2017
# Contact: hagayo@gmail.com
# Summary: Tests Stack class functionality

import unittest
from stack import Stack

__author__ = 'Hagay Onn'
__version__ = '1.0'


class StackTestCase(unittest.TestCase):
    def setUp(self):
        self.testStack = Stack()

    def test_init_stack_state(self):
        self.assertEqual(self.testStack.get_size(), 0, 'incorrect get_size() on init')
        self.assertEqual(self.testStack.get_last(), None, 'incorrect get_last() on init')
        self.assertEqual(self.testStack.pop(), None, 'incorrect pop() on init')

    def test_stack_functionality(self):
        self.testStack.push(3)
        self.testStack.push(7)
        self.testStack.push(12)
        self.assertEqual(self.testStack.get_size(), 3, 'incorrect get_size() Stop-Point 1')
        self.assertEqual(self.testStack.get_last(), 12, 'incorrect get_last() Stop-Point 1')
        self.assertEqual(self.testStack.pop(), 12, 'incorrect pop() Stop-Point 1')
        self.testStack.push(9)
        self.testStack.push(5)
        self.testStack.push(8)
        self.testStack.push(2)
        self.assertEqual(self.testStack.get_size(), 6, 'incorrect get_size() Stop-Point 2')
        self.assertEqual(self.testStack.get_last(), 2, 'incorrect get_last() Stop-Point 2')
        self.assertEqual(self.testStack.pop(), 2, 'incorrect pop() Stop-Point 2')
        self.testStack.pop()    # pop 8 out
        self.assertEqual(self.testStack.get_size(), 4, 'incorrect get_size() Stop-Point 3')
        self.assertEqual(self.testStack.get_last(), 5, 'incorrect get_last() Stop-Point 3')
        self.assertEqual(self.testStack.pop(), 5, 'incorrect pop() Stop-Point 3')
        self.testStack.push(4)
        self.testStack.push(6)
        self.assertEqual(self.testStack.get_size(), 5, 'incorrect get_size() Stop-Point 4')
        self.assertEqual(self.testStack.get_last(), 6, 'incorrect get_last() Stop-Point 4')
        self.assertEqual(self.testStack.pop(), 6, 'incorrect pop() Stop-Point 4')
        self.testStack.pop()
        self.testStack.pop()
        self.testStack.pop()
        self.testStack.pop()
        self.assertEqual(self.testStack.get_size(), 0, 'incorrect get_size() Stop-Point 5')
        self.assertEqual(self.testStack.get_last(), None, 'incorrect get_last() Stop-Point 5')
        self.assertEqual(self.testStack.pop(), None, 'incorrect pop() Stop-Point 5')
        self.testStack.pop()
        self.assertEqual(self.testStack.pop(), None, 'incorrect pop() Stop-Point 6')
        self.assertEqual(self.testStack.get_last(), None, 'incorrect get_last() Stop-Point 6')
        pass

    def tearDown(self):
        self.testStack = None
