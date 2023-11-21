import random
import time
import turtle
import math
from Players import HumanPlayer, Computer

# Class definition for the TicTacToeGame
class TicTacToeGame:
    def __init__(self, mode=1, size=600):
        # Initialize the game parameters
        self.matrix = 3
        self.size = size
        self.X = -size / 2
        self.Y = size / 2
        self.color_pen = "white"
        self.color_window = "black"
        self.table = [[None] * self.matrix for _ in range(self.matrix)]
        self.Tab = int(size / self.matrix)
        self.xo = turtle.Turtle()
        self.window = turtle.Screen()
        self.mode = mode

        # Choose the starting player randomly in mode 3, otherwise, set to None
        if mode == 3:
            self.turn = random.choice(['x', 'o'])
        else:
            self.turn = None

        # Set initial state based on the chosen mode
        if mode == 1:
            self.allow_next = 'N'
        if mode == 2:
            self.allow_next = 'Y'

    # Method to configure the turtle pen
    def set_pen(self):
        self.xo.color(self.color_pen)
        self.xo.pensize(7)
        self.xo.speed(0)
        self.xo.hideturtle()

    # Method to configure the turtle window
    def set_window(self):
        self.window.setup(self.size, self.size)
        self.window.title("Tic Tac Toe")
        self.window.bgcolor(self.color_window)

    # Method to draw the tic-tac-toe grid
    def draw_net(self):
        for a in range(1, self.matrix):
            # Draw vertical lines
            self.xo.penup()
            self.xo.goto(self.X + a * self.Tab, self.Y)
            self.xo.pendown()
            self.xo.goto(self.X + a * self.Tab, -self.Y)

            # Draw horizontal lines
            self.xo.penup()
            self.xo.goto(self.X, self.Y - a * self.Tab)
            self.xo.pendown()
            self.xo.goto(-self.X, self.Y - a * self.Tab)

    # Method to handle player click in Human-Human mode
    def click(self, x, y):
        row = math.floor((-y + self.size / 2) / self.Tab)
        col = math.floor((x + self.size / 2) / self.Tab)

        if self.table[row][col] is not None:
            return "Try again"
        else:
            self.human_click = 1
            self.update_table(row, col)
            self.allow_next = 'Y'

    # Method to count the number of empty elements in the game table
    def count_none_elements(self):
        count = 0
        for row in self.table:
            count += row.count(None)
        return count

    # Method to update the game table after a move
    def update_table(self, row, col):
        col_middle = (col * self.Tab + self.Tab / 2) - self.size / 2
        row_middle = (-row * self.Tab - self.Tab / 2) + self.size / 2
        self.xo.penup()
        self.xo.goto(col_middle - self.Tab / 8, row_middle - self.Tab / 8)

        # Write the current player's symbol on the board
        self.xo.write(self.turn, font=('Arial', int(self.Tab / 4)))

        # Update the game table
        self.table[row][col] = self.turn

        # Toggle player turn in mode 3
        if self.mode == 3:
            if self.turn == 'o':
                self.turn = 'x'
            else:
                self.turn = 'o'

        # Check for a winner and display the final screen
        self.final_screen()

    # Method to display the winner on the final screen
    def final_screen(self):
        if self.check() is not None:
            time.sleep(1)
            self.xo.penup()
            self.xo.goto(-150, 0)
            self.xo.clear()
            self.xo.write("Winner: " + self.check(), font=("Arial", 50))

    # Method to check for a winner in the game
    def check(self):
        # Check rows
        for row in self.table:
            if all(cell == 'o' for cell in row):
                return 'o'
            if all(cell == 'x' for cell in row):
                return 'x'

        # Check columns
        for col in range(self.matrix):
            if all(row[col] == 'o' for row in self.table):
                return 'o'
            if all(row[col] == 'x' for row in self.table):
                return 'x'

        # Check main diagonal
        if all(self.table[i][i] == 'o' for i in range(self.matrix)):
            return 'o'
        if all(self.table[i][i] == 'x' for i in range(self.matrix)):
            return 'x'

        # Check anti-diagonal
        if all(self.table[i][self.matrix - 1 - i] == 'o' for i in range(self.matrix)):
            return 'o'
        if all(self.table[i][self.matrix - 1 - i] == 'x' for i in range(self.matrix)):
            return 'x'

        # Check for a draw
        if self.count_none_elements() == 0:
            return 'ніхто'

# Main part of the script
print("Choose the mode: 1 - Human-Computer, 2 - Computer-Human, 3 - Human-Human")
mode = int(input("Enter number 1-3: "))

# Validate the chosen mode and initiate the game
if mode in [1, 2, 3]:
    game = TicTacToeGame(mode, 600)
    game.set_pen()
    game.set_window()
    game.draw_net()

    # Initialize players based on the chosen mode
    if mode == 1 or mode == 2:
        player1 = HumanPlayer('x')
        player2 = Computer('o')

        # Main game loop
        while game.check() is None:
            player1.pass_move(game)
            if game.check() is not None:
                break
            player2.pass_move(game)

    # Handle Human-Human mode
    if mode == 3:
        game.window.onclick(game.click)
        game.window.listen()

    # Start the game
    game.window.mainloop()
else:
    print("Wrong number")
