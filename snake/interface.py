from tkinter import *
# from snake import *

window = Tk()     # создаем корневой объект - окно
window.title("Snake")     # устанавливаем заголовок окна

window.geometry("1200x800")    # устанавливаем размеры окнаs
window.resizable(False, False)

WINDOW_WIDTH = "1200"
WINDOW_HEIGHT = "800"
BACKGROUND_COLOR = 'black'
SPACE_SIZE = 25

label = Label(text="Snake Game") # создаем текстовую метку

canvas = Canvas()

score = 0
label_score = Label(window, text=f"Score: {score}", font=("Arial", 40))
label_score.pack()

canvas = Canvas(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, background=BACKGROUND_COLOR)
canvas.pack()

window.mainloop()