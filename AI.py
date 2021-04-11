from random import random
from copy import deepcopy

from pieces import King
from pieces import Queen
from pieces import Rook
from pieces import Bishop
from pieces import Knight
from pieces import Pawn

def getAttackingCells(number, board, position):
    allowed = []
    x = position[0]
    y = position[1]
    if abs(number) == 6:
        if x > 0:
            allowed.append([x - 1,y])
        if x > 0 and  y > 0 :
            allowed.append([x - 1, y - 1])

        if x > 0 and  y < 7 :
            allowed.append([x - 1, y + 1])

        if x < 7 :
            allowed.append([x + 1,y])
        if x < 7 and  y > 0 :
            allowed.append([x + 1, y - 1])

        if x < 7 and y < 7 :
            allowed.append([x + 1, y + 1])

        if y > 0:
            allowed.append([x, y - 1])
        if y < 7 :
            allowed.append([x, y + 1])

    #-------------------------------------------------------------------


    elif number == 1:
            if x < 7:
                allowed.append([x+1,y-1])
            if x > 0:
                allowed.append([x-1,y-1])

    elif number == -1:

            if x < 7 :
                allowed.append([x+1,y+1])
            if x > 0 :
                allowed.append([x-1,y+1])

    #-------------------------------------------------------------------


    elif abs(number) == 2:


        if x > 1 and y < 7 :#and board[y+1][x-2]*number <= 0:
                allowed.append([x - 2, y + 1])

        if x > 1 and y > 0 :#and board[y-1][x-2]*number <= 0:
            allowed.append([x - 2, y - 1])

        if x < 6 and y < 7 :#and board[y+1][x+2]*number <= 0:
            allowed.append([x + 2, y + 1])

        if x < 6 and y > 0 :#and board[y-1][x+2]*number <= 0:
            allowed.append([x + 2, y - 1])
            

        if x > 0 and y < 6 :#and board[y+2][x-1]*number <= 0:
            allowed.append([x - 1, y + 2])

        if x > 0 and y > 1 :#and board[y-2][x-1]*number <= 0:
            allowed.append([x - 1, y - 2])

        if x < 7 and y < 6 :#and board[y+2][x+1]*number <= 0:
            allowed.append([x + 1, y + 2])

        if x < 7 and y > 1 :#and board[y-2][x+1]*number <= 0:
            allowed.append([x + 1, y - 2])

    #-------------------------------------------------------------------

    elif abs(number) == 3:
        xx = x
        yy = y

        while(xx > 0 and yy > 0):
            allowed.append([xx - 1,yy - 1])
            if board[yy - 1][xx - 1]*number <= 0:
                xx -= 1
                yy -= 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
       


        xx = x
        yy = y

        while(xx > 0 and yy < 7):
            allowed.append([xx - 1,yy + 1])
            if board[yy + 1][xx - 1]*number <= 0:
                xx -= 1
                yy += 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
       

        xx = x
        yy = y

        while(xx < 7 and yy > 0):
            allowed.append([xx + 1,yy - 1])
            if board[yy - 1][xx + 1]*number <= 0:
                xx += 1
                yy -= 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
      

        xx = x
        yy = y

        while(xx < 7 and yy < 7):
            allowed.append([xx + 1,yy + 1])
            if board[yy + 1][xx + 1]*number <= 0:
                xx += 1
                yy += 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break

        
        
    #-------------------------------------------------------------------

    elif abs(number) == 4:
        xx = x
        yy = y

        while(xx > 0):
            allowed.append([xx - 1,y])
            if board[y][xx - 1]*number <= 0:  
                xx -= 1
                if board[y][xx]*number != 0:
                    break
            else:
                break


        while(yy > 0):
            allowed.append([x,yy - 1])
            if board[yy - 1][x]*number <= 0:
                yy -= 1
                if board[yy][x]*number != 0:
                    break
            else:
                break

        xx = x
        yy = y

        while(xx < 7):
            allowed.append([xx + 1,y])
            if board[y][xx + 1]*number <= 0:
                xx += 1
                if board[y][xx]*number != 0:
                    break
            else:
                break

        while(yy < 7):
            allowed.append([x,yy + 1])
            if board[yy + 1][x]*number <= 0:
                yy += 1
                if board[yy][x]*number != 0:
                    break
            else:
                break
    #-------------------------------------------------------------------

    elif abs(number) == 5:
        xx = x
        yy = y

        while(xx > 0):
            allowed.append([xx - 1,y])
            if board[y][xx - 1]*number <= 0:  
                xx -= 1
                if board[y][xx]*number != 0:
                    break
            else:
                break


        while(yy > 0):
            allowed.append([x,yy - 1])
            if board[yy - 1][x]*number <= 0:
                yy -= 1
                if board[yy][x]*number != 0:
                    break
            else:
                break

        xx = x
        yy = y

        while(xx < 7):
            allowed.append([xx + 1,y])
            if board[y][xx + 1]*number <= 0:
                xx += 1
                if board[y][xx]*number != 0:
                    break
            else:
                break

        while(yy < 7):
            allowed.append([x,yy + 1])
            if board[yy + 1][x]*number <= 0:
                yy += 1
                if board[yy][x]*number != 0:
                    break
            else:
                break

        xx = x
        yy = y

        while(xx > 0 and yy > 0):
            allowed.append([xx - 1,yy - 1])
            if board[yy - 1][xx - 1]*number <= 0:
                xx -= 1
                yy -= 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
       


        xx = x
        yy = y

        while(xx > 0 and yy < 7):
            allowed.append([xx - 1,yy + 1])
            if board[yy + 1][xx - 1]*number <= 0:
                xx -= 1
                yy += 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
       

        xx = x
        yy = y

        while(xx < 7 and yy > 0):
            allowed.append([xx + 1,yy - 1])
            if board[yy - 1][xx + 1]*number <= 0:
                xx += 1
                yy -= 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
      

        xx = x
        yy = y

        while(xx < 7 and yy < 7):
            allowed.append([xx + 1,yy + 1])
            if board[yy + 1][xx + 1]*number <= 0:
                xx += 1
                yy += 1
                if board[yy][xx]*number != 0:
                    break
            else:
                break
        
        
            

    return allowed


