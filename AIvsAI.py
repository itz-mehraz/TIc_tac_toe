import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.create_board()
        self.status_label = tk.Label(self.root, text="AI X's turn", font=('Arial', 14), bg='white')
        self.status_label.grid(row=3, columnspan=3)
        self.ai_players = {"X": self.ai_move, "O": self.ai_move}

    def create_board(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Arial', 30), width=4, height=2,
                                                command=lambda i=i, j=j: self.on_button_click(i, j), bg='pink')
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == "" and not self.check_winner() and not self.check_draw():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        if self.current_player in self.ai_players:
            self.ai_players[self.current_player]()
        else:
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                self.show_result(f"AI {self.current_player} wins!")
            elif self.check_draw():
                self.show_result("It's a draw!")
            else:
                self.switch_player()

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def show_result(self, message):
        print(message)
        messagebox.showinfo("Game Over", message)
        self.root.destroy()  # Close the main window when the game is over

if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
