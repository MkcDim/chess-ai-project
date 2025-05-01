import tkinter as tk

# Size of the chessboard
BOARD_SIZE = 8
# Size of each square on the chessboard
SQUARE_SIZE = 60
# Colors for the chessboard squares
WHITE = "#F0D9B5"
BLACK = "#B58863"
HIGHLIGHT_COLOR = "#AAF"

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

        self.board = [row[:] for row in starting_board]  # Initialize the board with starting positions
        self.selected_piece = None
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

                # Highlight the square if it is selected
                if self.selected_piece == (row, col):
                    color = HIGHLIGHT_COLOR
                else:
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
        col = event.x // SQUARE_SIZE
        row = event.y // SQUARE_SIZE
        
        if self.selected_piece:
            from_row, from_col = self.selected_piece
            piece = self.board[from_row][from_col]

            # move only if the destination valid
            if self.board[row][col] is None:
                # Move the piece
                self.board[row][col] = piece
                self.board[from_row][from_col] = None
                self.selected_piece = None
                print(f"Moved {piece} from ({from_row}, {from_col}) to ({row}, {col})")
            
            self.selected_piece = None # deselect the piece
        else:
            piece = self.board[row][col]
            # Select only white pieces
            if piece and piece[0] == "w":
                self.selected_piece = (row, col)
                print(f"Selected {piece} at ({row}, {col})")
            else:
                print("Invalid selection or no piece at clicked position.")

        self.draw_board()  # Redraw the board after the move or selection

def main():
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()