def getCellsToGo(number, board, position, attackingCells, iskingChecked, kingPos, stats):
    
    bKingMoved, wKingMoved, blRookMoved, brRookMoved, wlRookMoved, wrRookMoved = stats[0], stats[1], stats[2], stats[3], stats[4], stats[5]

    cellsToGo = []
    
    for move in attackingCells:
        if board[move[1]][move[0]]*number <= 0:
            cellsToGo.append(move)

    antiCellsToGo = []


    #----------------------------------------------------
    x = position[0]
    y = position[1]
            
    if number == 1:
        for move in attackingCells:
            if board[move[1]][move[0]]*number >= 0:
                antiCellsToGo.append(move)
            
        
        if y == 6 and board[y-1][x]*number == 0:
            if board[y-2][x]*number == 0:
                cellsToGo.append([x,y-2])
        if y > 0:
            if board[y-1][x]*number == 0:
                cellsToGo.append([x,y-1])

##        if y == 3 and board[y][x-1] == -1 and board[y-1][x-1] == 0:
##            cellsToGo.append([x-1,y-1])
##        if y == 3 and board[y][x+1] == -1 and board[y-1][x+1] == 0:
##            cellsToGo.append([x+1,y-1])

        

    elif number == -1:
        for move in attackingCells:
            if board[move[1]][move[0]]*number >= 0:
                antiCellsToGo.append(move)
        if y == 1 and board[y+1][x]*number == 0:
            if board[y+2][x]*number == 0:
                cellsToGo.append([x,y+2])
        if y > 0:
            if board[y+1][x]*number == 0:
                cellsToGo.append([x,y+1])

