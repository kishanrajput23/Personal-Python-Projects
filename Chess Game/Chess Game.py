import random 

class Board:
    #A class to represent the chess board
    squares = {}

    #Probably a better way for board to have access to players
    players = []

    #Creates all squares and adds them to the board
    def populateSquares(self):
       # print("here")
        for x in range(8):
            for y in range(8):
                number = x * 8 + y
                pos = [x, y]
                
                # if (y == 1):
                #     occ = Pawn(pos,"White")
                #     self.players[0].pieces.append(occ)
                # elif (y == 6):
                #     occ = Pawn(pos,"Black")
                #     self.players[1].pieces.append(occ)
                if (y == 0):
                    occ = self.populateKingRow(0,pos,"White")
                    self.players[0].pieces.append(occ)
                elif (y == 7):
                    occ = self.populateKingRow(7,pos,"Black")
                    self.players[1].pieces.append(occ)
                else: 
                    occ = None                    

                #Even rows have black - white pattern
                if (x % 2 ==  0):
                    if (y % 2 == 0):
                        color = "Black"
                    else: color = "White"
                #Odd rows have white - black pattern
                else: 
                    if (y % 2 == 0):
                        color = "White"
                    else: color = "Black"
                
                self.squares[number] = (Square(pos, occ, color))

    #Populates given row with classic pieces (non pawns)
    def populateKingRow(self, row, pos, color):
        if (pos[1] == row):
            if (pos[0] == 0 or pos[0] == 7):
                return Rook(pos, color)
            elif (pos[0] == 1 or pos[0] == 6):
                return Knight(pos, color)
            elif (pos[0] == 2 or pos[0] == 5):
                return Bishop(pos, color)
            elif (pos[0] == 3):
                return Queen(pos, color)
            else:
                return King(pos, color)

    def getSquareAtPos(self, pos):
        num = pos[0] * 8 + pos[1] 

        #If pos is out of bounds then return None
        if (num > 63 or num < 0):
            return None
        return self.squares[num]
    
    def getPieceAtPos(self, pos):
        square = self.getSquareAtPos(pos)
        return square.occupied

    def getPlayer(self, color):
        if color == "White":
            return self.players[0]
        return self.players[1]

class Square:
        number = int
        position = [int, int]
        occupied = None
        color = str
       
        def __init__(self, pos, occ, color):
            self.position = pos
            self.occupied = occ
            self.color = color

