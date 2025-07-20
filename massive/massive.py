import ctypes

class Massive():
    def __init__(self):
        self.length = 0
        self.cap = 10
        self.massive = (ctypes.c_int * self.cap)()

    def resizing(self):
        self.cap *= 2
        new_massive = (ctypes.c_int * self.cap)()
        for i in range(self.length):
            new_massive[i] = self.massive[i]

        self.massive = new_massive

    def append(self, x):
        if self.length < self.cap:
            self.massive[self.length] = x
            self.length += 1
        if self.length == self.cap:
            self.resizing()

    def insert(self, index, x):
            if index >= self.length:
                self.append(x)
                return

            if self.length == self.cap:
                self.resizing()

            for i in range(self.length, index, -1):
                self.massive[i] = self.massive[i - 1]

            self.massive[index] = x
            self.length += 1

    def __iter__(self):
        for i in range(self.length):
            yield self.massive[i]

    def __getitem__(self, index):
        return self.massive[index]

    def __len__(self):
        return  self.length

    def __str__(self):
        string = '['
        for i in range(self.length):
            if i == 0:
                string += f'{str(self[i])}'
            else:
                string += f', {str(self[i])}'
        string += ']'
        return string

    def __add__(self, other):
        new_mass = Massive()
        for i in self:
            new_mass.append(i)
        for i in other:
            new_mass.append(i)
        return new_mass
    
    def __iadd__(self, other):
        for i in other:
            self.append(i)
        return self

    def __mul__(self, num):
        new_mass = Massive()
        for i in range(num):
            new_mass += self
        return new_mass

    def __imul__(self, num):
        new_mass = []
        for i in range(num):
            new_mass += self
        return new_mass

    def __contains__(self, item):
        for i in self:
            if item == i:
                return True
        return False

    def __delitem__(self, index):
        new_mass = (ctypes.c_int * self.cap)()

        if index > self.length-1:
            print('Out of range')
            return

        for i in range(self.length):
            if i == index:
                continue
            if i < index:
                new_mass[i] = self.massive[i]
            else:
                new_mass[i-1] = self.massive[i]

        self.length -= 1

        self.massive = new_mass

    def __le__(self, other):
        return self.length <= len(other)

    def __reversed__(self):
        for i in range(self.length - 1, -1, -1):
            yield self.massive[i]

    def __rmul__(self, other):
        return self * other


m = Massive()

m.append(1)
m.append(2)
m.append(3)


print(m * 3)

# ДЗ: реализовать все оставшиеся методы массива:
# __add__ - done
# __class__ - skip
# __class_getitem__ - skip
# __contains__ - done
# __delattr__ - skip
# __delitem__ - done
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __getitem__ - done
# __getstate__
# __gt__
# __hash__ - skip
# __iadd__ - done
# __imul__ - done
# __init__ - done
# __init_subclass__ - skip
# __iter__ - done
# __le__ - done
# __len__ - done
# __lt__
# __mul__ - done
# __ne__
# __new__
# __reduce__ - skip
# __reduce_ex__ - skip
# __repr__ - we have str so skip
# __reversed__ - done
# __rmul__
# __setattr__
# __setitem__
# __sizeof__ - skip
# __str__ - done
# __subclasshook__
# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort

