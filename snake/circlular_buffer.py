import ctypes

class RingBuffer():
    def __init__(self, cap):
        self.cap = cap # capacity
        self.count = 0 # counter of data in buffer
        self.head = 0 # write position
        self.tail = 0 # read position

        self.buf = (ctypes.c_int * self.cap)()

    def append(self, item):
        if self.count == self.cap:
            raise OverflowError("Buffer overflow")
        self.buf[self.head] = item
        self.head = (self.head + 1) % self.cap
        self.count += 1

    def read(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        item = self.buf[self.tail]
        self.tail = (self.tail +1) % self.cap
        self.count -= 1
        return item

    def __str__(self):
        string = '['
        for index, item in enumerate(self):
            if index == 0:
                string += f'{item}'
            else:
                string += f', {item}'
        string += ']'
        return string

    def __iter__(self):
        index = self.tail
        for _ in range(self.count):
            yield self.buf[index]
            index = (index + 1) % self.cap



