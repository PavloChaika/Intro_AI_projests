import random
import time

class Player():
    def __init__(self, turn):
         self.turn = turn

    def pass_move(self,game):
        pass


class HumanPlayer(Player):
    def __init__(self, turn):
        super().__init__(turn)

    def pass_move(self, game):
        game.turn = self.turn
        game.window.onclick(game.click)
        game.window.update()

class Computer(Player):
    def __init__(self, turn):
        super().__init__(turn)

    def pass_move(self, game):
        if game.allow_next == 'Y':
            if game.count_none_elements() == game.matrix * game.matrix:
                game.turn = self.turn
                game.update_table(random.randint(0, game.matrix - 1),
                                  random.randint(0, game.matrix - 1))
                game.allow_next = 'N'
            else:
                coord = self.minimax(game, self.turn)
                game.turn = self.turn
                if game.check() is None:
                    game.update_table(coord['x'], coord['y'])
                    game.allow_next = 'N'

    def minimax(self, state, player):
        max_one = self.turn  # yourself
        other_player = 'o' if player == 'x' else 'x'
        status = state.check()
        # first we want to check if the previous move is a winner
        if status == other_player:
            if other_player == max_one:
                return {'x': None, 'y': None, 'score': 1 * (state.count_none_elements() + 1)}
            else:
                return {'x': None, 'y': None, 'score': -1 * (state.count_none_elements() + 1)}
        elif status == 'ніхто':
            return {'x': None, 'y': None, 'score': 0}

        if player == max_one:
            final = {'x': None, 'y': None, 'score': -100}  # each score should maximize
        else:
            final = {'x': None, 'y': None, 'score': 100}  # each score should minimize
        for i in range(state.matrix):
            for j in range(state.matrix):
                if state.table[i][j] is None:
                    state.table[i][j] = player
                    score = self.minimax(state, other_player)  # simulate a game after making that move
                    # undo move
                    state.table[i][j] = None
                    score['x'] = i
                    score['y'] = j  # this represents the move optimal next move
                    if player == max_one:  # X is max player
                        if score['score'] > final['score']:
                            final = score
                    else:
                        if score['score'] < final['score']:
                            final = score
        return final