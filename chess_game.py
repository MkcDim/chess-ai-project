import tkinter as tk

# Size of the chessboard
BOARD_SIZE = 8
# Size of each square on the chessboard
SQUARE_SIZE = 60
# Colors for the chessboard squares
WHITE = "#F0D9B5"
BLACK = "#B58863"


# Chess piece symbole 
pieces = {
    "white": {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'
    },
    "black": {
        'K': '♚', 'Q': '♛', 'R': '♜', 'B': '♝', 'N': '♞', 'P': '♟'
    }
}

# Starting positions of the pieces on the board
starting_board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]


class ChessGame:
    def __init__(self,master):
        self.master = master
        self.master.title("Chess AI Project")
        
        self.canvas = tk.Canvas(self.master, width=BOARD_SIZE * SQUARE_SIZE, height=BOARD_SIZE * SQUARE_SIZE)
        self.canvas.pack()

        self.board = starting_board  # Initialize the board with starting positions

        self.draw_board()
        
        self.canvas.bind("<Button-1>", self.handle_click)


    def draw_board(self):
        """Draws the chessboard on the canvas."""
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                color = WHITE if (row + col) % 2 == 0 else BLACK
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

                # Draw pieces if exist
                piece = self.board[row][col]
                if piece:
                    color_prefix = "white" if piece[0] == "w" else "black"
                    piece_letter = piece[1]
                    self.canvas.create_text(
                        x1 + SQUARE_SIZE // 2,
                        y1 + SQUARE_SIZE // 2,
                        text=pieces[color_prefix][piece_letter],
                        font=("Arial", 32)
                    )

    def handle_click(self, event):
        """Handles mouse clicks on the chessboard."""
        x = event.x // SQUARE_SIZE
        y = event.y // SQUARE_SIZE
        print(f"Clicked on square: ({x}, {y})")

def main():
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()