class Piece:
    name = str
    position = [int, int]
    color = str

    #Returns whether int1 and int 2 or both positive or negative
    def samePolarity(self, int1, int2):
        if int1 > 0:
            if int2 > 0:
                return True
        if int1 < 0:
            if int2 < 0:
                return True
        return False

    #Returns whether moving to this square will put yourself in check
    def selfCheck(self, board, square):
        player = board.getPlayer(self.color)
        opponent = player.getOpponent(board)
        #If this piece is players King
        if self.name == "King":
            pass
        else:
            #Get the players King
            king = None
            for piece in player.pieces:
                if piece.name == "King":
                    king = piece
                    break

            posDif = [self.position[0] - king.position[0], 
                      self.position[1] - king.position[1]]

            #in the same column as King
            if self.position[0] == king.position[0]:
                if square.position[0] == self.position[0]: #if square is in same column, king is still safe
                    return False
                if posDif[1] > 0:   #if piece is above King
                    increment = 1
                else:               #piece is below King
                    increment = -1
                newPos = self.position.copy()
                newPos[1] += increment
                newSquare = board.getSquareAtPos(newPos)
                while newSquare != None:    #while on a square in bounds 
                    piece = newSquare.occupied
                    if piece != None:  #if it has a piece on it
                        if piece.color == player.color: #if another of players pieces is blocking King
                            return False
                        else: 
                            if (piece.name == "Rook" or piece.name == "Queen"): #if it is an enemy Rook or Queen
                                return True
                    newPos[1] += increment
                    newSquare = board.getSquareAtPos(newPos)
                return False

            #in the same row as King
            if self.position[1] == king.position[1]:
                if square.position[1] == self.position[1]: #if move is in same row, king is still safe
                    return False
                if posDif[0] > 0:   #if piece is right of King
                    increment = 1
                else:               #piece is left of King
                    increment = -1
                newPos = self.position.copy()
                newPos[0] += increment
                newSquare = board.getSquareAtPos(newPos)
                while newSquare != None:    #while on a square in bounds 
                    piece = newSquare.occupied
                    if piece != None:  #if it has a piece on it
                        if piece.color == player.color: #if another of players pieces is blocking King
                            return False
                        else: 
                            if (piece.name == "Rook" or piece.name == "Queen"): #if it is an enemy Rook or Queen
                                return True
                    newPos[0] += increment
                    newSquare = board.getSquareAtPos(newPos)
                return False
                
            #diagonal to King
            if abs(posDif[0]) == abs(posDif[1]):
                squareDif = [square.position[0] - king.position[0], 
                square.position[1] - king.position[1]]
                #If square in the same diagonal
                if self.samePolarity(posDif[0], squareDif[0]) and samePolarity(posDif[1], squareDif[1]):
                    return False                
                if posDif[0] > 0:   #if piece is right of King
                  incrementX = 1
                else:               #piece is left of King
                    incrementX = -1
                if posDif[1] > 0:   #if piece is above King
                    incrementY = 1
                else:               #piece is below King
                    incrementY = -1
                newPos = self.position.copy()
                newPos[0] += incrementX
                newPos[1] += incrementY
                newSquare = board.getSquareAtPos(newPos)
                while newSquare != None:    #while on a square in bounds 
                    piece = newSquare.occupied
                    if piece != None:  #if it has a piece on it
                        if piece.color == player.color: #if another of players pieces is blocking King
                            return False
                        else: 
                            if (piece.name == "Bishop" or piece.name == "Queen"): #if it is an enemy Rook or Queen
                                return True
                    newPos[0] += incrementX
                    newPos[1] += incrementY
                    newSquare = board.getSquareAtPos(newPos)
                return False
        


    #Checks that the square reached by pos is a valid square for this piece"""
    def isSquareValid(self, board, square):
        if square == None:
            return False

        if self.selfCheck(board, square):
            print("Cannot put yourself in check")
            return False

        #Is that square occupied by another of your pieces?
        piece = square.occupied
        if (piece != None and piece.color == self.color):
            return False
        
        #Pawns cannot attack up
        if (piece != None and self.name == "Pawn" and piece.position[0] == self.position[0]):
            return False

        #Pawns cannot move diagonally unless capturing
        if (piece == None and self.name == "Pawn" and 
        (square.position[0] == self.position[0] + 1 or square.position[0] == self.position[0] - 1)):
            return False
        
        return True
        
    """ Checks whether every square in a line determined by change in x and y is valid """
    def isLineValid(self, board, changeInX, changeInY, range):
        if (range == 0): range = 7
        validSquares = []
        newPos = self.position.copy()
        newPos[0] += changeInX
        newPos[1] += changeInY
        count = 0
        while self.isSquareValid(board, board.getSquareAtPos(newPos)) and count < range:
            square = board.getSquareAtPos(newPos)

            #if current square has an enemy on it break 
            if (square.occupied != None):
                validSquares.append(square)
                return validSquares
            else:
                validSquares.append(square)
                newPos[0] += changeInX
                newPos[1] += changeInY
                count += 1
        return validSquares


    #Moves the piece to designated square if possible
    # returns True if move was valid, False if not
    def move(self, board, square, player):
        if (self.color != player.color):
            print("Not your piece")
            return False
        validMoves = self.getValidMoves(board)
        if square in validMoves:
            #Remove Piece from current square
            board.getSquareAtPos(self.position).occupied = None
            #If square has an enemy piece on it, capture it
            if (square.occupied != None):
                player.capturedPieces.append(square.occupied)
            #Move Piece to new square
            self.position = square.position
            #Mark that square is occupied by this piece
            square.occupied = self
            return True
        else: 
            print("Not a valid move")
            return False

