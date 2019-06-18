class Player:
    def __init__(self, marker):
        self.piece = marker

class Board:

    def __init__(self):
        self.spots = list()
        for i in range(9):
            self.spots.append(None)

    def printSpot(self, spotNum):
        if self.spots[spotNum] == None:
            return spotNum
        else:
            return self.spots[spotNum]

    def printBoard(self):
        print("  ", self.printSpot(0), " | ", self.printSpot(1), " | ", self.printSpot(2))
        print("------|-----|------")
        print("  ", self.printSpot(3), " | ", self.printSpot(4), " | ", self.printSpot(5))
        print("------|-----|------")
        print("  ", self.printSpot(6), " | ", self.printSpot(7), " | ", self.printSpot(8))

    def placePiece(self, piece, playerPiece:str ):
        self.spots[piece] = playerPiece

    def checkWin(self):
        for i in range(0, 9, 3):
            if (self.spots[i] == self.spots[i+1] == self.spots[i+2]) and self.spots[i] != None:
                return True
        for i in range(2):
            if (self.spots[i] == self.spots[i+3] == self.spots[i+6]) and self.spots[i] != None:
                return True
        
        if (self.spots[0] == self.spots[4] == self.spots[8]) and self.spots[0] != None:
            return True

        if (self.spots[2] == self.spots[4] == self.spots[6]) and self.spots[2] != None:
            return True

        return False

def main():
    board = Board()
    p1 = Player('X')
    p2 = Player('O')

    board.printBoard()

    print("Welcome to Tic-Tac-Toe!\n")
    
    moveTracker = 0
    currentPlayer = p1

    while moveTracker < 9 and not board.checkWin():
        print("Ok,", currentPlayer.piece, ", make your move by typing a number on the board")

        selectedSpot = int(input())
        board.placePiece(selectedSpot, currentPlayer.piece) 
        board.printBoard()
        
        moveTracker += 1
        currentPlayer = p2 if currentPlayer == p1 else p1

    if moveTracker == 9:
        print("GAME OVER...TIE!")
    
    else:
        print("GAME OVER...", ("Player 1"  if currentPlayer == p2 else "Player 2"), " WINS!")
        
main()



