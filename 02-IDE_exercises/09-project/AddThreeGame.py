class AddThreeGame:

    def __init__ (self):
        self._player1_choices: list = []
        self._player2_choices: list = []
        self._current_state = 'UNFINISHED'
        self._whose_turn = 'first'

    def get_current_state(self):
        return self._current_state

    def make_move (self, which_player: str, number: int):
        if self._player1_choices + self._player2_choices == [1,2,3,4,5,6,7,8,9]:
            self._current_state = 'DRAW'
            return True
        if which_player != 'first' and which_player != 'second':
            return False
        if self._whose_turn == 'first' and which_player == 'second':
            return False
        if self._whose_turn == 'second' and which_player == 'first':
            return False
        if self._whose_turn == 'first' and which_player == 'first':
            if number not in range(1,10):
                return False
            if number not in self._player1_choices and number not in self._player2_choices:
                self._player1_choices.append(number)
                if len(self._player1_choices) < 3:
                    self._whose_turn = 'second'
                    return True
                else:
                    if len(self._player1_choices) == 3:
                        if self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[0] == 15:
                            self._current_state = 'FIRST WON'
                            return True
                        else:
                            self._whose_turn = 'second'
                            return True
                    if len(self._player1_choices) == 4:
                        if self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[3] == 15 or self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[0] ==15 or self._player1_choices[1] + self._player1_choices[3] + self._player1_choices[0] == 15 or self._player1_choices[0] + self._player1_choices[2]+self._player1_choices[3] == 15:
                            self._current_state = 'FIRST WON'
                            return True
                        else:
                            self._whose_turn = 'second'
                            return True
                    if len(self._player1_choices) == 5:
                        if self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[3] == 15 or self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[4] == 15 or self._player1_choices[1] + self._player1_choices[2] + self._player1_choices[0] == 15 or self._player1_choices[1] + self._player1_choices[3] + self._player1_choices[4] == 15 or self._player1_choices[1] + self._player1_choices[3] + self._player1_choices[0] == 15 or self._player1_choices[1] + self._player1_choices[4] + self._player1_choices[0] == 15 or self._player1_choices[2] + self._player1_choices[3] + self._player1_choices[4] == 15 or self._player1_choices[2] + self._player1_choices[3] + self._player1_choices[0] == 15 or self._player1_choices[2] + self._player1_choices[4] + self._player1_choices[0] == 15 or self._player1_choices[3] + self._player1_choices[4] + self._player1_choices[0] == 15:
                            self._current_state = 'FIRST WON'
                            return True
                        else:
                            self._whose_turn = 'second'
                            return True
                return False
        if self._whose_turn == 'second' and which_player == 'second':
            if number not in range(1,10):
                return False
            if number not in self._player1_choices and number not in self._player2_choices:
                self._player2_choices.append(number)
                if len(self._player2_choices) < 3:
                    self._whose_turn = 'first'
                    return True
                else:
                    if len(self._player2_choices) == 3:
                        if self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[0] == 15:
                            self._current_state = 'SECOND WON'
                            return True
                        else:
                            self._whose_turn = 'first'
                            return True
                    if len(self._player2_choices) == 4:
                        if self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[3] == 15 or self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[0] ==15 or self._player2_choices[1] + self._player2_choices[3] + self._player2_choices[0] == 15 or self._player2_choices[0] + self._player2_choices[2] + self._player2_choices[3] == 15:
                            self._current_state = 'SECOND WON'
                            return True
                        else:
                            self._whose_turn = 'first'
                            return True
                    if len(self._player2_choices) == 5:
                        if self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[3] == 15 or self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[4] == 15 or self._player2_choices[1] + self._player2_choices[2] + self._player2_choices[0] == 15 or self._player2_choices[1] + self._player2_choices[3] + self._player2_choices[4] == 15 or self._player2_choices[1] + self._player2_choices[3] + self._player2_choices[0] == 15 or self._player2_choices[1] + self._player2_choices[4] + self._player2_choices[0] == 15 or self._player2_choices[2] + self._player2_choices[3] + self._player2_choices[4] == 15 or self._player2_choices[2] + self._player2_choices[3] + self._player2_choices[0] == 15 or self._player2_choices[2] + self._player2_choices[4] + self._player2_choices[0] == 15 or self._player2_choices[3] + self._player2_choices[4] + self._player2_choices[0] == 15:
                            self._current_state = 'SECOND WON'
                            return True
                        else:
                            self._whose_turn = 'first'
                            return True
                return False

game = AddThreeGame()
game.make_move('first', 3)
game.make_move('second', 7)
game.make_move('first', 8)
game.make_move('second', 2)
game.make_move('first', 5)
game.make_move('second', 6)
print(game.get_current_state())