class Pawn(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col   
        self.name = "Pawn"

    def getValidMoves(self, board):
        validMoves = []
        #Up or forward depends on color
        if (self.color == "White"):
            up = 1
        else:
            up = -1
        #If the pawn has not moved
        if ((self.color == "White" and self.position[1] == 1) or
            (self.color == "Black" and self.position[1] == 6)):
            validMoves.extend(super().isLineValid(board, 0, up, 2))  #Can move up 2 
        else:
            validMoves.extend(super().isLineValid(board, 0, up, 1))  #Up
        validMoves.extend(super().isLineValid(board, 1, up, 1))  #Right Diagonal
        validMoves.extend(super().isLineValid(board, -1, up, 1)) #Left Diagonal
        return validMoves

class Rook(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Rook"

    def getValidMoves(self, board):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 0))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 0)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 0))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 0)) #Down
        return validMoves

class Knight(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Knight"
        
    def getValidMoves(self, board):
        pos = self.position.copy()
        xPos = pos[0]
        yPos = pos[1]
        validMoves = []
        possibleMoves = [[xPos + 2, yPos + 1],
                        [xPos + 2, yPos - 1],
                        [xPos - 2, yPos + 1],
                        [xPos - 2, yPos - 1],
                        [xPos + 1, yPos + 2],
                        [xPos - 1, yPos + 2],
                        [xPos + 1, yPos - 2],
                        [xPos - 1, yPos - 2]]
        for move in possibleMoves: 
            square = board.getSquareAtPos(move)
            if (self.isSquareValid(board, square)):
                validMoves.append(square)
        return validMoves        

class Bishop(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Bishop"

    def getValidMoves(self, board):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 1, 0))  #Right Forward Diag
        validMoves.extend(super().isLineValid(board, -1, 1, 0)) #Left Forward Diag
        validMoves.extend(super().isLineValid(board, 1, -1, 0)) #Right Back Diag
        validMoves.extend(super().isLineValid(board, -1, -1, 0)) #Left Back Diag
        return validMoves

class Queen(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "Queen"

    def getValidMoves(self, board):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 0))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 0)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 0))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 0)) #Down
        validMoves.extend(super().isLineValid(board, 1, 1, 0))  #Right Forward Diag
        validMoves.extend(super().isLineValid(board, -1, 1, 0)) #Left Forward Diag
        validMoves.extend(super().isLineValid(board, 1, -1, 0)) #Right Back Diag
        validMoves.extend(super().isLineValid(board, -1, -1, 0)) #Left Back Diag
        return validMoves

class King(Piece):
    def __init__(self, pos, col):
        self.position = pos
        self.color = col
        self.name = "King"

    def getValidMoves(self, board):
        validMoves = []
        validMoves.extend(super().isLineValid(board, 1, 0, 1))  #Right
        validMoves.extend(super().isLineValid(board, -1, 0, 1)) #Left
        validMoves.extend(super().isLineValid(board, 0, 1, 1))  #Up
        validMoves.extend(super().isLineValid(board, 0, -1, 1)) #Down
        validMoves.extend(super().isLineValid(board, 1, 1, 1))  #Right Forward Diag
        validMoves.extend(super().isLineValid(board, -1, 1, 1)) #Left Forward Diag
        validMoves.extend(super().isLineValid(board, 1, -1, 1)) #Right Back Diag
        validMoves.extend(super().isLineValid(board, -1, -1, 1)) #Left Back Diag
        return validMoves

class Player:
    color = str
    pieces = []
    capturedPieces = []

    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.capturedPieces = []
    
    def getOpponent(self, board):
        opponent = (board.players[1] if board.players[0] == self else board.players[0])
        return opponent


