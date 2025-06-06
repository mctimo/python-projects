x = [['_', '_', '_'],
     ['_', '_','_'],
     ['_', '_', '_']]

def print_row(x: [[str]] ):
    for i in x:
        for j in i:
            print(j, end="")
        print()
    print('____')



def is_full(x: [[str]] )-> bool:
    for i in x:
        for j in i:
            if j == '_':
                return False
    return True


def is_winner(x: [[str]]) -> bool:
    for i in range(len(x)):
        if x[i][0] != '_' and x[i][0] == x[i][1] == x[i][2]:
            return x[i][0]
    for i in range(len(x)):
        if x[0][i] != '_' and x[0][i] == x[1][i] == x[2][i]:
            return x[0][i]
    if x[0][0] != '_' and x[0][0] == x[1][1] == x[2][2] or x[0][2] == x[1][1] == x[2][0]:
        return x[0][0]

def copy_table(x: list[list[str]]) -> list[list[str]]:
    result = [['','',''],
              ['','',''],
              ['','','']]
    for i in range(len(x)):
        for j in range(len(x[i])):
            result[i][j] = x[i][j]
    return result

def set_user_value(x: list[list[str]], number: int, value: str) -> list[list[str]] or None:
    if not (0 <= number <= 9):
        print(f'Invalid number {number}')
        return
    if value not in ("x", "0"):
        print(f"Invalid value {value}")
        return

    row = number // 3
    colum = number % 3
    x[row][colum] = value
    return x

def next_step(x: list[list[str]], who_next: str) -> list:
    next_steps_list = []
    for i in range(len(x)):
        for j in range (len(x[i])):
            if x[i][j] == '_':
                result = copy_table(x)
                result[i][j] = who_next
                next_steps_list.append(result)
    return next_steps_list

def print_next_steps_list(l: list):
    for i in l:
        print_row(i)




set_user_value(x, 0, "0")
set_user_value(x, 3, "x")
set_user_value(x, 1, "0")
set_user_value(x, 7, "0")
l = next_step(x, who_next='x')
print_next_steps_list(l)


# Сделать интерфейс 
# Выводиться пустая доска
# Запраши


___
___
___
1
_x_
___
___
3
_x_
0__
___
5
_x_
0_x
___
...