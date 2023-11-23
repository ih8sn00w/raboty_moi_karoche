from tkinter import *
from tkinter import ttk


root = Tk()
root.title("TIC-TAC-TOE")
root.geometry("500x550")  # Немного увеличил высоту, чтобы вместить метку сообщения

buttons = [[None for _ in range(3)] for _ in range(3)]  # 2D список для хранения кнопок

for c in range(3):
    root.columnconfigure(index=c, weight=1)
for r in range(4):  # Увеличил количество строк для метки сообщения
    root.rowconfigure(index=r, weight=1)

game_over = False


def click(row, col):
    global k, game_over
    if not game_over and buttons[row][col]["text"] == "":
        if k % 2 == 0:
            buttons[row][col]["text"] = "O"
        else:
            buttons[row][col]["text"] = "X"
        k += 1
        check_winner()


def check_winner():
    global game_over
    # Проверка строк, столбцов и диагоналей на наличие выигрышной комбинации
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            highlight_winner(buttons[i][0], buttons[i][1], buttons[i][2])
            return
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            highlight_winner(buttons[0][i], buttons[1][i], buttons[2][i])
            return
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        highlight_winner(buttons[0][0], buttons[1][1], buttons[2][2])
        return
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        highlight_winner(buttons[0][2], buttons[1][1], buttons[2][0])
        return
    # Если нет победителя и все кнопки заполнены, это ничья
    if all(button["text"] != "" for row in buttons for button in row):
        game_over = True
        message_label.config(text="It's a tie!")  # Обновление метки сообщения


def highlight_winner(*winning_buttons):
    global game_over
    winner_label = Label(root, text="Winner!", font=("Arial", 16, "bold"))
    winner_label.grid(row=3, columnspan=3)  # Размещение метки над сеткой
    for button in winning_buttons:
        button.configure(style="Winner.TButton")
    game_over = True
    message_label.config(text="Winner!")  # Отображение сообщения о победе


k = 1

style = ttk.Style()
style.configure("Winner.TButton", foreground="black")  # Определение стиля для кнопок-победителей

for r in range(3):
    for c in range(3):
        btn = ttk.Button(root, text="", command=lambda row=r, col=c: click(row, col), style="Winner.TButton")
        btn.grid(row=r, column=c, ipadx=100, ipady=100, padx=4, pady=4)
        buttons[r][c] = btn  # Хранение кнопки в 2D списке

message_label = Label(root, text="", font=("Arial", 16))
message_label.grid(row=4, columnspan=3)  # Добавление метки для сообщений

root.mainloop()
