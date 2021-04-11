import pygame
from copy import deepcopy

class King():

    def __init__(self, screen, color, position):

        self.number = 6

        self.screen = screen
        self.position = position
        self.value = 1000
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_king.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_king.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50

        self.controlled = False
        self.dead = False

        self.board = []

        self.checked = False
        self.first = True
        


    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)

##    def checkForCheck(self, board):
##        if self.color == "White":
##            anti = "Black"
##            aim = -1
##        else:
##            anti = "White"
##            aim = 1
##        for i in range(8):
##            for j in range(8):
##                if board[i][j] == aim*1:
##                    testPiece = Pawn(self.screen, anti, [j, i], self)
##                    if not(i == 1 and aim == -1) and not (i == 6 and aim == 1):
##                        testPiece.first = False
##                elif board[i][j] == aim*2:
##                    testPiece = Knight(self.screen, anti, [j, i], self)
##                elif board[i][j] == aim*3:
##                    testPiece = Bishop(self.screen, anti, [j, i], self)
##                elif board[i][j] == aim*4:
##                    testPiece = Rook(self.screen, anti, [j, i], self)
##                elif board[i][j] == aim*5:
##                    testPiece = Queen(self.screen, anti, [j, i], self)
##                elif board[i][j] == aim*6:
##                    testPiece = King(self.screen, anti, [j, i])
##
##                else:
##                    continue
##
##                if testPiece.number != aim*6:
##                    testPiece.getPossibleMoves(board, False)
##                else:
##                    testPiece.getPossibleMoves(board, False)
##                moves = testPiece.allowed
##
##                for move in moves:
##                    if self.position == move:
##                        #print(self.color, "king is checked")
##                        return True
##
##        #print(self.color, "king is safe")
##        return False
                        



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]
        if x > 0 and board[y][x - 1]*self.number <= 0:
            self.allowed.append([x - 1,y])
        if x > 0 and  y > 0 and board[y - 1][x - 1]*self.number <= 0:
            self.allowed.append([x - 1, y - 1])

        if x > 0 and  y < 7 and board[y + 1][x - 1]*self.number <= 0:
            self.allowed.append([x - 1, y + 1])

        if x < 7 and board[y][x + 1]*self.number <= 0:
            self.allowed.append([x + 1,y])
        if x < 7 and  y > 0 and board[y - 1][x + 1]*self.number <= 0:
            self.allowed.append([x + 1, y - 1])

        if x < 7 and y < 7 and board[y + 1][x + 1]*self.number <= 0:
            self.allowed.append([x + 1, y + 1])

        if y > 0 and board[y - 1][x]*self.number <= 0:
            self.allowed.append([x, y - 1])
        if y < 7 and board[y + 1][x]*self.number <= 0:
            self.allowed.append([x, y + 1])

        
        if self.first and x>1 and x<6:
            if board[y][x+1] == 0 and board[y][x+2] == 0 and board[y][7] == 4*abs(self.number)/self.number:
                self.allowed.append([x+2,y])
            if board[y][x-1] == 0 and board[y][x-2] == 0 and board[y][0] == 4*abs(self.number)/self.number:
                self.allowed.append([x-2,y])
                    

##        attacked_pos = []
##        for i in range(len(pieces)):
##            if pieces[i].color != self.color:
##                pieces[i].getPossibleMoves(board)
##                attacked_pos += pieces[i].allowed
##
##        for move in self.allowed:
##            if move in attacked_pos:
##                self.allowed.remove(move)

##        if isChecking:
##            for move in self.allowed:
##                newBoard = deepcopy(board)
##                newBoard[self.position[1]][self.position[0]] = 0
##                newBoard[move[1]][move[0]] = self.number
##                if self.checkForCheck(newBoard):
##                    self.allowed.remove(move)
            


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 5
        return board


    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board, pieces)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            self.position = pos
            if self.position == [6,7] and self.first:
                for j in range(len(pieces)):
                    if pieces[j].position == [7,7]:
                        pieces[j].position = [5,7]
                        break

            elif self.position == [2,7]  and self.first:
                for j in range(len(pieces)):
                    if pieces[j].position == [0,7]:
                        pieces[j].position = [3,7]
                        break
            elif self.position == [6,0] and self.first:
                for j in range(len(pieces)):
                    if pieces[j].position == [7,0]:
                        pieces[j].position = [5,0]
                        break

            elif self.position == [2,0]  and self.first:
                for j in range(len(pieces)):
                    if pieces[j].position == [0,0]:
                        pieces[j].position = [3,0]
                        break
            
            self.first = False
            return True

        return False


