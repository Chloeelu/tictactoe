import random

class TicTacToe:
    PLAYER = 'X'
    COMPUTER = 'O'
    EMPTY = ' '

    def __init__(self): 
        """ initializes data fields (board and played) 
            and prints the banner messages 
            and prints the initial board on the screen
        """
        self.board = [' '] * 9 # A list of 9 strings, one for each cell, 
                               # will contain ' ' or 'X' or 'O'
        self.played = set()    # Set (of cell num) already played: to keep track of the played cells 
        print("Welcome to Tic-Tac-Toe!")
        print("You play X (first move) and computer plays O.")
        print("Computer plays randomly, not strategically.")
        self.printBoard()

    def printBoard(self) -> None:
        """ prints the board on the screen based on the values in the self.board data field """
        print("\n")
        print(self.board[0], "|", self.board[1],"|", self.board[2], "    0| 1 |2")
        print("--+---+--", "--+---+--", sep="    ")
        print(self.board[3], "|", self.board[4],"|", self.board[5], "    3| 4 |5")
        print("--+---+--", "--+---+--", sep="    ")
        print(self.board[6], "|", self.board[7],"|", self.board[8], "    6| 7 |8")
        print("--+---+--", "--+---+--", sep="    ")

    

    def isValidMove(self, number):
        if not number.isdigit():
            print("Must be an integer")
            return False
        number = int(number)
        if number not in range(9):
            print("Must enter a valid cell number")
            return False
        if number in self.played:
            print("Must enter a valid cell number")
            return False
        return True

    def playerNextMove(self) -> None:
        number = input("Next move for X (State a valid cell num):")
        while not self.isValidMove(number):
            number = input()
        self.played.add(int(number)) 
        self.board[int(number)] = self.PLAYER
        self.printBoard()

    def computerNextMove(self) -> None:
        winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for pos in winning_positions:
            i, j, k = pos
            # attempt to win
            if self.board[i] == self.board[j] == self.COMPUTER and k not in self.played:
                step = k
                break
            elif self.board[i] == self.board[k] == self.COMPUTER and j not in self.played:
                step = j
                break
            elif self.board[j] == self.board[k] == self.COMPUTER and i not in self.played:
                step = i
                break
            # Attempt to block player
            elif self.board[i] == self.board[j] == self.PLAYER and k not in self.played:
                step = k
                break
            elif self.board[i] == self.board[k] == self.PLAYER and j not in self.played:
                step = j
                break
            elif self.board[j] == self.board[k] == self.PLAYER and i not in self.played:
                step = i
                break
        else:
            while True:
                step = random.randrange(9)
                if step not in self.played:
                    break
        self.played.add(step) 
        self.board[step] = self.COMPUTER
        self.printBoard()

    def isWinningMove(self, i, j, k):
        return self.board[i] == self.board[j] == self.board[k] != self.EMPTY

    def hasWon(self, who: str) -> bool:
        winning_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        return any(self.isWinningMove(*pos) for pos in winning_positions)

    def terminate(self, who: str) -> bool:
        winner = self.hasWon(who)
        if winner and who == self.PLAYER:
            print("You won! Thanks for playing.")
            return True
        if winner and who == self.COMPUTER:
            print("You lost! Thanks for playing.")
            return True
        if len(self.played) == 9:
            print("A draw! Thanks for playing.")
            return True 
        return False

if __name__ == "__main__":
    ttt = TicTacToe()
    while True:
        ttt.playerNextMove()
        if(ttt.terminate(TicTacToe.PLAYER)): break
        ttt.computerNextMove()
        if(ttt.terminate(TicTacToe.COMPUTER)): break
