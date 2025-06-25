from tkinter import *
from tik_tac_main import *

root = Tk()     # создаем корневой объект - окно
root.title("Tik Tac Game")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
 
label = Label(text="Tik Tac Game") # создаем текстовую метку

# Создаём обёртку (контейнер) для кнопок
frame = Frame(root)
frame.pack(expand=True)  # expand=True делает так, чтобы frame занял всё пространство
frame.place(relx=0.5, rely=0.5, anchor='center')  # центрирует frame в окне

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

board2 = [['0', '_', 'x'],
         ['_', 'x', '_'],
         ['x', '_', 'x']]

buttons = []


def click_button(index, board=board):

    if board[index // 3][index % 3] != '_':
        messagebox.showinfo("Клетка занята!")
        return  # 🔒 клетка уже занята

    # ходит игрок
    set_user_value(x=board, number=index, value='x')
    buttons[index]["text"] = "X"

    if is_winner(board):
        messagebox.showinfo("Игра окончена", "Победил: X")
        return

    if is_full(board):
        messagebox.showinfo("Игра окончена","Ничья!")
        return

    # ходит ии
    best_step_board = best_step(board)
    best_step_index = best_step_value(board, best_step_board)
    set_user_value(x=board, number=best_step_index, value='0')
    buttons[best_step_index]["text"] = "0"

    if is_winner(board) or is_full(board):
        messagebox.showinfo("Игра окончена", "Победил: 0")
        return

    if is_full(board):
        messagebox.showinfo("Игра окончена","Ничья!")
        return
    

for i in range(9):
    row = i // 3    # вычисляем номер строки 
    col = i % 3     # вычисляем номер столбца
    btn = Button(frame, text=str(''), width=10, height=3, command=lambda i=i: click_button(i))
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()