##        if y == 4 and board[y][x-1] == 1:# and board[y+1][x-1] == 0:
##            cellsToGo.append([x-1,y+1])
##        if y == 4 and board[y][x+1] == 1:# and board[y+1][x+1] == 0:
##            cellsToGo.append([x+1,y+1])
        
    elif abs(number) == 6:                   
            
        dangerous = []
        
        for i in range(8):
            for j in range(8):
                if board[i][j]*number < 0:
                    dangerous += getAttackingCells(board[i][j], board, [j,i])

        for move in attackingCells:
            if move in dangerous:
                antiCellsToGo.append(move)

        if not iskingChecked:
            if number>0:
                #print(board[7][7], board[7][0], board[0][7], board[0][0])
                if not wKingMoved and not wrRookMoved and not [5,7] in dangerous and not [6,7] in dangerous and board[7][5] == 0 and board[7][6] == 0:# and board[7][7] == 4:
                    cellsToGo.append([x + 2,y])
                if not wKingMoved and not wlRookMoved and not [3,7] in dangerous and not [2,7] in dangerous and not [1,7] in dangerous and board[7][3] == 0 and board[7][2] == 0 and board[7][1] == 0:# and board[7][0] == 4:
                    cellsToGo.append([x - 2,y])

            if number<0:
                if not bKingMoved and not brRookMoved and not [5,0] in dangerous and not [6,0] in dangerous and board[0][5] == 0 and board[0][6] == 0:#  and board[0][7] == -4:
                    cellsToGo.append([x + 2,y])
                if not bKingMoved and not blRookMoved and not [3,0] in dangerous and not [2,0] in dangerous and not [1,0] in dangerous and board[0][3] == 0 and board[0][2] == 0 and board[0][1] == 0:# and board[0][0] == -4:
                    cellsToGo.append([x - 2,y])
                


    
    if iskingChecked or bentWithKing(kingPos, position, board):
        for move in cellsToGo:
            newBoard = deepcopy(board)
            newBoard[move[1]][move[0]] = number
            newBoard[position[1]][position[0]] = 0

            color = "White"
            if number < 0:
                color = "Black"

            if kingChecked(newBoard, color):
                antiCellsToGo.append(move)
            

    


        
                        
    returned = []
    for cell in cellsToGo:
        if not cell in antiCellsToGo:
            returned.append(cell)
            
        
    return returned


def kingChecked(board, color):
    position = [-1,-1]
    if color == "White":
        dangerous = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == 6:
                    position = [j, i]
                

                if board[i][j] < 0:
                    dangerous += getAttackingCells(board[i][j], board, [j,i])

        if position in dangerous:
            return True
        else:
            return False
    else:
        dangerous = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == -6:
                    position = [j, i]
                

                if board[i][j] > 0:
                    dangerous += getAttackingCells(board[i][j], board, [j,i])

        if position in dangerous:
            return True
        else:
            return False

    


def bentWithKing(kingPos, position, board):
    if kingPos in getAttackingCells(5, board, position):
        return True
    return False
    

        

