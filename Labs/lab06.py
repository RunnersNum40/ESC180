from random import choice

class TicTacToe:
    def __init__(self, players, size=3):
        self.board = board = [[" " for i in range(size)] for i in range(size)]
        self.size = size
        self.players = players
        self.marks = [player.mark for player in players]

    def main_loop(self):
        winner = None
        while True:
            for player in self.players:
                if self.get_free_squares() == []:
                    break
                print(self)
                player.move(self)
                if self.is_win(player.mark):
                    winner = player.mark
                    break
            if winner:
                print("{} is the winner! GG".format(winner))
                break
        if not winner:
            print("The game is a tie! Booo")

        print(self)
        self.reset()

    def reset(self):
        self.__init__(self.players, self.size)

    def pos(self, square_num, prev={}):
        return (square_num-1)%self.size, (square_num-1)//self.size

    def put_in_board(self, mark, square_num):
        self.board[self.pos(square_num)[0]][self.pos(square_num)[1]] = mark

    def get_free_squares(self):
        return [[x, y] for y in range(self.size) for x in range(self.size) if self.board[x][y] == " "]

    def is_row_all_marks(self, row_i, mark):
        return all(self.board[row_i][i] == mark for i in range(self.size))

    def is_col_all_marks(self, col_i, mark):
        return all(self.board[i][col_i] == mark for i in range(self.size))

    def are_diag_all_marks(self, mark):
        return all(self.board[i][i] ==  mark for i in range(self.size)) or all(self.board[i][self.size-i-1] == mark for i in range(self.size))

    def is_win(self, mark):
        return any(self.is_col_all_marks(i, mark) or self.is_row_all_marks(i, mark) for i in range(self.size)) or self.are_diag_all_marks(mark)

    def __str__(self):
          return ("\n---"+"+---"*(self.size-1)+"\n").join("  |".join([self.board[x][y] for x in range(self.size)]) for y in range(self.size))

class Player:
    def __init__(self, mark):
        self.mark = mark

class HumanPlayer(Player):
    def move(self, game):
        move = int(input("What is your move? "))
        game.put_in_board(self.mark, move)

class ComputerPlayer(Player):
    def make_random_move(self, game):
        corrds = choice(game.get_free_squares())
        game.board[corrds[0]][corrds[1]] = self.mark

    def move(self, game):
        print("Calculating...")
        for i in range(1, 10):
            if game.pos(i) in game.get_free_squares():
                new = TicTacToe()
                new.board = list(map(list, game.board))
                new.put_in_board(self.mark, i)
                if new.is_win(mark):
                    game.put_in_board(self.mark, i)
                    break
        else:
            self.make_random_move(game)

game = TicTacToe((ComputerPlayer("X"), ComputerPlayer("0")), 5)
game.main_loop()