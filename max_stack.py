#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Hagay Onn
# Date:    15 April 2017
# Contact: hagayo@gmail.com
# Summary: Stack class that supports pushing/popping objects as well as getting last/max object in O(1)

from stack import Stack

__author__ = 'Hagay Onn'
__version__ = '1.0'


class MaxStack(Stack):

    def __init__(self):
        super(MaxStack, self).__init__()
        self._max_list = []    # list storing the stack's max values

    def push(self, item):
        """push/put new object into the stack"""
        super(MaxStack, self).push(item)
        if (self._max_list == []) or (self._max_list[0] <= item):
            self._max_list.insert(0, item)
        return

    def pop(self):
        """gets the last object pushed to stack and remove it from stack"""
        if self.is_empty():
            return None
        if (self.get_last() == self.get_max()):
            self._max_list.pop(0)
        return super(MaxStack, self).pop()

    def get_max(self):
        """gets the maximal object in the stack currently, without popping"""
        if (self._max_list == []):  # or (self._max_list is None)
            return None
        return self._max_list[0]

    # Nice to have for debugging, etc.
    def __str__(self):
        """returns a human friendly representation of the stack"""
        print_str = super(MaxStack, self).__str__()
        print_str += ", Max={0}".format(str(self.get_max()))
        return print_str

    def print(self):
        """prints the stack in a human friendly format"""
        print(self.__str__())

# for playing with the MaxStack functionality in the terminal
if __name__ == '__main__':
    testStack = MaxStack()
    testStack.print()
    testStack.push(4)
    testStack.print()
    testStack.push(7)
    testStack.print()
    testStack.push(5)
    testStack.print()
    testStack.push(5)
    testStack.print()
    testStack.push(7)
    testStack.print()
    testStack.push(8)
    testStack.print()
    testStack.push(1)
    testStack.print()
    testStack.push(3)
    testStack.print()
    testStack.push(123)
    testStack.print()
    print(" Popped out 1: {}".format(str(testStack.pop())))
    testStack.print()
    print(" Popped out 2: {}".format(str(testStack.pop())))
    testStack.print()
    print(" Popped out 3: {}".format(str(testStack.pop())))
    testStack.print()
    print(" Popped out 4: {}".format(str(testStack.pop())))
    testStack.print()
    pass
