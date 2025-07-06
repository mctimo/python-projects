import ctypes

class Massive():
    def __init__(self):
        self.lenght = 0
        self.cap = 10
        self.massive = (ctypes.c_int * self.cap)()

    def append(self, x):
        if self.lenght < self.cap:
            self.massive[self.lenght] = x
            self.lenght += 1
        if self.lenght == self.cap:
            self.cap *= 2
            new_massive = (ctypes.c_int * self.cap)()
            for i in range(self.lenght):
                new_massive[i] = self.massive[i]
            new_massive[self.lenght] = x

            self.massive = new_massive

    def insert(self, index, x):
            if index >= self.lenght:
                self.append(x)
                return

            if self.lenght == self.cap:
                self.cap *= 2
                new_massive = (ctypes.c_int * self.cap)()
                for i in range(self.lenght):
                    new_massive[i] = self.massive[i]
                self.massive = new_massive

            for i in range(self.lenght, index, -1):
                self.massive[i] = self.massive[i - 1]

            self.massive[index] = x
            self.lenght += 1

    def __getitem__(self, index):
        return self.massive[index]

    def __len__(self):
        return  self.lenght

mass = Massive()
for i in range(40):
    mass.append(i)


for i in range(len(mass)):
    print(mass[i])


# add insert вставление элемента перед номером

#
# Если длина меньше капасити
# Меняем элемент на тот индекс который передаем
# Все что справа от него двигаем вправо
# Если длина равна или больше капасити
