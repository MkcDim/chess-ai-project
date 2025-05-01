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
    [None] * 8,
    [None] * 8,
    [None] * 8,
    [None] * 8,
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
        self.canvas.delete("all")  # Clear the canvas before redrawing
        # Draw the squares of the chessboard
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                x1 = col * SQUARE_SIZE
                y1 = row * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                color = WHITE if self.selected_piece == (row, col) else \
                        WHITE if (row + col) % 2 == 0 else BLACK

                # Draw the square
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
            if (row,col) in self.get_legal_moves(from_row,from_col):
                # Move the piece
                self.board[row][col] = piece
                self.board[from_row][from_col] = None
                print(f"Moved {piece} from ({from_row}, {from_col}) to ({row}, {col})")
            else:
                print("Invalid move.")
            
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

    def get_legal_moves(self, row, col):
        piece = self.board[row][col]
        if not piece:
            return []
        
        color, type_ = piece[0], piece[1]
        moves = []

        if type_ == "P":
            if row > 0 and self.board[row - 1][col] is None:
                    moves.append((row - 1, col))
            if row == 6 and self.board[row - 2][col] is None:
                    moves.append((row - 2, col))

        elif type_ == "R":
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr , col + dc
                while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                    if self.board[r][c] is None:
                        moves.append((r, c))
                    else:
                        break
                    r += dr
                    c += dc
        elif type_ == "N":
            knight_moves = [
                (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-1, -2), (-1, 2), (1, -2), (1, 2)
            ]
            for dr, dc in knight_moves:
                r = row + dr
                c = col + dc
                if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                    if self.board[r][c] is None or self.board[r][c][0] != color:
                        moves.append((r, c))
        return moves

def main():
    root = tk.Tk()
    game = ChessGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()