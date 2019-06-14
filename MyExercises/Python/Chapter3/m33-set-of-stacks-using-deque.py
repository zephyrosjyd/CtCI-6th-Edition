import unittest
from collections import deque 
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return '{} ->'.format(self.value)


class Stack:
    def __init__(self, capacity):
        self.cap = capacity
        self.struct = deque()

    def __str__(self):
        return ' '.join([str(x) for x in self.struct])

    def push(self, value):
        if self.full():
            raise RuntimeError('Stack is full.')
        self.struct.append(Node(value))

    def pop(self):
        if self.empty():
            raise RuntimeError('Stack is empty.')
        n = self.struct.pop()
        return n.value

    def remove(self):
        if self.empty():
            raise RuntimeError('Stack is empty.')
        n = self.struct.popleft()
        return n.value

    def empty(self):
        return len(self.struct) == 0

    def full(self):
        return len(self.struct) == self.cap


class SetOfStack:
    def __init__(self, capacity):
        self.cap = capacity
        self.stacks = []

    def __str__(self):
        return ' | '.join([str(s) for s in self.stacks])

    def push(self, value):
        if self.empty():
            self.stacks.append(Stack(self.cap))
        last = self._get_last_stack()
        if last.full():
            self.stacks.append(Stack(self.cap))
            last = self._get_last_stack()
        last.push(value)

    def pop(self):
        if self.empty():
            raise IndexError('Set of stacks is empty.')
        last = self._get_last_stack()
        value = last.pop()
        if last.empty():
            self.stacks = self.stacks[:-1]
        return value

    def pop_at(self, index):
        if self.empty() or index < 0 or index >= len(self.stacks):
            raise RuntimeError('Invalid index')
        stack = self.stacks[index]
        if stack is self._get_last_stack():
            return self.pop()
        value = stack.pop()
        for i in range(index, len(self.stacks) - 1):
            while not self.stacks[i].full():
                v = self.stacks[i + 1].remove()
                self.stacks[i].push(v)
                if self.stacks[i + 1].empty():
                    break
        last = self._get_last_stack()
        if last.empty():
            self.stacks = self.stacks[:-1]
        return value

    def _get_last_stack(self):
        return None if self.empty() else self.stacks[-1]

    def empty(self):
        return not self.stacks


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_stringify(self):
        stack = Stack(3)
        stack.struct.append(Node(0))
        stack.struct.append(Node(1))
        stack.struct.append(Node(2))
        self.assertEqual(str(stack), '0 -> 1 -> 2 ->')

        ss = SetOfStack(2)
        ss.stacks.append(stack)
        ss.stacks.append(stack)
        self.assertEqual(str(ss), '0 -> 1 -> 2 -> | 0 -> 1 -> 2 ->')

    def test_push(self):
        ss = SetOfStack(3)
        for i in range(3):
            ss.push(i)
        self.assertEqual(str(ss), '0 -> 1 -> 2 ->')

    def test_pop(self):
        ss = SetOfStack(5)
        for i in range(10):
            ss.push(i)
        # print(str(ss))
        for _ in range(10):
            ss.pop()
        self.assertEqual(str(ss), str(SetOfStack(5)))

    def test_stacks(self):
        stacks = SetOfStack(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        self.assertEqual(lst, list(reversed(range(35))))

    def test_pop_at(self):
        stacks = SetOfStack(5)
        for i in range(35):
            stacks.push(i)
        # print(str(stacks))
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        # print(str(stacks))
        # print(lst)
        self.assertEqual(lst, list(range(4, 35)))


if __name__ == '__main__':
    unittest.main()
