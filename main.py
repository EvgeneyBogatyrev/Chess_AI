import sys
import pygame

from copy import deepcopy

from piece import Piece
from AI import Brain

bgcolor = (230, 230, 230)


pieces = []
turn = "White"

def anti(color):
    if color == "White":
        return "Black"
    return "White"

def draw(screen):
    screen.fill(bgcolor)

    pygame.draw.rect(screen, (200,200,200), (0,0,800,800))

    counter = 0
    for x in range(0,100*8, 100):
        for y in range(0,100*8, 100):
            if counter%2 == 0:
                pygame.draw.rect(screen, (250, 255, 0), (x, y, 100, 100))
            counter += 1
        counter += 1


def transformed(pos):
    cell = []
    pos = list(pos)
    cell.append(pos[0] // 100)
    cell.append(pos[1] // 100)
    return cell


def getAttackingCells(number, board, position):
    allowed = []
    x = position[0]
    y = position[1]
    if abs(number) == 6:
        if x > 0:# and board[y][x - 1]*number <= 0:
            allowed.append([x - 1,y])
        if x > 0 and  y > 0 :#and board[y - 1][x - 1]*number <= 0:
            allowed.append([x - 1, y - 1])

        if x > 0 and  y < 7 :#and board[y + 1][x - 1]*number <= 0:
            allowed.append([x - 1, y + 1])

        if x < 7 :#and board[y][x + 1]*number <= 0:
            allowed.append([x + 1,y])
        if x < 7 and  y > 0 :#and board[y - 1][x + 1]*number <= 0:
            allowed.append([x + 1, y - 1])

        if x < 7 and y < 7 :#and board[y + 1][x + 1]*number <= 0:
            allowed.append([x + 1, y + 1])

        if y > 0:# and board[y - 1][x]*number <= 0:
            allowed.append([x, y - 1])
        if y < 7 :#and board[y + 1][x]*number <= 0:
            allowed.append([x, y + 1])

    #-------------------------------------------------------------------


    elif number == 1:
            if x < 7:
                allowed.append([x+1,y-1])
            if x > 0:
                allowed.append([x-1,y-1])

    elif number == -1:
##        if y == 1 and board[y+1][x]*number == 0:
##            if board[y+2][x]*number == 0:
##                allowed.append([x,y+2])
##        if y < 7:
##            if board[y+1][x]*number == 0:
##                allowed.append([x,y+1])
            if x < 7 :#and board[y+1][x+1]*number < 0:
                allowed.append([x+1,y+1])
            if x > 0 :#and board[y+1][x-1]*number < 0:
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
                print(stats)
                if not wKingMoved and not wrRookMoved and not [5,7] in dangerous and not [6,7] in dangerous and board[7][5] == 0 and board[7][6] == 0:
                    cellsToGo.append([x + 2,y])
                if not wKingMoved and not wlRookMoved and not [3,7] in dangerous and not [2,7] in dangerous and not [1,7] in dangerous and board[7][3] == 0 and board[7][2] == 0 and board[7][1] == 0:
                    cellsToGo.append([x - 2,y])

            if number<0:
                if not bKingMoved and not brRookMoved and not [5,0] in dangerous and not [6,0] in dangerous and board[0][5] == 0 and board[0][6] == 0:
                    cellsToGo.append([x + 2,y])
                if not bKingMoved and not blRookMoved and not [3,0] in dangerous and not [2,0] in dangerous and not [1,0] in dangerous and board[0][3] == 0 and board[0][2] == 0 and board[0][1] == 0:
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
    

        

        

        

    
            
            
        
        

            
            

def runGame():

    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("Chess")


    board = []
    turn = "White"

    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)


    for i in range(8):
        board[1][i] = -1
        board[6][i] = 1

    board[0][0] = -4
    board[0][1] = -2
    board[0][2] = -3
    board[0][3] = -5
    board[0][4] = -6
    board[0][5] = -3
    board[0][6] = -2
    board[0][7] = -4

    board[7][0] = 4
    board[7][1] = 2
    board[7][2] = 3
    board[7][3] = 5
    board[7][4] = 6
    board[7][5] = 3
    board[7][6] = 2
    board[7][7] = 4

    


    oldBoard = []
    bKingMoved = False
    wKingMoved = False
    blRookMoved = False
    brRookMoved = False
    wlRookMoved = False
    wrRookMoved = False

    stats = [bKingMoved, wKingMoved, blRookMoved, brRookMoved, wlRookMoved, wrRookMoved]

    color = "Black"
    brain = Brain(color, 1, screen)

    while(True):

        pos = pygame.mouse.get_pos()

        #-------------------------------------------------------------------

        
        if oldBoard != board:
            pieces = []
            for i in range(8):
                for j in range(8):
                    if i == 0 and board[i][j] == -1:
                        board[i][j] = -5
                    if i == 7 and board[i][j] == 1:
                        board[i][j] = 5
                    if board[i][j] != 0:
                        pieces.append(Piece(screen, board[i][j], [j,i]))
                    if turn == "White" and board[i][j] == 6:
                        kingPos = [j, i]
                    elif turn == "Black" and board[i][j] == -6:
                        kingPos = [j, i]

            oldBoard = deepcopy(board)


            iskingChecked = kingChecked(board, turn)

            


            

        #-----------------------------------------------------------------------

        if turn == color:
            lastBoard = deepcopy(board)
            try:
                if len(pieces) > 12 and not iskingChecked:
                    print("TopTen")
                    board, stats = brain.softCalc(3, board, -1, iskingChecked, kingPos, stats)
                    
                else:
                    print("minimax")
                    board, stats = brain.minimax(4, board, -1, iskingChecked, kingPos, stats)
                if board == "lul":
                    print("minimax correction")
                    board, stats = brain.minimax(4, lastBoard, -1, iskingChecked, kingPos, stats)
            except TypeError:
                print(anti(turn), "won!")
                sys.exit()
                
                
            turn = anti(color)

                


        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(pieces)):
                    if pieces[i].color == turn and pieces[i].rect.collidepoint(pos):
                        pieces[i].controlled = True
                        pieces[i].attackingCells = getAttackingCells(pieces[i].number, board, pieces[i].position)
                        pieces[i].cellsToGo = getCellsToGo(pieces[i].number, board, pieces[i].position, pieces[i].attackingCells, iskingChecked, kingPos, stats)
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                savedBoard = deepcopy(board)
                for i in range(len(pieces)):
                    if pieces[i].controlled:
                        board, stats = pieces[i].move(board, transformed(pos), stats)
                        pieces[i].controlled = False
                        pieces[i].cellsToGo = []
                        break

                if savedBoard != board:
                    turn = anti(turn)


        #---------------------------------------------------------------------


        screen.fill(bgcolor)
        draw(screen)

        for piece in pieces:
            piece.draw(pos)

        pygame.display.flip()
                           
            
                


        




runGame()


