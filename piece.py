import pygame

class Piece():

    def __init__(self, screen, number, position):
        self.screen = screen
        self.number = number
        self.position = position

        if self.number > 0:
            self.color = "White"
        else:
            self.color = "Black"

        if self.number == 1:
            self.image = pygame.image.load('images/white_pawn.png')
        elif self.number == -1:
            self.image = pygame.image.load('images/black_pawn.png')
        elif self.number == 2:
            self.image = pygame.image.load('images/white_knight.png')
        elif self.number == -2:
            self.image = pygame.image.load('images/black_knight.png')
        elif self.number == 3:
            self.image = pygame.image.load('images/white_bishop.png')
        elif self.number == -3:
            self.image = pygame.image.load('images/black_bishop.png')
        elif self.number == 4:
            self.image = pygame.image.load('images/white_rook.png')
        elif self.number == -4:
            self.image = pygame.image.load('images/black_rook.png')
        elif self.number == 5:
            self.image = pygame.image.load('images/white_queen.png')
        elif self.number == -5:
            self.image = pygame.image.load('images/black_queen.png')
        elif self.number == 6:
            self.image = pygame.image.load('images/white_king.png')
        elif self.number == -6:
            self.image = pygame.image.load('images/black_king.png')
        

            
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]*100 + 50
        self.rect.centery = self.position[1]*100 + 50


        self.controlled = False
        
        self.attackingCells = []
        self.cellToGo = []


    def draw(self, pos):
        if self.controlled:
            self.rect.centerx = pos[0]
            self.rect.centery = pos[1]
        else:
            self.rect.centerx = self.position[0]*100 + 50
            self.rect.centery = self.position[1]*100 + 50
            
        self.screen.blit(self.image, self.rect)


    def move(self, board, pos, stats):
        if pos in self.cellsToGo:
            
            if self.number == 6:
                stats[1] = True

                if pos[0] - self.position[0] == 2:
                    board[7][7] = 0
                    board[7][5] = 4
                    stats[5] = True

                if pos[0] - self.position[0] == -2:
                    board[7][0] = 0
                    board[7][3] = 4
                    stats[4] = True

            if self.number == -6:
                stats[0] = True

                if pos[0] - self.position[0] == 2:
                    board[0][7] = 0
                    board[0][5] = -4
                    stats[3] = True

                if pos[0] - self.position[0] == -2:
                    board[0][0] = 0
                    board[0][3] = -4
                    stats[2] = True

                

            if self.number == 4 and self.position == [7,7]:
                stats[5] = True
            if self.number == 4 and self.position == [0,7]:
                stats[4] = True

            if self.number == -4 and self.position == [7,0]:
                stats[3] = True
            if self.number == -4 and self.position == [0,0]:
                stats[2] = True

            
            if self.number == 1 and pos[1] == 0:
                board[self.position[1]][self.position[0]] = 0
                board[pos[1]][pos[0]] = 5
                self.position = pos
            elif self.number == -1 and pos[1] == 7:
                board[self.position[1]][self.position[0]] = 0
                board[pos[1]][pos[0]] = -5
                self.position = pos
            else:
                board[self.position[1]][self.position[0]] = 0
                board[pos[1]][pos[0]] = self.number
                self.position = pos

            
            
        return board, stats
        
        