def positionValue(number, x, y, update = False):
    if number == 2:
        board = [
                [-5, -4, -3, -3, -3, -3, -4, -5],
                [-4, -2, 0, 0, 0, 0, -2, -4],
                [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
                [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
                [-3, 0, 1.5, 2, 2, 1.5, 0, -3],
                [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
                [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
                [-5, -1, -3, -3, -3, -3, -1, -5]
            ]
    if number == -2:
        board = [
                [-5, -1, -3, -3, -3, -3, -1, -5],
                [-4, -2, 0, 0.5, 0.5, 0, -2, -4],
                [-3, 0.5, 1, 1.5, 1.5, 1, 0.5, -3],
                [-3, 0, 1.5, 2, 2, 1.5, 0, -3],
                [-3, 0.5, 1.5, 2, 2, 1.5, 0.5, -3],
                [-3, 0, 1, 1.5, 1.5, 1, 0, -3],
                [-4, -2, 0, 0, 0, 0, -2, -4],
                [-5, -4, -3, -3, -3, -3, -4, -5]
            ]

    elif number == 1:
        board = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [5 ,5, 5, 5, 5, 5, 5, 5],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [0.5, 0.5, 1, 2.5, 2.5, 1.0, 0.5, 0.5],
                [0, 0, 0, 2, 2, 0, 0, 0],
                [0.5, -0.5, -1, -1, 0, -1, -0.5, 0.5],
                [0.5, 1, 1, -2, -2, 1, 1, 0.5],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]

    elif number == -1:
        board = [                                                  
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0.5, 1, 1, -2, -2, 1, 1, 0.5],
                [0.5, -0.5, -1, -1, 0, -1, -0.5, 0.5],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0.5, 0.5, 1, 2.5, 2.5, 1.0, 0.5, 0.5],
                [1, 1, 2, 3, 3, 2, 1, 1],
                [5 ,5, 5, 5, 5, 5, 5, 5],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]

    elif number == 3:
        board = [
                [-2, -1, -1, -1, -1, -1, -1, -2],
                [-1, 0, 0, 0, 0, 0, 0, -1],
                [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
                [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
                [-1, 0, 1, 1, 1, 1, 0, -1],
                [-1, 1, 1, 1, 1, 1, 1, -1],
                [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
                [-2, -1, -1, -1, -1, -1, -1, -2]
            ]

    elif number == -3:
        board = [                                      
                [-2, -1, -1, -1, -1, -1, -1, -2],
                [-1, 0.5, 0, 0, 0, 0, 0.5, -1],
                [-1, 1, 1, 1, 1, 1, 1, -1],
                [-1, 0, 1, 1, 1, 1, 0, -1],
                [-1, 0.5, 0.5, 1, 1, 0.5, 0.5, -1],
                [-1, 0, 0.5, 1, 1, 0.5, 0, -1],
                [-1, 0, 0, 0, 0, 0, 0, -1],
                [-2, -1, -1, -1, -1, -1, -1, -2]
            ]
    elif number == 4:
        board = [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0.5, 1, 1, 1, 1, 1, 1, 0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [0, 0, 0, 0.5, 0.5, 0, 0, 0]
            ]

    elif number == -4:
        board = [
                [0, 0, 0, 0.5, 0.5, 0, 0, 0],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [-0.5, 0, 0, 0, 0, 0, 0, -0.5],
                [0.5, 1, 1, 1, 1, 1, 1, 0.5],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]

    elif number == 5:
        board = [
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                [-1, 0, 0, 0, 0, 0, 0, -1],
                [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-1, 0, 0.5, 0, 0, 0, 0, -1],
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2]
            ]

    elif number == -5:
        board = [
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2],
                [-1, 0, 0, 0, 0, 0, 0, -1],
                [-1, 0, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-0.5, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [0, 0, 0.5, 0.5, 0.5, 0.5, 0, -0.5],
                [-1, 0.5, 0.5, 0.5, 0.5, 0.5, 0, -1],
                [-1, 0, 0.5, 0, 0, 0, 0, -1],
                [-2, -1, -1, -0.5, -0.5, -1, -1, -2]
            ]
    elif number == 6:
        board = [
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-2, -3, -3, -4, -4, -3, -3, -2],
                [-2, -3, -3, -4, -4, -3, -3, -2],
                [2, 2, 0, 0, 0, 0, 2, 2],
                [2, 3 ,5, -1, 0, -1, 5, 2]
            ]
        if update:
            board = [
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, 1, 1, 0, 0, 1, 1, -3],
                [-3, 1, 1, 0, 0, 1, 1, -3],
                [-2, 1, 1, 0, 0, 1, 1, -2],
                [-2, 0, 0, 0, 0, 0, 0, 0],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-2, -2 ,2, -2, -2, -2, -2, -2]
            ]

    elif number == -6:
        board = [
                [2, 3, 5, -1, 0, -1, 5, 2],
                [2, 3 ,0, 0, 0, 0, 3, 2],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-2, -3, -3, -4, -4, -3, -3, -2],
                [-2, -3, -3, -4, -4, -3, -3, -2]
                
            ]
        if update:
            board = [
                [-2, -2 ,2, -2, -2, -2, -2, -2]
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-2, 0, 0, 0, 0, 0, 0, 0],
                [-2, 1, 1, 0, 0, 1, 1, -2],
                [-3, 1, 1, 0, 0, 1, 1, -3],
                [-3, 1, 1, 0, 0, 1, 1, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
                [-3, -4, -4, -5, -5, -4, -4, -3],
            ]
    elif number == 0:
        return 0

    sign = 1
    if number < 0:
        sign = -1

    return board[y][x]*sign/3

    

    

    
        



