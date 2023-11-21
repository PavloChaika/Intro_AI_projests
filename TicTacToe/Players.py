import random
import time

# Player class, serves as a base class for HumanPlayer and Computer classes
class Player():
    def __init__(self, turn):
        self.turn = turn

    def pass_move(self, game):
        pass

# HumanPlayer class, inherits from Player
class HumanPlayer(Player):
    def __init__(self, turn):
        super().__init__(turn)

    def pass_move(self, game):
        # Set the current player's turn and listen for a click on the game window
        game.turn = self.turn
        game.window.onclick(game.click)
        game.window.update()

# Computer class, inherits from Player
class Computer(Player):
    def __init__(self, turn):
        super().__init__(turn)

    def pass_move(self, game):
        # If it's the computer's turn and the next move is allowed
        if game.allow_next == 'Y':
            # If it's the first move, choose a random position
            if game.count_none_elements() == game.matrix * game.matrix:
                game.turn = self.turn
                game.update_table(random.randint(0, game.matrix - 1), random.randint(0, game.matrix - 1))
                game.allow_next = 'N'
            else:
                # Use the minimax algorithm to determine the optimal move
                coord = self.minimax(game, self.turn)
                game.turn = self.turn
                if game.check() is None:
                    game.update_table(coord['x'], coord['y'])
                    game.allow_next = 'N'

    # Minimax algorithm for determining the optimal move
    def minimax(self, state, player):
        max_one = self.turn  # yourself
        other_player = 'o' if player == 'x' else 'x'
        status = state.check()

        # Check if the previous move is a winner
        if status == other_player:
            if other_player == max_one:
                return {'x': None, 'y': None, 'score': 1 * (state.count_none_elements() + 1)}
            else:
                return {'x': None, 'y': None, 'score': -1 * (state.count_none_elements() + 1)}
        elif status == 'ніхто':
            return {'x': None, 'y': None, 'score': 0}

        # Initialize scores based on whether it's maximizing or minimizing player's turn
        if player == max_one:
            final = {'x': None, 'y': None, 'score': -100}  # each score should maximize
        else:
            final = {'x': None, 'y': None, 'score': 100}  # each score should minimize

        # Iterate through all possible moves
        for i in range(state.matrix):
            for j in range(state.matrix):
                if state.table[i][j] is None:
                    # Simulate a game after making that move
                    state.table[i][j] = player
                    score = self.minimax(state, other_player)
                    # Undo move
                    state.table[i][j] = None
                    score['x'] = i
                    score['y'] = j  # this represents the move optimal next move

                    # Update the final move if it leads to a better score
                    if player == max_one:
                        if score['score'] > final['score']:
                            final = score
                    else:
                        if score['score'] < final['score']:
                            final = score
        return final
