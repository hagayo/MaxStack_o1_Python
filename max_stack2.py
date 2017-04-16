#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Hagay Onn
# Date:    15 April 2017
# Contact: hagayo@gmail.com
# Summary: Stack class that supports pushing/popping objects as well as getting last/max object in O(1)

from stack import Stack

__author__ = 'Hagay Onn'
__version__ = '1.0'


class MaxStack2(Stack):

    def __init__(self):
        super(MaxStack2, self).__init__()

    def push(self, item):
        """push/put new object into the stack"""
        new_max = item
        if (not self.is_empty()) and (self.get_max() > item):
            new_max = self.get_max()
        super(MaxStack2, self).push((item, new_max))
        return

    def pop(self):
        """gets the last object pushed to stack and removes it from stack"""
        if self.is_empty():
            return None
        return super(MaxStack2, self).pop()[0]

    def get_last(self):
        """gets last object pushed to stack, without popping"""
        if self.is_empty():
            return None
        return super(MaxStack2, self).get_last()[0]

    def get_max(self):
        """gets the maximal object in the stack currently, without popping"""
        if self.is_empty():
            return None
        return super(MaxStack2, self).get_last()[1]

    # Nice to have for debugging, etc.
    def __str__(self):
        """returns a human friendly representation of the stack"""
        print_str = super(MaxStack2, self).__str__()
        print_str += ", Max={0}".format(str(self.get_max()))
        return print_str

    def print(self):
        """prints the stack in a human friendly format"""
        print(self.__str__())

# for playing with the MaxStack2 functionality in the terminal
if __name__ == '__main__':
    testStack = MaxStack2()
    popped = None
    testStack.print()
    testStack.push(4)
    testStack.push(7)
    testStack.push(5)
    testStack.print()
    testStack.push(3)
    testStack.push(7)
    testStack.print()
    testStack.push(8)
    testStack.push(1)
    testStack.push(2)
    testStack.print()
    testStack.push(123)
    testStack.print()
    popped = testStack.pop()
    testStack.print()
    print(" TestStack 5: Last:{0}, MAX:{1} Popped:{2}".format(str(testStack.get_last()),
                                                              str(testStack.get_max()), popped))
    popped = testStack.pop()
    print(" TestStack 6: Last:{0}, MAX:{1} Popped:{2}".format(str(testStack.get_last()),
                                                              str(testStack.get_max()), popped))
    popped = testStack.pop()
    print(" TestStack 7: Last:{0}, MAX:{1} Popped:{2}".format(str(testStack.get_last()),
                                                              str(testStack.get_max()), popped))
    popped = testStack.pop()
    print(" TestStack 8: Last:{0}, MAX:{1} Popped:{2}".format(str(testStack.get_last()),
                                                              str(testStack.get_max()), popped))
    popped = testStack.pop()
    print(" TestStack 9: Last:{0}, MAX:{1} Popped:{2}".format(str(testStack.get_last()),
                                                              str(testStack.get_max()), popped))
    testStack.print()
    pass