def drawBoard(board):
    print(" ")
    print(" ")
    print("Black Captured: ", end = "")
    for captured in board.players[1].capturedPieces:
        print(captured.name[:4], end = " ")
    print(" ")
    print(" ")
    for y in range(9):
        #print guide numbers before each row
        if (y < 8):
            print(8-y, end = " ")
        else:
            print(" ", end = " ")
        for x in range(8):
            #If on the last row print guide letters
            if (y==8): 
                print ("   " +numToLetter(x) + "   ", end = "")
            else:
                invrow = 7-y
                square = board.getSquareAtPos([x, invrow])
                if (square.occupied == None):
                    print("|  " + square.color[0] + '  |', end = "")
                else:
                    print("|" + square.occupied.name[0:4] + ' |', end = "")
                if (x == 7):
                    print(" ")
    print(" ")
    print(" ")
    print("White captured: ", end = "")
    for captured in board.players[0].capturedPieces:
        print(captured.name[:4], end = " ")
    print(" ")
    print(" ")

#Converts number of row to a letter
def numToLetter(num):
    if (num == 0):
        num  = "A"
    elif (num == 1):
        num = "B"
    elif (num == 2):
        num = "C"
    elif (num == 3):
        num = "D"
    elif (num == 4):
        num = "E"
    elif (num == 5):
        num = "F"
    elif (num == 6):
        num = "G"
    elif (num == 7):
        num = "H"
    else:
        print("Number: " + num + " is not valid")
        return
    return num

#Converts letter of a row to a number
def letterToNum(letter):
    if (letter == "A"):
        letter = 0
    elif (letter == "B"):
        letter = 1
    elif (letter == "C"):
        letter = 2
    elif (letter == "D"):
        letter = 3
    elif (letter == "E"):
        letter = 4
    elif (letter == "F"):
        letter = 5
    elif (letter == "G"):
        letter = 6
    elif (letter == "H"):
        letter = 7
    else:
        print("Letter: " + letter + " is not valid")
        return
    return letter


#Converts traditional chess positions (i.e A8) to positions
def alphaNumMoveToPos(text):
    letter = text[0].capitalize()
    number = text[1]
    #convert letters to x 
    letter = letterToNum(letter)
    #convert numbers from 1-8 to 0-7
    if (number.isnumeric()):
        number = int(number) - 1
        if (number > 7 or number < 0):
            print("Number: " + number + " is not valid")
            return
    else: 
        print("Number: " + number + " is not valid")
        return
    return [letter, number]

#Parses the text into a move and moves the pieces
#Returns whether the move was valid
def parseMove(text, board, player):
    try:
        trimText = text.strip()
        piecePos = alphaNumMoveToPos(trimText[0:2])
        targetSquare = alphaNumMoveToPos(trimText[3:])
    except:
        print("Move not Valid")
        return False

    if (piecePos == None or targetSquare == None):
        return False
    piece = board.getPieceAtPos(piecePos)
    if piece == None:
        return False
    square = board.getSquareAtPos(targetSquare)
    validMove = piece.move(board, square, player)
    return validMove

        

def startGame():
    #Create the board
    board = Board()

    #Create Players and assign them random color
    colors = ["White", "Black"]
    playerColor = random.randint(0, 1)
    player1 = Player(colors[playerColor])
    player2 = Player(colors[1-playerColor])

    #Probably a cleaner way to pass players into move function, Fine for now
    if (player1.color == "White"):
        whitePlayer = player1
        blackPlayer = player2 
    else:
        whitePlayer = player2
        blackPlayer = player1 

    board.players = [whitePlayer, blackPlayer]
    board.populateSquares()
    drawBoard(board)

    gameOver = False
    whiteTurn = True
    while not gameOver:
        if (whiteTurn):
            move = input("White's move:")
            if (move == "end"):
                gameOver = True
                return
            validMove = parseMove(move, board, whitePlayer)
        else:
            move = input("Black's move:")
            if (move == "end"):
                gameOver = True
                return
            validMove = parseMove(move, board, blackPlayer)
        if (validMove):
            whiteTurn = not whiteTurn
        drawBoard(board)

startGame()