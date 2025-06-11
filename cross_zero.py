x = [['_', '_', '_'],
     ['_', '_','_'],
     ['_', '_', '_']]

x2 = [['x', '0', 'x'],
     ['0', '0','x'],
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
    if (x[0][0] != '_' and x[0][0] == x[1][1] == x[2][2]) or (x[0][2] != '_' and x[0][2] == x[1][1] == x[2][0]):
        return x[0][0]
    return False

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
    if x[row][colum] == '_':
        x[row][colum] = value
        return x
    else:
        print('Value already busy')
        return

def next_step(x: list[list[str]], who_next: str) -> list:
    next_steps_list = []
    for i in range(len(x)):
        for j in range (len(x[i])):
            if x[i][j] == '_':
                result = copy_table(x)
                result[i][j] = who_next
                next_steps_list.append(result)
    return next_steps_list

def changer(who_next: str) -> str:
    if who_next == 'x':
        return '0'
    else:
        return 'x'

def count_steps(x: list, who_next: str) -> int:
    if not is_winner(x):
        next_steps_list = next_step(x, who_next)
        if len(next_steps_list) > 0:
            counter = 1
            for i in next_steps_list:
                counter += count_steps(i, changer(who_next))
            return counter
        return 1
    else:
        return 1

def print_next_steps_list(l: list):
    for i in l:
        print_row(i)


def start_game(x: [[str]] ) -> str or None:
    print("Hello!")
    user_input = input("Start Game?\n")
    who_next = 'x'
    if user_input == "yes" or "YES" or "Yes":
        while not is_winner(x):
            print_row(x)
            if who_next == 'x':
                x_input = input("Input cross position:\n")
                set_user_value(x, int(x_input), 'x')
                who_next = 'y'
            else:
                zero_input = input("Input zero position\n")
                set_user_value(x, int(zero_input), '0')
                who_next = 'x'
        print(f"{is_winner(x)} is WINNER!")
    else:
        print("OK! Good buy")

#start_game(x)
print(count_steps(x2, 'x'))
# алгоритм минимакс 
# библиотека tkinter