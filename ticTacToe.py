'''
-------------------------------------------------------------------------------------------------
Author: Tyler Hanf
06/18/2019
Filename: ticTacToe.py

This code demonstrates the use of many basic programming concepts
including classes, functions, for and while loops, basic logic, if statements,
and types. If you are confused at any point, my comments should help to explain some concepts and my
thought process.
--------------------------------------------------------------------------------------------------
'''

'''
--------------------------------------------------------------
The player class defines which piece the player will put down.
i.e. either an 'X' or an 'O'.
--------------------------------------------------------------
'''
class Player:
    '''
    The __init__ method is called once an instance
    of the class is made. 
    
    When the Player class is called, the __init__ method
    will execute and set the 'piece' variable to the contents
    of 'marker'.
    
    In order to make an instance of the class Player,
    set a variable (such as player1) to Player(*insert piece character*)
    
    Example: player1 = Player('X')
    
    See line 75 and 76 for the implementation
    ''' 
    def __init__(self, marker: str, name: str):
        self.piece = marker
        self.name = name

'''
--------------------------------------------------------------
The board class represents a tic tac toe board.

i.e.  0 | 1 | 2
     ---|---|---
      3 | 4 | 5
     ---|---|---
      6 | 7 | 8

Each digit represents a spot and will be used by each player
to select the spot they wish to place their piece on.
---------------------------------------------------------------
'''
class Board:
    '''
    The board initializes by creating an array
    named 'spots' comprised of each spot where the index is the spot number
    and the value is None because no piece has been 
    placed yet.
    
    Index Number:  0     1     2     3     4     5     6     7     8
    self.spots = [None, None, None, None, None, None, None, None, None]
    
    '''
    def __init__(self):
        # create empty list
        self.spots = list()
        # fill self.spots  with 9 spots containing None
        for i in range(9):
            self.spots.append(None)

    '''
    The printSpot method takes a spot number (an index for the spots array)
    and prints the index number if the value of the spot is 'None' (no player
    has placed a piece on that spot). If the value is either an 'X' or 'O', the 
    correct piece will be printed.

    Benefits of this function (and the purpose of functions in general):
        1. Easier for others to read code and understand what is happening
        2. Since each spot has to be checked, this saves a lot of code space
        3. Makes development faster because I do not have to rewrite code many times
        4. If I needed to change the if statement in any way, I only need to change one location
    '''
    def printSpot(self, spotNum: int):
        if self.spots[spotNum] == None:
            return spotNum
        else:
            return self.spots[spotNum]

    '''
    printBoard() prints the current state of the board.

    printSpot() is used to check each spot and display a
    players piece if a piece has been placed there.

    The spot number will be shown if the spot is empty
    '''
    def printBoard(self):
        print("  ", self.printSpot(0), " | ", self.printSpot(1), " | ", self.printSpot(2))
        print("------|-----|------")
        print("  ", self.printSpot(3), " | ", self.printSpot(4), " | ", self.printSpot(5))
        print("------|-----|------")
        print("  ", self.printSpot(6), " | ", self.printSpot(7), " | ", self.printSpot(8))

    '''
    placePiece() takes a spot index and the players piece (either 'X' or 'O')

    It sets the value at the spotNum to either 'X' or 'O'

    This function assumes a player is putting in a correct value
    For simplicity, I chose to leave out the code for checking the spot number

    Parameter types are included to make it easer for another person to read the code
    '''
    def placePiece(self, spotNum: int, playerPiece: str):
        self.spots[spotNum] = playerPiece

    '''
    checkWin() determines if either player has won.
    
    It is called at every cycle of the game loop

    True is returned if someone has one, else returns False
    
    Note 1: The last part of each if statement is used to determine
    if checking is truly right. The first half logic works if every 
    value is 'None', so I needed to ensure that all the values are the same
    (either 'X' or 'O') but are also not 'None'

    Note 2: It is best practice to set numbers to constant variables rather
    than just having 'random' numbers. Because tic-tac-toe does not change 
    and we know exactly how it will be implemented, the 'hard coding' of numbers
    is ok, but not ideal.
    '''
    def checkWin(self):
        # Checks to see if all values are the same in each row
        # The for loop steps by 3 because the beginning of each row increments by 3
        # Refer to lines 44-48 to visualize the logic
        for i in range(0, 9, 3):
            if (self.spots[i] == self.spots[i+1] == self.spots[i+2]) and self.spots[i] != None:
                return True

        # Checks to see if all the values are the same in each column
        # Each subsequent index in the same column is 3 more than the previous spot
        # Refer to lines 44-48 to visualize the logic
        for i in range(3):
            if (self.spots[i] == self.spots[i+3] == self.spots[i+6]) and self.spots[i] != None:
                return True
        
        # Checks the diagonal from the top left corner to the bottom right
        if (self.spots[0] == self.spots[4] == self.spots[8]) and self.spots[0] != None:
            return True

        # Checks the diagonal from the top right corner to the bottom left
        if (self.spots[2] == self.spots[4] == self.spots[6]) and self.spots[2] != None:
            return True

        # If none of the if statements were true, then no one has won,
        # so return false
        return False

'''
It is common practice to run the 'main' code in a 'main' function.

Here is the 'main' code for tic-tac-toe is doing:
    1. Create a board
    2. Assign players
    3. Start a game loop
    4. Once a player has won or all the tiles are filled, quit
    5. Display the results of the game to the players.

All of the other code outside of the 'main' function is called from 
within this function and used for the above stated goals to be met
'''
def main():
    # Create an instance of the board
    board = Board()

    # Create the two players
    # Assign player1 piece to be 'X' with name "Player 1"
    # Assign player2 piece to be 'X' with name "Player 2"
    p1 = Player('X', "Player 1")
    p2 = Player('O', "Player 2")

    # Display welcome message
    print("Welcome to Tic-Tac-Toe!\n")
    
    # Print the board for the first time
    board.printBoard()

    # moveTracker keeps track of the number of moves
    # if 9 pieces has been played an no one has one, it must be a tie
    moveTracker = 0

    # Sets the current player to 'p1'
    # This will be used to determine which piece should be placed
    # and who has won
    currentPlayer = p1

    # This is the main game loop
    # Will repeat until 9 pieces have been placed or someone has one
    while moveTracker < 9:
        print("Ok,", currentPlayer.name, ", make your move by typing a number on the board")

        # input must be wrapped in int() to set the selectedSpot as int not string
        # input is defaulted to string
        selectedSpot = int(input())

        # Place the piece
        board.placePiece(selectedSpot, currentPlayer.piece) 

        # Print the board
        board.printBoard()
        
        # Check to see if anyone has won, if so, break
        if board.checkWin():
            break;

        # Increment number of pieces by 1 as another piece has been placed
        # and no one has one
        moveTracker += 1

        # Switch the current player via inline if statement
        currentPlayer = p2 if currentPlayer == p1 else p1

    # if moveTracker is 9, it must have been a tie
    if moveTracker == 9:
        print("GAME OVER...TIE!")
    
    # if moveTracker is not 9, someone must have won
    # The last person to place piece must have won
    else:
        print("GAME OVER...", currentPlayer.name, " WINS!")
        
# Standard format for using main function in python... 
# Go to the below link for more info: 
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
    main()



