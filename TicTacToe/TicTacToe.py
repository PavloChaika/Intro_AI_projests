import random
import time
import turtle
import math
from Players import HumanPlayer, Computer


class TicTacToeGame:
    def __init__(self, mode = 1, size=600):
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
        if mode == 3:
            self.turn = random.choice(['x', 'o'])
        else:
            self.turn = None
        if mode == 1:
            self.allow_next = 'N'
        if mode == 2:
            self.allow_next = 'Y'

    def set_pen(self):
        self.xo.color(self.color_pen)
        self.xo.pensize(7)
        self.xo.speed(0)
        self.xo.hideturtle()

    def set_window(self):
        self.window.setup(self.size, self.size)
        self.window.title("Хрестики нулики")
        self.window.bgcolor(self.color_window)

    def draw_net(self):
        for a in range(1, self.matrix):
            self.xo.penup()
            self.xo.goto(self.X + a * self.Tab, self.Y)
            self.xo.pendown()
            self.xo.goto(self.X + a * self.Tab, -self.Y)

            self.xo.penup()
            self.xo.goto(self.X, self.Y - a * self.Tab)
            self.xo.pendown()
            self.xo.goto(-self.X, self.Y - a * self.Tab)

    def click(self, x, y):
        row = math.floor((-y + self.size/2)/ self.Tab)
        col = math.floor((x + self.size/2)/ self.Tab)

        if self.table[row][col] is not None:
            return "Try again"
        else:
            self.human_click = 1
            self.update_table(row, col)
            self.allow_next = 'Y'

    def count_none_elements(self):
        count = 0
        for row in self.table:
            count += row.count(None)
        return count

    def update_table(self, row, col):

        col_middle = (col * self.Tab + self.Tab / 2) - self.size / 2
        row_middle = (-row * self.Tab - self.Tab / 2) + self.size / 2
        self.xo.penup()
        self.xo.goto(col_middle - self.Tab / 8, row_middle - self.Tab / 8)

        self.xo.write(self.turn, font=('Arial', int(self.Tab / 4)))

        # add to the table

        self.table[row][col] = self.turn

        if self.mode == 3:
            if self.turn == 'o':
                self.turn = 'x'
            else:
                self.turn = 'o'

        game.final_screen()

    def final_screen(self):
        if self.check() is not None:
            time.sleep(1)
            self.xo.penup()
            self.xo.goto(-150, 0)
            self.xo.clear()
            self.xo.write("Виграли " + self.check(), font=("Arial", 50))


    def check(self):
        # Check rows
        for row in self.table:
            if all(cell == 'o' for cell in row): return 'o'
            if all(cell == 'x' for cell in row): return 'x'
        # Check columns
        for col in range(self.matrix):
            if all(row[col] == 'o' for row in self.table): return 'o'
            if all(row[col] == 'x' for row in self.table): return 'x'

        # Check main diagonal
        if all(self.table[i][i] == 'o' for i in range(self.matrix)): return 'o'
        if all(self.table[i][i] == 'x' for i in range(self.matrix)): return 'x'

        # Check anti-diagonal
        if all(self.table[i][self.matrix - 1 - i] == 'o' for i in range(self.matrix)): return 'o'
        if all(self.table[i][self.matrix - 1 - i] == 'x' for i in range(self.matrix)): return 'x'

        if sum(None in sublist for sublist in self.table) == 0:
            return 'ніхто'


print("Choose the mode: 1 - Human-Computer, 2 - Computer-Human, 3 - Human-Human")
mode = int(input("Enter number 1-3: "))

if mode in [1, 2, 3]:
    game = TicTacToeGame(mode, 600)
    game.set_pen()
    game.set_window()
    game.draw_net()

    if mode == 1 or mode == 2:
        player1 = HumanPlayer('x')
        player2 = Computer('o')

        while game.check() is None:
            player1.pass_move(game)
            if game.check() is not None: break
            player2.pass_move(game)

    if mode == 3:
        game.window.onclick(game.click)
        game.window.listen()

    game.window.mainloop()
else:
    print("Wrong number")