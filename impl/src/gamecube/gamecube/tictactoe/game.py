#!/usr/bin/env python

import copy

class GameState(object):

    def __init__(self, board, next_player):
        # the state of the board as `next_player` sees it
        self.board = copy.deepcopy(board)

        # the next player to move, i.e. the next shape (X, O) that will be placed on the board.
        self.next_player = copy.deepcopy(next_player)
    
    def copy(self):
        return GameState(self.board, self.next_player)
    
    def get_valid_moves(self) -> set:
        moves = set()
        for idx, player in enumerate(self.board):
            if player is None:
                moves.add(idx)
        return moves
    
    def move(self, position):
        tmp = copy.deepcopy(self.board)
        tmp[position] = self.next_player

        return GameState(tmp, -self.next_player)
    
    def __repr__(self):
        i2s = lambda i: {None:str(i[0]), 1:"X", -1:"O"}[i[1]]
        boardi2s = list(map(i2s, enumerate(self.board)))

        return f"""
        :: next_player {'X' if self.next_player == 1 else 'O'}
        >> {''.join(boardi2s[0:3])}
        >> {''.join(boardi2s[3:6])}
        >> {''.join(boardi2s[6:9])}
        """

class BadMoveException(Exception):
    pass

class TicTacToe(object):

    def __init__(self):
        self.state = None
        self.history = None
        
        self.reset_game()

    def create_fresh_board(self):
        return [None for _ in range(9)]

    def reset_game(self):
        self.state = GameState(self.create_fresh_board(), 1)
        self.history = []

    def check_win(self):
        board = self.state.board

        # rows
        if board[0] == board[1] == board[2]:
            if board[0] is None:
                return False, None
            return True, board[0]

        if board[3] == board[4] == board[5]:
            if board[3] is None:
                return False, None
            return True, board[3]

        if board[6] == board[7] == board[8]:
            if board[6] is None:
                return False, None
            return True, board[6]

        # columns
        if board[0] == board[3] == board[6]:
            if board[0] is None:
                return False, None
            return True, board[0]

        if board[1] == board[4] == board[7]:
            if board[1] is None:
                return False, None
            return True, board[1]

        if board[2] == board[5] == board[8]:
            if board[2] is None:
                return False, None
            return True, board[2]

        # diagonals
        if board[0] == board[4] == board[8]:
            if board[0] is None:
                return False, None
            return True, board[0]

        if board[2] == board[4] == board[6]:
            if board[2] is None:
                return False, None
            return True, board[2]
        
        return False, None

    def move(self, position):
        valid_moves = self.state.get_valid_moves()

        if position in valid_moves:
            next_state = self.state.move(position)
            self.history.append(next_state.copy())
            self.state = next_state
        else:
            raise BadMoveException(
                f"Bad move `{position}`; valid moves = `{valid_moves}`"
                )

if __name__ == "__main__":
    def main():
        # repl
        ttt = TicTacToe()
        ttt.reset_game()

        game_over, win = ttt.check_win()

        while not game_over:
            print(ttt.state)
            usr = int(input(f"{ttt.state.next_player}> "))
            ttt.move(usr)
            game_over, win = ttt.check_win()

        print(f"winner: {win}")

    main()