def calcBalance(board, color, checked = False, update = False):
    balance = 0
    
    for i in range(8):
        for j in range(8):
            if board[i][j] == -6:
                balance -= 99
            elif board[i][j] == -5:
                balance -= 9
            elif board[i][j] == -4:
                balance -= 5
            elif board[i][j] == -3:
                balance -= 3
            elif board[i][j] == -2:
                balance -= 3
            elif board[i][j] == -1:
                balance -= 1
            elif board[i][j] == 1:
                balance += 1
            elif board[i][j] == 2:
                balance += 3
            elif board[i][j] == 3:
                balance += 3
            elif board[i][j] == 4:
                balance += 5
            elif board[i][j] == 5:
                balance += 9
            elif board[i][j] == 6:
                balance += 99
                
                

    for i in range(8):
        for j in range(8):
            balance += positionValue(board[i][j], j, i, update)

    if checked:
        if color == "White":
            balance += 3
        else:
            balance -= 3


##    balance -= (whiteInRow/2)**2
##    balance += (blackInRow/2)**2

    return balance   
    

    

class Brain():

    def __init__(self, color, depth, screen):

        self.color = color
        self.desiredValue = 9999
        if self.color == "Black":
            self.desiredValue = -9999

        self.depth = depth
        self.balance = 0

        self.screen = screen
        self.turn = 0

    def softCalc(self, depth, board, desire, isChecked, kingPos, stats, original = True):
        statsCopy = deepcopy(stats)
        if original:
            self.turn += 1
            
        statsCopy = deepcopy(stats)
        if depth == 0:
            if desire > 0:
                color = "Black"
            else:
                color = "White"
            return calcBalance(board, color), []

        

        else:
            if desire < 0:
                color = "Black"
                value = 9999                
                
            else:
                color = "White"
                value = -9999
                                
                
            
            boards = []
            for i in range(8):
                for j in range(8):
                    if board[i][j]*desire > 0:
                        attack = getAttackingCells(board[i][j], board, [j, i])
                        moves = getCellsToGo(board[i][j], board, [j, i], attack, isChecked, kingPos, stats)

                       

                        for move in moves:
                            newBoard = deepcopy(board)
                            newBoard[i][j] = 0
                            newBoard[move[1]][move[0]] = board[i][j]
                            if board[i][j] == 6:
                                #stats[1] = True
                                if move[0] - j == 2:
                                    newBoard[7][5] = 4
                                    newBoard[7][7] = 0
                                    #stats[5] = True
                                if move[0] - j == -2:
                                    newBoard[7][0] = 0
                                    newBoard[7][3] = 4
                                    #stats[4] = True
                            if board[i][j] == -6:
                                #stats[0] = True
                                if move[0] - j == 2:
                                    newBoard[0][5] = -4
                                    newBoard[0][7] = 0
                                    #stats[3] = True
                                if move[0] - j == -2:
                                    newBoard[0][0] = 0
                                    newBoard[0][3] = -4
                                    #stats[2] = True

                            if board[i][j] == 1 and move[1] == 0:
                                newBoard[move[1]][move[0]] = 5
                            if board[i][j] == -1 and move[1] == 7:
                                newBoard[move[1]][move[0]] = -5

                            if self.color == "White":
                                extra = 1
                            else:
                                extra = -1
                        
                            
                            boards.append(newBoard)

            if not original and len(boards) == 0:
                return -9999*desire, stats

            if color == "Black":
                reverse = False
            else:
                reverse = True
            if color == "White":
                anticolor = "Black"
            else:
                anticolor = "White"
            top = sorted(boards, key = lambda x : calcBalance(x, color, kingChecked(x, anticolor)), reverse = reverse)
            topTen = []
            for i in range(min(10,len(top))):
                topTen.append(top[i])
            #print(topTen[0])
            if depth == 0:
                isChAnti = kingChecked(board, anticolor)
                if topTen[0][7][6] == 6 and stats[1] == False:
                    stats[1] = True
                    stats[5] = True
                if topTen[0][7][1] == 6 and stats[1] == False:
                    stats[1] = True
                    stats[4] = True
                if topTen[0][0][6] == -6 and stats[0] == False:
                    stats[0] = True
                    stats[3] = True
                if topTen[0][0][1] == -6 and stats[0] == False:
                    stats[0] = True
                    stats[2] = True
                return calcBalance(topTen[0], color, isChAnti), stats
            else:
                bestBoard = []
                for i in range(min(10,len(top))):
                    isChAnti = kingChecked(topTen[i], anticolor)
                    a, statsCopy = self.softCalc(depth - 1, topTen[i], desire*(-1), isChAnti, kingPos, stats, False)
                    if a*desire > value*desire:
                        value = a
                        bestBoard = topTen[i]
                    #print(bestBoard)
                if original:
                    if not bestBoard == []:
                        if bestBoard[7][6] == 6 and stats[1] == False:
                            stats[1] = True
                            stats[5] = True
                        if bestBoard[7][1] == 6 and stats[1] == False:
                            stats[1] = True
                            stats[4] = True
                        if bestBoard[0][6] == -6 and stats[0] == False:
                            stats[0] = True
                            stats[3] = True
                        if bestBoard[0][1] == -6 and stats[0] == False:
                            stats[0] = True
                            stats[2] = True
                        return bestBoard, stats
                    return "lul", stats
                return value, stats
            
                
            
                            
