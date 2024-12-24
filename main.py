import tkinter as tk
import time
from PIL import Image, ImageTk  # handling and displaying the queen image

BOARD_SIZE = 8
DELAY = 0.5 

class VisualizeNQueens:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Project: 8-Queens With Backtracking Algorithm")
        self.board_canvas = tk.Canvas(root, width=400, height=400)
        self.board_canvas.pack()
        self.cell_size = 400 // BOARD_SIZE
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.log_text = tk.Text(root, height=10, width=50)
        self.log_text.pack()
        self.queen_image = ImageTk.PhotoImage(Image.open("queen.png").resize(
            (self.cell_size - 20, self.cell_size - 20)
        ))
        self.draw_board()

    def draw_board(self):
        # update the board and places the queens at their current positions
        self.board_canvas.delete("all")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                color = "#E7C9B3" if (i + j) % 2 == 0 else "#763513"  
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.board_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                if self.board[i][j] == 1:
                    self.board_canvas.create_image(
                        x1 + self.cell_size // 2, y1 + self.cell_size // 2, image=self.queen_image
                    )
        self.root.update()

    def log(self, message):
        # logs
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def place_queens(self, row=0):
        # backtracking algorithm
        if row == BOARD_SIZE:
            return True
        for col in range(BOARD_SIZE):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.log(f"Placing queen at ({row}, {col})")
                self.draw_board()
                time.sleep(DELAY)
                if self.place_queens(row + 1):
                    return True
                self.board[row][col] = 0
                self.log(f"Backtracking from ({row}, {col})")
                self.draw_board()
                time.sleep(DELAY)
        return False

    def is_safe(self, row, col):
        # checks if it's safe to place a queen at (row, col)

        # check column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # check the main diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check the secondary diagonal
        for i, j in zip(range(row, -1, -1), range(col, BOARD_SIZE)):
            if self.board[i][j] == 1:
                return False

        return True


if __name__ == "__main__":
    root = tk.Tk()
    visualizer = VisualizeNQueens(root)
    visualizer.place_queens()
    root.mainloop()
