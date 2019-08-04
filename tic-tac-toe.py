
import random

def createboard(boardsize):
    board = []
    for i in range(boardsize):
        row = [' '] * boardsize
        board.append(row)
    return board

def reset(board):
    boardsize = len(board)
    
    for i in range(boardsize):
        for j in range(boardsize):
            board[i][j] = ' '

def printboardrow(board, rownumber):
    boardsize = len(board)
    row = ''
    for j in range(boardsize - 1):
        row = row + ' ' + board[rownumber][j] + ' ' + '|' 
        
    row = row + ' ' + board[rownumber][boardsize - 1]
    print(row)

    if rownumber < boardsize - 1:
        print('---|' * (boardsize - 1) + '---')

def printboard(board):
    boardsize = len(board)
    for i in range(boardsize):
        printboardrow(board, i)

def printboardx(board):
    boardsize = len(board)
    for i in range(boardsize):
        row = ''
        for j in range(boardsize - 1):
            row = row + ' ' + board[i][j] + ' ' + '|' 
            
        row = row + ' ' + board[i][j]
        print(row)

        if i < boardsize - 1:
            print('---|' * (boardsize - 1) + '---')

def isvalidinput(board, row, column):
    boardsize = len(board)

    if row > boardsize or row < 1 or column < 1 or column > boardsize:
        return False
    else:
        return True

def getuserinput(board):
    userinput = input('Your turn: ')
    splitinput = userinput.split(' ')
    row = int(splitinput[0])
    column = int(splitinput[1])

    while (not isvalidinput(board, row, column)) or board[row - 1][column - 1] != ' ':
        if not isvalidinput(board, row, column):
            print('Out of range')
        else:
            print('Taken')

        userinput = input('Enter spot: ')
        splitinput = userinput.split(' ')
        row = int(splitinput[0])
        column = int(splitinput[1])

    return [row, column]

def getcomputermove(board):
    #return getnextavailablemove(board)

    # get win move 
    move = getblockmove(board, 'O')
    if move != None:
        return move

    move = getblockmove(board, 'X')
    if move != None:
       return move

    move = getmiddlemove(board)
    if move != None:
        return move

    move = getcornersmove(board) 
    if move != None:
        return move

    move = getnextavailablemove(board)
    return move

def getcornersmove(board):
    boardsize = len(board)
    if board[0][0] == ' ':
        return [1, 1]

    if board[0][boardsize - 1] == ' ':
        return [1, boardsize]        

    if board[boardsize - 1][0] == ' ':
        return [boardsize, 1]

    if board[boardsize - 1][boardsize - 1] == ' ':
        return [boardsize, boardsize]

def getmiddlemove(board):
    boardsize = len(board)
    remainder = boardsize % 2
    if remainder != 0:
        i = (boardsize // 2) + 1
        if board[i - 1][i - 1] == ' ':
            return [i, i]
            
    return None
 
def getblockmove(board, symbol):
    boardsize = len(board)
    #check rows
    
    for i in range(boardsize):
        symbolcount = 0
        blankspace = None
        for j in range(boardsize):
            if board[i][j] == symbol:
                symbolcount += 1
            elif board[i][j] == ' ':
                blankspace = [i + 1, j + 1]

        if symbolcount == boardsize - 1 and blankspace != None:
            return blankspace     
        
    #check columns

    for j in range(boardsize):
        symbolcount = 0
        blankspace = None
        for i in range(boardsize):
            if board[i][j] == symbol:
                symbolcount += 1
            elif board[i][j] == ' ':
                blankspace = [i + 1, j + 1]

        if symbolcount == boardsize - 1 and blankspace != None:
            return blankspace

    #check diagonals
    symbolcount = d2symbolcount = 0
    blankspace = d2blankspace = None

    for i, j in zip(range(boardsize), range(boardsize)):
        if board[i][j] == symbol:
            symbolcount += 1
        elif board[i][j] == ' ':
            blankspace = [i + 1, j + 1]

        d2j = boardsize - 1 - j
        if board[i][d2j] == symbol:
            d2symbolcount += 1
        elif board[i][d2j] == ' ':
            d2blankspace = [i + 1, d2j + 1]                

    if symbolcount == boardsize - 1 and blankspace != None:
        return blankspace

    if d2symbolcount == boardsize - 1 and d2blankspace != None:
        return d2blankspace

    return None

def getnextavailablemove(board):
    boardsize = len(board)
    row = column = -1

    hasemptyspace = False
    for i in range(boardsize):
        for j in range(boardsize):
            if board [i][j] == ' ':
                hasemptyspace = True
                row = i + 1
                column = j + 1
                break

        if hasemptyspace == True:
            break

    if hasemptyspace == False:
        return None
    
    returnlist = [row, column]
    return returnlist





def getrandommove(board):
    boardsize = len(board)
    row = column = -1    

    row = random.randint(1, boardsize)
    column = random.randint(1, boardsize)
    
    while board[row - 1][column - 1] != ' ':
        row = random.randint(1, boardsize)
        column = random.randint(1, boardsize)
    
    if row == -1:
        return None

    returnlist = [row, column]
    return returnlist

def main():

    boardsize = int(input('Enter board size:'))

    board = createboard(boardsize)
    #reset(board)
    gameresult = gameover(board)
    usermove = True

    while gameresult == 0:
        #printboard(board)
        if usermove:
            printboard(board)
            userinput = getuserinput(board)
            row = userinput[0]
            column = userinput[1]
            move = 'X'
            usermove = False
        else:
            computerinput = getcomputermove(board)
            row = computerinput[0]
            column = computerinput[1]
            move = 'O'
            usermove = True

        updateboard(board, row, column, move)
        gameresult = gameover(board)

    printboard(board)

    if gameresult == 1:
        print('You Win! \(^.^)/ ')
    elif gameresult == 2:
        print('You Lose')
    else:
        print('Draw')

def gameover(board):
    # 0 = game still going 1 = X won, 2 = O won, 3 = draw
    hasemptyspace = False
    boardsize = len(board)

    # Check Rows
    for i in range(boardsize):
        xcount = ocount = 0
        for j in range(boardsize):
            if board[i][j] == 'X':
                xcount += 1
            elif board[i][j] == 'O':
                ocount += 1
            elif board[i][j] == ' ':
                hasemptyspace = True
        
        if xcount == boardsize:
            return 1
        if ocount == boardsize:
            return 2

    # Check Columns
    for j in range(boardsize):
        xcount = ocount = 0
        for i in range(boardsize):
            if board[i][j] == 'X':
                xcount += 1
            elif board[i][j] == 'O':
                ocount += 1
            elif board[i][j] == ' ':
                hasemptyspace = True
        
        if xcount == boardsize:
            return 1
        if ocount == boardsize:
            return 2

    # Check Diagonals
    xcount = ocount = 0
    d2xcount = d2ocount = 0
    for i, j in zip(range(boardsize), range(boardsize)):
        if board[i][j] == 'X':
            xcount += 1
        elif board[i][j] == 'O':
            ocount += 1    
        
        d2j = boardsize - 1 - j
        if board[i][d2j] == 'X':
            d2xcount += 1
        elif board[i][d2j] == 'O':
            d2ocount += 1

    if xcount == boardsize or d2xcount == boardsize:
        return 1
    if ocount == boardsize or d2ocount == boardsize:
        return 2   

    # Check for Draw        
    if hasemptyspace == False:
        return 3

    return 0

def updateboard(board, row, column, move):
    #print('updateboard called with', row, column)
    board[row - 1][column - 1] = move

if __name__ == '__main__':
    main()