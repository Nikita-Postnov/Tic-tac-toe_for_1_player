import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")

        self.player = "X"
        self.computer = "O"
        self.board = [['' for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text="", width=10, height=3,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.window.mainloop()

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=self.player)

            if self.check_winner(self.player):
                messagebox.showinfo("Победа!", "Вы победили!")
                self.window.destroy()
            elif self.check_draw():
                messagebox.showinfo("Ничья!", "Ничья! Игра окончена.")
                self.window.destroy()
            else:
                self.computer_move()

    def computer_move(self):
        best_move = self.get_best_move()
        row, col = best_move
        self.board[row][col] = self.computer
        self.buttons[row][col].config(text=self.computer)

        if self.check_winner(self.computer):
            messagebox.showinfo("Поражение!", "Вы проиграли!")
            self.window.destroy()
        elif self.check_draw():
            messagebox.showinfo("Ничья!", "Ничья! Игра окончена.")
            self.window.destroy()

    def get_best_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '']
        for row, col in empty_cells:
            self.board[row][col] = self.computer
            if self.check_winner(self.computer):
                self.board[row][col] = ''
                return row, col
            self.board[row][col] = ''

        for row, col in empty_cells:
            self.board[row][col] = self.player
            if self.check_winner(self.player):
                self.board[row][col] = ''
                return row, col
            self.board[row][col] = ''

        return random.choice(empty_cells)

    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def check_draw(self):
        return all(self.board[i][j] != '' for i in range(3) for j in range(3))


if __name__ == "__main__":
    game = TicTacToe()