class Queen():

    def __init__(self, screen, color, position, king):

        self.number = 5
        self.king = king

        self.screen = screen
        self.position = position
        self.value = 9
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_queen.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_queen.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50

        self.controlled = False
        self.dead = False


    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]

        xx = x
        yy = y

        while(xx > 0 and board[y][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,y])
            xx -= 1
            if board[y][xx]*self.number != 0:
                break

        while(yy > 0 and board[yy - 1][x]*self.number <= 0):
            self.allowed.append([x,yy - 1])
            yy -= 1
            if board[yy][x]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and board[y][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,y])
            xx += 1
            if board[y][xx]*self.number != 0:
                break

        while(yy < 7 and board[yy + 1][x]*self.number <= 0):
            self.allowed.append([x,yy + 1])
            yy += 1
            if board[yy][x]*self.number != 0:
                break


        xx = x
        yy = y

        while(xx > 0 and yy > 0 and board[yy - 1][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,yy - 1])
            xx -= 1
            yy -= 1
            if board[yy][xx]*self.number != 0:
                break


        xx = x
        yy = y

        while(xx > 0 and yy < 7  and board[yy + 1][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,yy + 1])
            xx -= 1
            yy += 1
            if board[yy][xx]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and yy > 0  and board[yy - 1][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,yy - 1])
            xx += 1
            yy -= 1
            if board[yy][xx]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and yy < 7  and board[yy + 1][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,yy + 1])
            xx += 1
            yy += 1
            if board[yy][xx]*self.number != 0:
                break

        if isChecking:
            for move in self.allowed:
                newBoard = deepcopy(board)
                newBoard[self.position[1]][self.position[0]] = 0
                newBoard[move[1]][move[0]] = self.number
                if self.king.checkForCheck(newBoard):
                    self.allowed.remove(move)


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 4
        return board


    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            self.position = pos
            return True

        return False


class Rook():

    def __init__(self, screen, color, position, king):

        self.number = 4
        self.king = king

        self.screen = screen
        self.position = position
        self.value = 5
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_rook.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_rook.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50

        self.controlled = False
        self.dead = False



    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]

        xx = x
        yy = y

        while(xx > 0 and board[y][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,y])
            xx -= 1
            if board[y][xx]*self.number != 0:
                break

        while(yy > 0 and board[yy - 1][x]*self.number <= 0):
            self.allowed.append([x,yy - 1])
            yy -= 1
            if board[yy][x]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and board[y][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,y])
            xx += 1
            if board[y][xx]*self.number != 0:
                break

        while(yy < 7 and board[yy + 1][x]*self.number <= 0):
            self.allowed.append([x,yy + 1])
            yy += 1
            if board[yy][x]*self.number != 0:
                break

        if isChecking:
            for move in self.allowed:
                newBoard = deepcopy(board)
                newBoard[self.position[1]][self.position[0]] = 0
                newBoard[move[1]][move[0]] = self.number
                if self.king.checkForCheck(newBoard):
                    self.allowed.remove(move)


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 3
        return board


    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            self.position = pos
            return True

        return False


class Bishop():

    def __init__(self, screen, color, position, king):

        self.number = 3
        self.king = king

        self.screen = screen
        self.position = position
        self.value = 3
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_bishop.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_bishop.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50

        self.controlled = False
        self.dead = False


    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]

        xx = x
        yy = y

        while(xx > 0 and yy > 0 and board[yy - 1][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,yy - 1])
            xx -= 1
            yy -= 1
            if board[yy][xx]*self.number != 0:
                break


        xx = x
        yy = y

        while(xx > 0 and yy < 7  and board[yy + 1][xx - 1]*self.number <= 0):
            self.allowed.append([xx - 1,yy + 1])
            xx -= 1
            yy += 1
            if board[yy][xx]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and yy > 0  and board[yy - 1][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,yy - 1])
            xx += 1
            yy -= 1
            if board[yy][xx]*self.number != 0:
                break

        xx = x
        yy = y

        while(xx < 7 and yy < 7  and board[yy + 1][xx + 1]*self.number <= 0):
            self.allowed.append([xx + 1,yy + 1])
            xx += 1
            yy += 1
            if board[yy][xx]*self.number != 0:
                break

        if isChecking:
            for move in self.allowed:
                newBoard = deepcopy(board)
                newBoard[self.position[1]][self.position[0]] = 0
                newBoard[move[1]][move[0]] = self.number
                if self.king.checkForCheck(newBoard):
                    self.allowed.remove(move)


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 2
        return board



    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            
            self.position = pos
            return True

        return False


