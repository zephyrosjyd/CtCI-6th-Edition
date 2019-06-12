class FixedMultiStack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.numstacks = 3
        self.array = [0] * (self.numstacks * self.stacksize)
        self.sizes = [0] * self.numstacks

    def push(self, value, stacknum):
        if self.is_full(stacknum):
            raise RuntimeError('{} stack is full'.format(stacknum))
        cursor = self.get_last_cursor(stacknum)
        self.array[cursor + 1] = value
        self.sizes[stacknum - 1] += 1

    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise RuntimeError('{} stack is empty'.format(stacknum))
        cursor = self.get_last_cursor(stacknum)
        self.sizes[stacknum - 1] -= 1
        return self.array[cursor]

    def peek(self, stacknum):
        if self.is_empty(stacknum):
            return
        cursor = self.get_last_cursor(stacknum)
        return self.array[cursor]

    def get_last_cursor(self, stacknum):
        return self.stacksize * (stacknum - 1) + self.sizes[stacknum - 1] - 1

    def is_empty(self, stacknum):
        return self.sizes[stacknum - 1] == 0

    def is_full(self, stacknum):
        return self.sizes[stacknum - 1] == self.stacksize


def ThreeInOne():
    newstack = FixedMultiStack(2)
    print(newstack.is_empty(1), '->', newstack.array)
    newstack.push(3, 1)
    print(newstack.peek(1), '->', newstack.array)
    print(newstack.is_empty(1), '->', newstack.array)
    newstack.push(2, 1)
    print(newstack.peek(1), '->', newstack.array)
    print(newstack.pop(1), '->', newstack.array)
    print(newstack.peek(1), '->', newstack.array)
    newstack.push(3, 1)
    print(newstack.array)
    print(newstack.is_empty(3), '->', newstack.array)
    newstack.push(3, 3)
    print(newstack.peek(3), '->', newstack.array)
    print(newstack.is_empty(3), '->', newstack.array)
    newstack.push(2, 3)
    print(newstack.peek(3), '->', newstack.array)
    print(newstack.pop(3), '->', newstack.array)
    print(newstack.peek(3), '->', newstack.array)
    newstack.push(3, 3)
    print(newstack.array)

ThreeInOne()

