#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  Hagay Onn
# Date:    15 April 2017
# Contact: hagayo@gmail.com
# Summary: Stack that supports pushing/popping and getting last object and size in O(1)

__author__ = 'Hagay Onn'
__version__ = '1.0'


class Stack(object):

    def __init__(self):
        self._items_counter = 0    # number of items in stack, enables get_size in o(1)
        self._stack_list = []      # list storing the stack items sequentially

    def is_empty(self):
        """returns True if stack is empty"""
        if (self._stack_list == []) or (self._items_counter == 0):
            # only one condition is really needed above
            return True
        return False

    def get_size(self):
        """returns the stack's size in o(1)"""
        # return len(self._stack_list) i.e. the standard way might be not in o(1)
        return self._items_counter

    def push(self, item):
        """push/put new object into the stack"""
        self._stack_list.insert(0, item)
        self._items_counter += 1
        return

    def pop(self):
        """gets the last object pushed to stack and remove it from stack"""
        if self.is_empty():
            return None
        self._items_counter -= 1
        return self._stack_list.pop(0)

    def get_last(self):
        """gets last object pushed to stack, without popping"""
        if self.is_empty():
            # if required to return last obj pushed, even if the stack is empty
            # another class member should be initialized when popping the last item from the stack
            return None
        return self._stack_list[0]

    # Nice to have for debugging, etc.
    def __str__(self):
        """returns a human friendly string representation of the stack"""
        # __class__.__name__ is used for inherited classes' name
        print_str = self.__class__.__name__ + ": Size={0}".format(str(self._items_counter))
        print_str += ", Last={0}".format(str(self.get_last()))
        print_str += ", Items=[ "
        for index in range(0, self._items_counter):
            print_str += str(self._stack_list[index]) + " "
        print_str += "]"
        return print_str

    def print(self, title):
        """prints the stack in a human friendly format with title"""
        print(title, self.__str__(), sep=": ")

# playing with the Stack functionality in terminal
if __name__ == '__main__':
    testStack = Stack()
    popped = None
    testStack.print("INIT")
    testStack.push(3)
    testStack.push(7)
    testStack.push(12)
    testStack.print("After push 1")
    testStack.pop()
    testStack.print("After pop 1 ")
    testStack.push(9)
    testStack.push(5)
    testStack.push(8)
    testStack.push(2)
    testStack.print("After push 2")
    popped = testStack.pop()
    print("Popped out 2: " + str(popped))
    testStack.print("After pop 2 ")
    popped = testStack.pop()
    print("Popped out 3: " + str(popped))
    testStack.print("After pop 3 ")
    testStack.push(5)
    testStack.push(4)
    testStack.push(6)
    testStack.pop()
    testStack.pop()
    testStack.pop()
    popped = testStack.pop()
    print("Popped out 4: " + str(popped))
    testStack.print("After pop 4 ")
    pass
