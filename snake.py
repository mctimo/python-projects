from curses import *
import random
view = initscr()
try:
    y = 0
    x = 0
    snake = '>'
    view.addstr(0, 0, snake)
    z,y = random(0,10), random(0,10)
    view.addstr(z, y, '$')
    while True:
        input = view.getch()
        if input == 119:
            y -= 1
        if input == 115:
            y += 1
        if input == 97:
            x -= 1
        if input == 100:
            x +=1
        view.erase()
        view.addstr(y,x,snake)
        if x, y == z, y:
            
finally:
    endwin()