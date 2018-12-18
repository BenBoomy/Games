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

    for row in matrix:
        print row

def newPiece():
    num = random.randint(1, 7)
    
    if num == 1:
        block_1 = Block(0, 0, RED)
        block_2 = Block(1, 0, RED)
        block_3 = Block(2, 0, RED)
        block_4 = Block(3, 0, RED)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
    elif num == 2:
        block_1 = Block(0, 0, ORANGE)
        block_2 = Block(1, 0, ORANGE)
        block_3 = Block(2, 0, ORANGE)
        block_4 = Block(2, 1, ORANGE)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)

    elif num == 3:
        block_1 = Block(0, 0, MAGENTA)
        block_2 = Block(0, 1, MAGENTA)
        block_3 = Block(1, 0, MAGENTA)
        block_4 = Block(2, 0, MAGENTA)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
    elif num == 4:
        block_1 = Block(0, 0, BLUE)
        block_2 = Block(0, 1, BLUE)
        block_3 = Block(1, 0, BLUE)
        block_4 = Block(1, 1, BLUE)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
    elif num == 5:
        block_1 = Block(0, 1, GREEN)
        block_2 = Block(1, 0, GREEN)
        block_3 = Block(1, 1, GREEN)
        block_4 = Block(2, 0, GREEN)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
    elif num == 6:
        block_1 = Block(0, 0, OLIVE)
        block_2 = Block(1, 0, OLIVE)
        block_3 = Block(1, 1, OLIVE)
        block_4 = Block(2, 0, OLIVE)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
    elif num == 7:
        block_1 = Block(0, 0, CYAN)
        block_2 = Block(1, 0, CYAN)
        block_3 = Block(1, 1, CYAN)
        block_4 = Block(2, 1, CYAN)
        player_objects.add(block_1, block_2, block_3, block_4)
        all_objects.add(block_1, block_2, block_3, block_4)
        player_blocks.append(block_1)
        player_blocks.append(block_2)
        player_blocks.append(block_3)
        player_blocks.append(block_4)
        
def main():
    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((550, 900))
    gameLoop = True

    right = Wall(500)
    left = Wall(0)
    all_objects.add(right)
    all_objects.add(left)
    newPiece()
    list2matrix()
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    for block in player_blocks:
                        block.left()
                        for block in player_blocks:
                            if block.rect.x < 50:
                                for block in player_blocks:
                                    block.right()
                elif event.key == pygame.K_RIGHT:
                    print player_blocks
                    for block in player_blocks:
                        block.right()
                        for block in player_blocks:
                            if block.rect.x >= 500:
                                for block in player_blocks:
                                    block.left()
                elif event.key == pygame.K_DOWN:
                    for block in player_blocks:
                        block.down()

        all_objects.update()
        screen.fill(BLACK)
        all_objects.draw(screen)
        pygame.display.flip()

main()