class Knight():

    def __init__(self, screen, color, position, king):

        self.number = 2
        self.king = king

        self.screen = screen
        self.position = position
        self.value = 3
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_knight.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_knight.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50

        self.controlled = False
        self.dead = False


    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]

        if x > 1 and y < 7 and board[y+1][x-2]*self.number <= 0:
            self.allowed.append([x - 2, y + 1])

        if x > 1 and y > 0 and board[y-1][x-2]*self.number <= 0:
            self.allowed.append([x - 2, y - 1])

        if x < 6 and y < 7 and board[y+1][x+2]*self.number <= 0:
            self.allowed.append([x + 2, y + 1])

        if x < 6 and y > 0 and board[y-1][x+2]*self.number <= 0:
            self.allowed.append([x + 2, y - 1])
            

        if x > 0 and y < 6 and board[y+2][x-1]*self.number <= 0:
            self.allowed.append([x - 1, y + 2])

        if x > 0 and y > 1 and board[y-2][x-1]*self.number <= 0:
            self.allowed.append([x - 1, y - 2])

        if x < 7 and y < 6 and board[y+2][x+1]*self.number <= 0:
            self.allowed.append([x + 1, y + 2])

        if x < 7 and y > 1 and board[y-2][x+1]*self.number <= 0:
            self.allowed.append([x + 1, y - 2])

        if isChecking:
            for move in self.allowed:
                newBoard = deepcopy(board)
                newBoard[self.position[1]][self.position[0]] = 0
                newBoard[move[1]][move[0]] = self.number
                if self.king.checkForCheck(newBoard):
                    self.allowed.remove(move)

        

        
    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            self.position = pos
            return True

        return False


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 1
        return board


class Pawn():

    def __init__(self, screen, color, position, king):

        self.number = 1
        self.king = king

        self.screen = screen
        self.position = position
        self.value = 1
        self.allowed = []
        self.color = color
        self.image = pygame.image.load('images/white_pawn.png')
        if self.color == "Black":
            self.image = pygame.image.load('images/black_pawn.png')
            self.number *= -1
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50
        self.first = True

        self.controlled = False
        self.dead = False


    def update(self, mouse):
        if not self.controlled:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
        else:
            self.rect.centerx = mouse[0]
            self.rect.centery = mouse[1]

    def draw(self):
        self.screen.blit(self.image, self.rect)



    def getPossibleMoves(self, board, isChecking = False):
        self.allowed = []
        x = self.position[0]
        y = self.position[1]

        if self.color == "White":
            if self.first and board[y-1][x]*self.number == 0:
                if board[y-2][x]*self.number == 0:
                    self.allowed.append([x,y-2])
            if y > 0:
                if board[y-1][x]*self.number == 0:
                    self.allowed.append([x,y-1])
                if x < 7 and board[y-1][x+1]*self.number < 0:
                    self.allowed.append([x+1,y-1])
                if x > 0 and board[y-1][x-1]*self.number < 0:
                    self.allowed.append([x-1,y-1])

        else:
            if self.first and board[y+1][x]*self.number == 0:
                if board[y+2][x]*self.number == 0:
                    self.allowed.append([x,y+2])
            if y < 7:
                if board[y+1][x]*self.number == 0:
                    self.allowed.append([x,y+1])
                if x < 7 and board[y+1][x+1]*self.number < 0:
                    self.allowed.append([x+1,y+1])
                if x > 0 and board[y+1][x-1]*self.number < 0:
                    self.allowed.append([x-1,y+1])
        if isChecking:
            for move in self.allowed:
                newBoard = deepcopy(board)
                newBoard[self.position[1]][self.position[0]] = 0
                newBoard[move[1]][move[0]] = self.number
                if self.king.checkForCheck(newBoard):
                    self.allowed.remove(move)
        


    def importPosition(self, board):
        x = self.position[0]
        y = self.position[1]

        board[y][x] = 6
        return board


    def move(self, pos, board, pieces):
        x = pos[0]
        y = pos[1]
        self.getPossibleMoves(board)

        if pos in self.allowed:
            for i in range(len(pieces)):
                if pieces[i].position == pos:
                    pieces[i].dead = True
            self.position = pos
            self.first = False
            return True

        return False



        

        
        