##                            if (balancePrev - balanceNow)*desire > min(self.turn, 10):
##                                values.append(-10*desire)
##                            else:
##                                
##                                if color == "White":
##                                    anticolor = "Black"
##                                else:
##                                    anticolor = "White"
##                                isChAnti = kingChecked(newBoard, anticolor)
##                                a, [] = self.minimax(depth - 1, newBoard, desire*(-1), isChAnti, kingPos, stats, False, value)
##                                values.append(a)
##                            
##                            if not point == -0.69:
##                                if desire > 0:
##                                    if values[-1] > point:
##                                        return point, []
##                                elif desire < 0:
##                                    if values[-1] < point:
##                                        return point, []
##
##                            
##                            value = values[-1]
##                            
##
##
##
##
##
##            if not original:
##                if desire > 0:
##                    if len(values) == 0:
##                        return -99999, []
##                    return max(values), []
##                else:
##                    if len(values) == 0:
##                        return 99999, []
##                    return min(values), []
##
##            else:
##                if desire > 0:
##                    if len(values) == 0:
##                        result = -99999
##                    else:
##                        result =  max(values)
##                else:
##                    if len(values) == 0:
##                        result = 99999
##                    else:
##                        result = min(values)
##
##
##
##            for i in range(len(values)):
##                if values[i] == result:
##                    board, newStats = self.calculateMove(i, board, desire, isChecked, kingPos, statsCopy)
##                    return board, newStats

    def minimax(self, depth, board, desire, isChecked, kingPos, stats, original = True, point = -0.69):
        if original:
            self.turn += 1
            
        statsCopy = deepcopy(stats)
        if depth == 0:
            if desire > 0:
                color = "Black"
            else:
                color = "White"
            return calcBalance(board, color, False, True), []

        

        else:
            if desire < 0:
                color = "Black"
                value = 9999                
                
            else:
                color = "White"
                value = -9999
                                
                
            values = []
            balancePrev = calcBalance(board, color)
            for i in range(8):
                for j in range(8):
                    if board[i][j]*desire > 0:
                        attack = getAttackingCells(board[i][j], board, [j, i])
                        moves = getCellsToGo(board[i][j], board, [j, i], attack, isChecked, kingPos, stats)

                        for move in moves:
                            newBoard = deepcopy(board)
                            newBoard[i][j] = 0
                            newBoard[move[1]][move[0]] = board[i][j]
                            if board[i][j] == 6:
                                stats[1] = True
                                if move[0] - j == 2:
                                    newBoard[7][5] = 4
                                    newBoard[7][7] = 0
                                    stats[5] = True
                                if move[0] - j == -2:
                                    newBoard[7][0] = 0
                                    newBoard[7][3] = 4
                                    stats[4] = True
                            if board[i][j] == -6:
                                stats[0] = True
                                if move[0] - j == 2:
                                    newBoard[0][5] = -4
                                    newBoard[0][7] = 0
                                    stats[3] = True
                                if move[0] - j == -2:
                                    newBoard[0][0] = 0
                                    newBoard[0][3] = -4
                                    stats[2] = True

