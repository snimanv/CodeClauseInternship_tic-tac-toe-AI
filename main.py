import tkinter as tk
from tkinter import messagebox
import math

class TicTacToeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(root, text=' ', font=('Arial', 40), width=5, height=2,
                                  command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

        self.ai = 'O'
        self.player = 'X'

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ' and self.current_player == 'X':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X')
            if self.check_winner('X'):
                self.show_winner('X')
                return
            if self.is_board_full():
                self.show_draw()
                return
            self.current_player = 'O'
            self.root.after(100, self.ai_move)

    def ai_move(self):
        best_move = self.find_best_move()
        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.check_winner('O'):
                self.show_winner('O')
                return
            if self.is_board_full():
                self.show_draw()
                return
            self.current_player = 'X'

    def minimax(self, is_ai_turn):
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
        if self.check_winner('O'):
            return 1
        if self.check_winner('X'):
            return -1
        if self.is_board_full():
            return 0

        if is_ai_turn:
            best_score = -math.inf
            for (r, c) in available_moves:
                self.board[r][c] = 'O'
                score = self.minimax(False)
                self.board[r][c] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for (r, c) in available_moves:
                self.board[r][c] = 'X'
                score = self.minimax(True)
                self.board[r][c] = ' '
                best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_move = None
        best_score = -math.inf
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

        for (r, c) in available_moves:
            self.board[r][c] = 'O'
            score = self.minimax(False)
            self.board[r][c] = ' '
            if score > best_score:
                best_score = score
                best_move = (r, c)

        return best_move

    def check_winner(self, marker):
        win_combinations = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]
        return [marker, marker, marker] in win_combinations

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def show_winner(self, winner):
        for row in range(3):
            for col in range(3):
                if self.check_winner_line(winner, row, col):
                    self.buttons[row][col].config(bg='green')
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.root.quit()

    def show_draw(self):
        messagebox.showinfo("Game Over", "It's a draw!")
        self.root.quit()

    def check_winner_line(self, marker, row, col):
        return (self.board[row][0] == marker and self.board[row][1] == marker and self.board[row][2] == marker) or \
               (self.board[0][col] == marker and self.board[1][col] == marker and self.board[2][col] == marker) or \
               (self.board[0][0] == marker and self.board[1][1] == marker and self.board[2][2] == marker and row == col) or \
               (self.board[2][0] == marker and self.board[1][1] == marker and self.board[0][2] == marker and row + col == 2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()