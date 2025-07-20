import ctypes

class Queue():
    def __init__(self, cap):
        self.cap = cap
        self.length = 0
        self.massive = (ctypes.c_int * self.cap)()

    def append(self, item):
        self.massive[self.length] = item
        self.length += 1

    def delete_first(self):
        result = self.massive[0]
        for i in range(self.length):
            self.massive[i] = self.massive[i + 1]
        self.length -= 1
        return result

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
        for i in range(self.length):
            yield self.massive[i]
