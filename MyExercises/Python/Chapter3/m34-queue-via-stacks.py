import unittest


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.is_empty():
            value = self.data[-1]
            self.data = self.data[:-1]
            return value

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0


class MyQueue:
    def __init__(self):
        self.outlet_stack = Stack()
        self.inlet_stack = Stack()

    def add(self, value):
        self.inlet_stack.push(value)

    def remove(self):
        self._shift()
        return self.outlet_stack.pop()

    def peek(self):
        self._shift()
        return self.outlet_stack.peek()

    def _shift(self):
        if self.outlet_stack.is_empty():
            while not self.inlet_stack.is_empty():
                self.outlet_stack.push(self.inlet_stack.pop())

    def is_empty(self):
        self._shift()
        return self.outlet_stack.is_empty()


from collections import deque

class MyTestCase(unittest.TestCase):
    def test(self):
        q = MyQueue()
        qq = deque()
        for i in range(5):
            q.add(i)
            qq.append(i)

        for i in range(5, 8):
            q.remove()
            qq.popleft()

        for i in range(8, 11):
            q.add(i)
            qq.append(i)

        result = []
        while not q.is_empty():
            result.append(q.remove())

        self.assertEqual(result, list(qq))


if __name__ == '__main__':
    unittest.main()

