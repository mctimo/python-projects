from random import randint
from tkinter import *
from circlular_buffer import RingBuffer

# CONST
WINDOW_X = 500
WINDOW_Y = 500
BACKGROUND_COLOR = 'black'
SPACE_SIZE = 25

# main logic
direction = "right" # дефолтное направление змейки

snake_tail_x = RingBuffer(cap=1000)
snake_tail_y = RingBuffer(cap=1000)


def change_direction(event):
    global direction
    key = event.keysym.lower()  # чтобы работало и с заглавными, и с маленькими

    if key in ["up", "w"] and direction != "down":
        direction = "up"
    elif key in ["down", "s"] and direction != "up":
        direction = "down"
    elif key in ["left", "a"] and direction != "right":
        direction = "left"
    elif key in ["right", "d"] and direction != "left":
        direction = "right"


def start_game():
    global snake_x, snake_y, apple_x, apple_y, snake_tail, score
    snake_x, snake_y = 0, 0
    apple_x = randint(0, (WINDOW_X - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
    apple_y = randint(0, (WINDOW_Y - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
    next_turn()


def next_turn():
    global snake_x, snake_y, snake_tail, apple_x, apple_y, score

    canvas.delete("all")

    # создаем яблоко
    canvas.create_rectangle(apple_x, apple_y, apple_x + SPACE_SIZE, apple_y + SPACE_SIZE, fill="red")

    # на основе direction делаем шаг
    if direction == "up":
        snake_y -= SPACE_SIZE
    elif direction == "down":
        snake_y += SPACE_SIZE
    elif direction == "left":
        snake_x -= SPACE_SIZE
    elif direction == "right":
        snake_x += SPACE_SIZE

    if snake_y >= WINDOW_Y or snake_x >= WINDOW_X:
        print("Game Over!")
        exit()
    if snake_y <= -1 or snake_x <= -1:
        print("Game Over!")
        exit()
    if (snake_x, snake_y) in zip(snake_tail_x, snake_tail_y):
        print("Game Over!")
        exit()

    snake_tail_x.append(snake_x)
    snake_tail_y.append(snake_y)

    for x, y in zip(snake_tail_x, snake_tail_y):
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill="white")

    if (apple_x, apple_y) == (snake_x, snake_y):
        score += 1
        label_score.config(text=f"Score: {score}")
        while True:
            apple_x = randint(0, (WINDOW_X - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
            apple_y = randint(0, (WINDOW_Y - SPACE_SIZE) // SPACE_SIZE) * SPACE_SIZE
            if (apple_x, apple_y) not in zip(snake_tail_x, snake_tail_y):
                break
    else:
        snake_tail_x.read()
        snake_tail_y.read()
    window.after(100, next_turn)


window = Tk()     # создаем корневой объект - окно
window.title("Snake")     # устанавливаем заголовок окна

window.geometry("1200x800")    # устанавливаем размеры окнаs
window.resizable(False, False)


label = Label(text="Snake Game") # создаем текстовую метку

score = 0
label_score = Label(window, text=f"Score: {score}", font=("Arial", 40))
label_score.pack()

canvas = Canvas(window, height=WINDOW_Y, width=WINDOW_X, background=BACKGROUND_COLOR)
canvas.pack()

window.bind("<KeyPress>", change_direction)  # считываю с клавы направление
start_game()

window.mainloop()
