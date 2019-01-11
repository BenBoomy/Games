#########################################
# ##### ##### ##### ####   #####  ##### #
#   #   #       #   #   #    #    #     #
#   #   ###     #   ####     #    ##### #
#   #   #       #   # #      #        # #
#   #   #####   #   #  #   #####  ##### #
#########################################


##### Import #####

import pygame
import random
from threading import Timer
import time

from Block import Block
from Wall import Wall

##### Initialising #####

all_objects = pygame.sprite.Group()
player_objects = pygame.sprite.Group()
player_blocks = []
bottom_objects = pygame.sprite.Group()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
OLIVE = (128, 128, 0)
CYAN = (0, 255, 255)

##### Functions #####

def list2matrix():
    matrix = [None] * 2

    for i in range(len(matrix)):
        matrix[i] = [None] * 4

    for i in player_blocks:
        matrix[i.y][i.x] = i
    return matrix

def createPiece(colour, pos1, pos2, pos3, pos4):
    block_1 = Block(pos1[0], pos1[1], colour)
    block_2 = Block(pos2[0], pos2[1], colour)
    block_3 = Block(pos3[0], pos3[1], colour)
    block_4 = Block(pos4[0], pos4[1], colour)
    
    player_objects.add(block_1, block_2, block_3, block_4)
    all_objects.add(block_1, block_2, block_3, block_4)
    
    player_blocks.append(block_1)
    player_blocks.append(block_2)
    player_blocks.append(block_3)
    player_blocks.append(block_4)

def down():
    for block in player_blocks:
        block.down()

def turnPiece(matrix, direction):
    global idx
    if direction:
        if idx == 0: #means piece is in right position
            new = zip(matrix[0], matrix[1])
            for row in matrix:
                for item in row:
                    try:
                        print item.rect.y
                    except AttributeError:
                        pass
            print matrix
##            for i in matrix:
##                for j in i:
##                    try:
##                        print matrix[i][j]
##                    except:
##                        print "wassup"
            corner = matrix[0][0]
        elif idx == 2: #means piece is in left position
            corner = matrix[0][3]
        elif idx  == 1: #means piece is in top position
            corner = matrix[0][0]
        elif idx == 3: #means piece is in bottom position
            corner = matrix[0][1]

        if idx == 3:
            idx = 0
        else:
            idx += 1

    if not direction:
        if idx == 0: #means piece is in right position
            corner = matrix[0][0]
        elif idx == 2: #means piece is in left position
            corner = matrix[0][3]
        elif idx  == 1: #means piece is in top position
            corner = matrix[0][0]
        elif idx == 3: #means piece is in bottom position
            corner = matrix[0][1]

        if idx == 1:
            idx = 0
            
        else:
            idx -= 1

def newPiece():
    num = random.randint(1, 7)

    if num == 1:
        createPiece(RED, (0,0), (1,0), (2,0), (3,0))
    elif num == 2:
        createPiece(ORANGE, (0,0), (1,0), (2,0), (2,1))
    elif num == 3:
        createPiece(MAGENTA, (0,0), (0,1), (1,0), (2,0))
    elif num == 4:
        createPiece(BLUE, (0,0), (0,1), (1,0), (1,1))
    elif num == 5:
        createPiece(GREEN, (0,1), (1,0), (1,1), (2,0))
    elif num == 6:
        createPiece(OLIVE, (0,0), (1,0), (1,1), (2,0))
    elif num == 7:
        createPiece(CYAN, (0,0), (1,0), (1,1), (2,1))

def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((600, 1000))
    gameLoop = True
    t1 = 0
    
    global idx
    idx = 0

    right_wall = Wall(550)
    left_wall = Wall(0)
    all_objects.add(right_wall)
    all_objects.add(left_wall)
    
##    newPiece()
##    matrix = list2matrix()

    while gameLoop:
        if len(player_blocks) == 0:
            newPiece()
            matrix = list2matrix()
            
        for block in player_objects:
            if block.rect.y >= 875:
                player_objects.empty()
                bottom_objects.add(block)
                player_blocks[:] = []
                
        #moving piece down automatically
        t = time.time()
        if t - t1 > 1:
            down()
            t1 = t
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                #movement management
                
                if event.key == pygame.K_LEFT:
                    for block in player_blocks:
                        block.left()
                        for block in player_blocks:
                            if block.rect.x < 50:
                                for block in player_blocks:
                                    block.right()
                                    
                elif event.key == pygame.K_RIGHT:
                    for block in player_blocks:
                        block.right()
                        for block in player_blocks:
                            if block.rect.x >= 550:
                                for block in player_blocks:
                                    block.left()
                elif event.key == pygame.K_UP:
                    turnPiece(matrix, True)

                elif event.key == pygame.K_DOWN:
                    turnPiece(matrix, False)
                    
                if event.key == pygame.K_SPACE:
                    down()
        
        all_objects.update()
        screen.fill(BLACK)
        all_objects.draw(screen)
        pygame.display.flip()

main()
