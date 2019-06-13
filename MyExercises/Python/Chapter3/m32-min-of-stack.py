import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '{}'.format(self.value)

    def __repr__(self):
        return 'Node<{}>:{}'.format(id(self), self.value)


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.mins = []

    def __str__(self):
        n, s = self.top, ''
        while n:
            s = '{}{} -> '.format(s, n)
            n = n.next
        return s if s else '<empty>'

    def push(self, value):
        if self.is_empty():
            self.top = Node(value)
            self.size += 1
            self.mins.append(value)
            return
        n = Node(value)
        n.next = self.top
        self.top = n
        self.size += 1
        if value < self.min():
            self.mins.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        n = self.top
        self.top = self.top.next
        self.size -= 1
        if n.value == self.min():
            self.mins = self.mins[:-1]
        return n.value

    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty.')
        return self.top.value

    def min(self):
        if not self.is_empty():
            return self.mins[-1]

    def is_empty(self):
        return self.size == 0

import random

class StackMin(unittest.TestCase):

    '''Test Case'''
    samples = range(440)

    def setUp(self):
        random.shuffle(self.samples)

    def test_stack(self):
        stack = Stack()
        for i in self.samples:
            stack.push(i)
        lst = []
        for _ in self.samples:
            lst.append(stack.pop())

        self.assertEqual(lst, list(reversed(self.samples)))

    def test_min(self):
        stack = Stack()
        stack.push(5)
        stack.push(6)
        stack.push(2)
        stack.push(7)
        stack.push(1)
        stack.push(3)
        lst = []
        stack.pop()
        lst.append(stack.min())
        stack.pop()
        lst.append(stack.min())
        stack.pop()
        lst.append(stack.min())
        stack.pop()
        lst.append(stack.min())
        stack.pop()
        lst.append(stack.min())
        self.assertEqual(lst, [1,2,2,5,5])


if __name__ == '__main__':
    # StackMin()
    unittest.main()
