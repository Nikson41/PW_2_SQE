import tkinter as tk
from tkinter import messagebox


    # Розробка гри "Хрестики-нулики"
    # З помилками

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Хрестики-нулики")

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.label = tk.Label(root, text="Хід: X", font=("Arial", 16))
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        self.create_board()

        self.reset_button = tk.Button(root, text="Нова гра", font=("Arial", 12), command=self.reset_game)


        # UI/UX Помилка №2: Кнопка "Нова гра" розташована в незручному місці


        # self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)

        self.reset_button.grid(row=2, column=1)

    def create_board(self):
        for row in range(3):
            for col in range(3):
                # button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                #                    command=lambda r=row, c=col: self.make_move(r, c))

                # UI/UX Помилка №3: Різний розмір кнопок (поганий дизайн)


                button = tk.Button(self.root, text="", font=("Arial", 24), width=3 + row, height=1 + col,
                                   command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row+1, column=col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        # Функціональна помилка №1: Дозволяє перезаписувати вже зроблений хід, що порушує правила гри


        # if self.buttons[row][col]["text"] != "":
        #     return

        self.buttons[row][col]["text"] = self.current_player

        if self.check_winner():
            messagebox.showinfo("Гра завершена", f"Переміг: {self.current_player}")

            # Функціональна помилка №2: Гра не зупиняється після перемоги

            # self.disable_buttons()
            return

        if self.check_draw():
            messagebox.showinfo("Гра завершена", "Нічия!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        # UI/UX Помилка №1: Не оновлюється інформація про поточного гравця після ходу

        # self.label.config(text=f"Хід: {self.current_player}")

    def check_winner(self):
        # Перевірка рядків
        for row in self.buttons:

            # if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":

            # Функціональна помилка №3: Визнає переможцем навіть при порожніх клітинках, що є некоректним

            if row[0]["text"] == row[1]["text"] == row[2]["text"]:
                return True

        # Перевірка колонок
        for col in range(3):
            if self.buttons[0][col]["text"] == self.buttons[1][col]["text"] == self.buttons[2][col]["text"] != "":
                return True

        # Діагоналі
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True

        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button["text"] == "":
                    return False
        return True

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.label.config(text="Хід: X")

        for row in self.buttons:
            for button in row:
                button.config(text="", state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
    
