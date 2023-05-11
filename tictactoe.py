import random

class TicTacToe:
    def __init__(self): # Use as is
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


    def playerNextMove(self) -> None:
        """ prompts the player for a valid cell number; 
            error checks that the input is a valid cell number; 
            and prints the info and the updated self.board;
        """
        number = input("Next move for X (State a vaild cell num):")

        while True:
            if number.isdigit():
                number = int(number)
                if number in range(0,9):
                    print("You chose cell", number)
                    if number in self.played:
                        print("Must enter a vaild cell number")
                        number = input()
                    else:
                        self.played.add(number) 
                        self.board[number] = "X"
                        self.printBoard()
                        break     
                else:
                    print("Must enter a vaild cell number")
                    number = input()
            else: 
                print("Must be an integer")
                number = input()
        

        

    def computerNextMove(self) -> None:
        """ computer randomly chooses a valid cell, 
            and prints the info and the updated self.board 
        """
        while True:
            step = random.randrange(9)
            if step in self.played:
                step = random.randrange(9)  
            else:
                self.played.add(step) 
                self.board[step] = "O"
                self.printBoard()
                break  

    def hasWon(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won, False otherwise """
        winner = (self.board[0]==who and self.board[1]==who and self.board[2]==who) or\
        (self.board[3]==who and self.board[4]==who and self.board[5]==who) or\
        (self.board[6]==who and self.board[7]==who and self.board[8]==who) or\
        (self.board[0]==who and self.board[3]==who and self.board[6]==who) or\
        (self.board[1]==who and self.board[4]==who and self.board[7]==who) or\
        (self.board[2]==who and self.board[5]==who and self.board[8]==who) or\
        (self.board[0]==who and self.board[4]==who and self.board[8]==who) or\
        (self.board[2]==who and self.board[4]==who and self.board[6]==who)
        return winner                         

    def terminate(self, who: str) -> bool:
        """ returns True if who (being passed 'X' or 'O') has won or if it's a draw, False otherwise;
            it also prints the final messages:
                 "You won! Thanks for playing." or 
                 "You lost! Thanks for playing." or 
                 "A draw! Thanks for playing."  
        """
        winner = self.hasWon(who)
        if winner and  who=='X':
            print("You won! Thanks for playing.")
            return True
        if winner and  who=='O':
            print("You lost! Thanks for playing.")
            return True
        if len(self.played) == 9:
            print("A draw! Thanks for playing.")
            return True 
        return False

if __name__ == "__main__":  # Use as is
    ttt = TicTacToe()  # initialize a game
    while True:
        ttt.playerNextMove()            # X starts first
        if(ttt.terminate('X')): break   # if X won or a draw, print message and terminate
        ttt.computerNextMove()          # computer plays O
        if(ttt.terminate('O')): break   # if O won or a draw, print message and terminate
