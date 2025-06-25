from tkinter import messagebox


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
    if (x[0][0] != '_' and x[0][0] == x[1][1] == x[2][2]):
        return x[0][0]
    if (x[0][2] != '_' and x[0][2] == x[1][1] == x[2][0]):
        return x[0][2]
    return None


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
        return x


def next_step(x: list[list[str]], current_player: str) -> list:
    next_steps_list = []
    for i in range(len(x)):
        for j in range (len(x[i])):
            if x[i][j] == '_':
                result = copy_table(x)
                result[i][j] = current_player
                next_steps_list.append(result)
    return next_steps_list


def changer(current_player: str) -> str:
    if current_player == 'x':
        return '0'
    else:
        return 'x'


def count_steps(x: list, current_player: str) -> int:
    if not is_winner(x):
        next_steps_list = next_step(x, current_player)
        if len(next_steps_list) > 0:
            counter = 1
            for i in next_steps_list:
                counter += count_steps(i, changer(current_player))
            return counter
        return 1
    else:
        return 1

# 0 is AI
# X is player


def value(x: list, current_player: str) -> int:
    winner = is_winner(x)

    if winner == '0':
        return 1
    elif winner == 'x':
        return -1
    elif is_full(x):
        return 0

    result = []
    list_of_steps = next_step(x ,current_player=current_player)
    for i in list_of_steps:
        result.append(value(i,current_player=changer(current_player)))

    if current_player == '0':
        return max(result)
    else:
        return min(result)


def best_step(x: [[str]]) -> [[str]]:
    values = []
    steps = []
    next_steps = next_step(x,current_player='0')
    for i in next_steps:
        steps.append(i)
        values.append(value(i,current_player='x'))

    return steps[values.index(max(values))]


# нахожу разницу в досках
def best_step_value(old_board: [[str]], new_board: [[str]]) -> int:

    for i in range(3):
        for j in range(3):
            if old_board[i][j] != new_board[i][j]:
                return i*3 +j


def print_next_steps_list(l: list):
    for i in l:
        print_row(i)


def start_game(x: [[str]] ) -> str or None:
    current_player = 'x'
    while not is_winner(x) and not is_full(x):
        print_row(x)
        if current_player == 'x':
            x_input = input("Input cross position:\n")
            set_user_value(x, int(x_input)-1, 'x')
            current_player = '0'
        else:
            step = best_step(x)
            number_of_positon = best_step_value(x, step)
            set_user_value(x, number_of_positon,'0')
            current_player = 'x'
    print_row(x)
    print(f"{is_winner(x)} is WINNER!")

