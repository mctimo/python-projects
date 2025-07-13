import ctypes

class Massive():
    def __init__(self):
        self.lenght = 0
        self.cap = 10
        self.massive = (ctypes.c_int * self.cap)()

    def resizing(self):
        self.cap *= 2
        new_massive = (ctypes.c_int * self.cap)()
        for i in range(self.lenght):
            new_massive[i] = self.massive[i]

        self.massive = new_massive

    def append(self, x):
        if self.lenght < self.cap:
            self.massive[self.lenght] = x
            self.lenght += 1
        if self.lenght == self.cap:
            self.resizing()

    def insert(self, index, x):
            if index >= self.lenght:
                self.append(x)
                return

            if self.lenght == self.cap:
                self.resizing()

            for i in range(self.lenght, index, -1):
                self.massive[i] = self.massive[i - 1]

            self.massive[index] = x
            self.lenght += 1

    def __iter__(self):
        for i in range(self.lenght):
            yield self.massive[i]

    def __getitem__(self, index):
        return self.massive[index]

    def __len__(self):
        return  self.lenght

    def __str__(self):
        string = '['
        for i in range(self.lenght):
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


# ДЗ: реализовать все оставшиеся методы массива:
# __add__ - done
# __class__ - skip
# __class_getitem__ - skip
# __contains__ - ?
# __delattr__
# __delitem__
# __dir__
# __doc__
# __eq__
# __format__
# __ge__
# __getattribute__
# __getitem__ - done
# __getstate__
# __gt__
# __hash__
# __iadd__ - done
# __imul__ - done
# __init__ - done
# __init_subclass__ - skip
# __iter__ - done
# __le__
# __len__ - done
# __lt__
# __mul__ - done
# __ne__
# __new__
# __reduce__
# __reduce_ex__
# __repr__
# __reversed__
# __rmul__
# __setattr__
# __setitem__
# __sizeof__
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

