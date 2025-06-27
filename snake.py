from curses import *
from random import randint

view = initscr()

try:
    view_y, view_x = view.getmaxyx()
    snake_y = 0
    snake_x = 0
    snake = '>'
    view.addstr(0, 0, snake)
    apple_x,apple_y = randint(0,10), randint(0,10)
    view.addstr(apple_x, apple_y, '$')
    snake_tail = []
    while True:
        input = view.getch()
        if input == 119:
            snake_y -= 1
        if input == 115:
            snake_y += 1
        if input == 97:
            snake_x -= 1
        if input == 100:
            snake_x +=1
        if (snake_y, snake_x) == (view_y , view_x):
            exit()
        if (snake_y, snake_x) in snake_tail:
            exit()
        snake_tail.append((snake_y, snake_x))
        view.erase()
        for i in snake_tail:
            view.addstr(i[0],i[1],snake)
        if (apple_y, apple_x) == (snake_y, snake_x):
            apple_y,apple_x = randint(0,10), randint(0,10)
        else:
            del snake_tail[0]
        view.addstr(apple_y, apple_x, '$')
finally:
    endwin()


# сделать выход за границы ошибка в 26 строке и добавить обработку 0-0 (слева и сверху)
# сделать ui в tkinter