##                            if board[i][j] == 1:
##                                newBoard[move[1]][move[0]] = 5
##                            if board[i][j] == -1:
##                                newBoard[move[1]][move[0]] = -5

                            if self.color == "White":
                                extra = 1
                            else:
                                extra = -1
                        
                            
                            balanceNow = calcBalance(newBoard, color)
                            if (balancePrev - balanceNow)*desire > min(self.turn, 10):
                                values.append(-10*desire)
                            else:
                                if color == "White":
                                    anticolor = "Black"
                                else:
                                    anticolor = "White"
                                isChAnti = kingChecked(newBoard, anticolor)
                                a, [] = self.minimax(depth - 1, newBoard, desire*(-1), isChAnti, kingPos, stats, False, value)
                                values.append(a)
                            
                            if not point == -0.69:
                                if desire > 0:
                                    if values[-1] > point:
                                        return point, []
                                elif desire < 0:
                                    if values[-1] < point:
                                        return point, []

                            
                            value = values[-1]
                            





            if not original:
                if desire > 0:
                    if len(values) == 0:
                        return -99999, []
                    return max(values), []
                else:
                    if len(values) == 0:
                        return 99999, []
                    return min(values), []

            else:
                if desire > 0:
                    if len(values) == 0:
                        result = -99999
                    else:
                        result =  max(values)
                else:
                    if len(values) == 0:
                        result = 99999
                    else:
                        result = min(values)



            for i in range(len(values)):
                if values[i] == result:
                    board, newStats = self.calculateMove(i, board, desire, isChecked, kingPos, statsCopy)
                    print(statsCopy)
                    return board, newStats
                
                

    def calculateMove(self, number, board, desire, isChecked, kingPos, stats):
        color = self.color
        counter = 0
        
       
        for i in range(8):
            for j in range(8):
                if board[i][j]*desire > 0:
                    attack = getAttackingCells(board[i][j], board, [j, i])
                    moves = getCellsToGo(board[i][j], board, [j, i], attack, isChecked, kingPos, stats)

                    for move in moves:
                        if counter < number:
                            counter += 1
                        else:
                            newBoard = deepcopy(board)
                            newBoard[i][j] = 0
                            newBoard[move[1]][move[0]] = board[i][j]
                            if board[i][j] == 6:
                                stats[1] = True
                                if move[0] - j == 2:
                                    newBoard[7][5] = 4
                                    newBoard[7][7] = 0
                                    stats[5] = True
                                if move[0] - j == -2:
                                    newBoard[7][0] = 0
                                    newBoard[7][3] = 4
                                    stats[4] = True
                            if board[i][j] == -6:
                                stats[0] = True
                                if move[0] - j == 2:
                                    newBoard[0][5] = -4
                                    newBoard[0][7] = 0
                                    stats[3] = True
                                if move[0] - j == -2:
                                    newBoard[0][0] = 0
                                    newBoard[0][3] = -4
                                    stats[2] = True

                            if board[i][j] == 1 and move[1] == 0:
                                newBoard[move[1]][move[0]] = 5
                            if board[i][j] == -1 and move[1] == 7:
                                newBoard[move[1]][move[0]] = -5

                            return newBoard, stats

        return board, stats
                
                            
                            
                


    def doMove(self, board, pieces, number):
        counter = 0
        color = "Black"

        for i in range(len(pieces)):
            if not pieces[i].dead and pieces[i].color == color:
                pieces[i].getPossibleMoves(board)
                moves = pieces[i].allowed
                for move in moves:
                    if counter >= number:
                        pieces[i].move(move, board, pieces)
                        return pieces
                    else:
                        counter += 1

        return pieces, [lastBlackPiece, lastWhitePiece, whiteInRow, blackInRow]
            
                
                        
            


    def analizeBoardBlack(self, board, pieces, balance=-0.6, returnplz=False, maximum = 0):
        if balance == -0.6:
            balance = self.balance
        testPiece = Pawn(self.screen, "Black", [0, 0])
        self.color = "Black"
        boards = []
        values = []
        for i in range(8):
            for j in range(8):
                if board[i][j] < 0:
                    if board[i][j] == -1:
                        testPiece = Pawn(self.screen, self.color, [j, i])
                        if i != 1:
                            testPiece.first = False
                    elif board[i][j] == -2:
                        testPiece = Knight(self.screen, self.color, [j, i])
                    elif board[i][j] == -3:
                        testPiece = Bishop(self.screen, self.color, [j, i])
                    elif board[i][j] == -4:
                        testPiece = Rook(self.screen, self.color, [j, i])
                    elif board[i][j] == -5:
                        testPiece = Queen(self.screen, self.color, [j, i])
                    elif board[i][j] == -6:
                        testPiece = King(self.screen, self.color, [j, i])


                    testPiece.getPossibleMoves(board)
                    

                    for k in range(len(testPiece.allowed)):
                        if not returnplz:
                            newBoard = deepcopy(board)
                            newBoard[testPiece.position[1]][testPiece.position[0]] = 0
                        if board[testPiece.allowed[k][1]][testPiece.allowed[k][0]] != 0:
                            n = board[testPiece.allowed[k][1]][testPiece.allowed[k][0]]
                            if n == 1:
                                values.append(balance-1)
                            elif n == 2:
                                values.append(balance-3)
                            elif n == 3:
                                values.append(balance-3)
                            elif n == 4:
                                values.append(balance-5)
                            elif n == 5:
                                values.append(balance-9)
                            elif n == 6:
                                values.append(balance-9999)

                        else:
                            values.append(balance-0)
        
                        if not returnplz:
                            values[-1] += positionValue(testPiece.number, testPiece.allowed[k][0], testPiece.allowed[k][1])

                        if not returnplz:
                            newBoard[testPiece.allowed[k][1]][testPiece.allowed[k][0]] = testPiece.number

                            boards.append(newBoard)
                        
                        if returnplz and values[-1] < maximum:
                            return maximum
                            
                            
                    
                        
        
        if returnplz:
            return min(values)
        minimum = 999999
        for i in range(len(values)):
            values[i] = self.analizeBoardWhite(boards[i], pieces, values[i], minimum)
            minimum = values[i]
            print(minimum)

        

        
            
                        

        winner = min(values)
        number = 0
        
        for i in range(len(values)):
            if values[i] == winner:
                number = i
                break

        print(winner)
        return self.calculateMove(number, board, pieces)


    def analizeBoardWhite(self, board, pieces, balance, minimum):
        testPiece = Pawn(self.screen, "White", [0, 0])
        boards = []
        values = []
        self.color = "White"
        for i in range(8):
            for j in range(8):
                if board[i][j] > 0:
                    if board[i][j] == 1:
                        testPiece = Pawn(self.screen, self.color, [j, i])
                        if i != 6:
                            testPiece.first = False
                    elif board[i][j] == 2:
                        testPiece = Knight(self.screen, self.color, [j, i])
                    elif board[i][j] == 3:
                        testPiece = Bishop(self.screen, self.color, [j, i])
                    elif board[i][j] == 4:
                        testPiece = Rook(self.screen, self.color, [j, i])
                    elif board[i][j] == 5:
                        testPiece = Queen(self.screen, self.color, [j, i])
                    elif board[i][j] == 6:
                        testPiece = King(self.screen, self.color, [j, i])


                    testPiece.getPossibleMoves(board)
                    

                    for k in range(len(testPiece.allowed)):
                        newBoard = deepcopy(board)
                        newBoard[testPiece.position[1]][testPiece.position[0]] = 0
                        if board[testPiece.allowed[k][1]][testPiece.allowed[k][0]] != 0:
                            n = newBoard[testPiece.allowed[k][1]][testPiece.allowed[k][0]]
                            if n == -1:
                                values.append(balance+1)
                            elif n == -2:
                                values.append(balance+3)
                            elif n == -3:
                                values.append(balance+3)
                            elif n == -4:
                                values.append(balance+5)
                            elif n == -5:
                                values.append(balance+9)
                            elif n == -6:
                                values.append(balance+9999)

                        else:
                            values.append(self.balance+0)

                        #values[-1] += positionValue(testPiece.number, testPiece.allowed[k][0], testPiece.allowed[k][1])

                        if values[-1] > minimum:
                            return minimum
                            
                            
                        newBoard[testPiece.allowed[k][1]][testPiece.allowed[k][0]] = testPiece.number

                        boards.append(newBoard)

        maximum = -999999
            
        for i in range(len(values)):
            values[i] = self.analizeBoardBlack(boards[i], pieces, values[i], True, maximum)
            maximum = values[i]

        winner = maximum
        
        return winner
##        number = 0
##        
##        for i in range(len(values)):
##            if values[i] == winner:
##                number = i
##                break
##        return self.calculateMove(number, board, pieces)



    



        return pieces



                        

        


        
                    



