########################################
#
# ##### ##### ##### ####   #####  ##### #
#   #   #       #   #   #    #    #     #
#   #   ###     #   ####     #    ##### #
#   #   #       #   # #      #        # #
#   #   #####   #   #  #   #####  ##### #
#########################################



##### Imports #####

import pygame as pg
import random
import time as t

##### Groups n Shit #####
all_sprites = pg.sprite.Group()
player_sprites = pg.sprite.Group()
bottom_sprites = pg.sprite.Group()

##### Colours #####

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
OLIVE = (112, 130, 56)
CYAN = (0, 255, 255)

##### Classes and Functions #####

from Block import *
from Wall import *
from Bottom import *

##class Wall(pg.sprite.Sprite):
##
##   def __init__(self, x):
##
##      pg.sprite.Sprite.__init__(self)
##      self.image = pg.Surface((100, 800))
##      self.image.fill(WHITE)
##
##      self.rect = self.image.get_rect()
##      self.rect.x = x
##      self.rect.y = 0
##
##      all_sprites.add(self)
##
##class Bottom(pg.sprite.Sprite):
##
##   def __init__(self, colour):
##
##       pg.sprite.Sprite.__init__(self)
##       self.image = pg.Surface((600, 100))
##       self.image.fill(colour)
##
##       self.rect = self.image.get_rect()
##       self.rect.x = 0
##       self.rect.y = 800
##
##       all_sprites.add(self)
##       bottom_sprites.add(self)
##
##class Block(pg.sprite.Sprite):
##
##    def __init__(self, x, y, colour):
##
##        pg.sprite.Sprite.__init__(self)
##        self.image = pg.Surface((length, length))
##
##        self.image.fill(colour)
##
##        self.rect = self.image.get_rect()
##        self.rect.x = x + 100
##        self.rect.y = y
##
##        self.x = x
##        self.y = y
##        all_sprites.add(self)
##        player_sprites.add(self)
##
##    def left(self):
##        self.rect.x -= length
##        for sprite in player_sprites:
##           if sprite.rect.x < 100:
##              for sprite in player_sprites:
##                 sprite.rect.x += length
##                 
##    def right(self):
##        self.rect.x += length
##        for sprite in player_sprites:
##           if sprite.rect.x + length > scrn_width - 100:
##              for sprite in player_sprites:
##                 sprite.rect.x -= length
##
##    def down(self):
##        self.rect.y += length
        
def tetramino():
   new_piece = random.randint(0,6)

   if new_piece == 0:
      block_1 = Block(0, 0, RED)
      block_2 = Block(length, 0, RED)
      block_3 = Block(2 * length, 0, RED)
      block_4 = Block(3 * length, 0, RED)
      
   if new_piece == 1:
      block_1 = Block(0, 0, ORANGE)
      block_2 = Block(length, 0, ORANGE)
      block_3 = Block(2 * length, 0, ORANGE)
      block_4 = Block(2 * length, length, ORANGE)
      
   if new_piece == 2:
      block_1 = Block(0, 0, MAGENTA)
      block_2 = Block(0, length, MAGENTA)
      block_3 = Block(length, 0, MAGENTA)
      block_4 = Block(2 * length, 0, MAGENTA)
      
   if new_piece == 3:
      block_1 = Block(0, 0, BLUE)
      block_2 = Block(0, length, BLUE)
      block_3 = Block(length, 0, BLUE)
      block_4 = Block(length, length, BLUE)
      
   if new_piece == 4:
      block_1 = Block(0, length, GREEN)
      block_2 = Block(length, 0, GREEN)
      block_3 = Block(length, length, GREEN)
      block_4 = Block(2 * length, 0, GREEN)
      
   if new_piece == 5:
      block_1 = Block(0, 0, OLIVE)
      block_2 = Block(length, 0, OLIVE)
      block_3 = Block(length, length, OLIVE)
      block_4 = Block(2 * length, 0, OLIVE)
      
   if new_piece == 6:
      block_1 = Block(0, 0, CYAN)
      block_2 = Block(length, 0, CYAN)
      block_3 = Block(length, length, CYAN)
      block_4 = Block(2 * length, length, CYAN)

   player_sprites.add(block_1, block_2, block_3, block_4)
   all_sprites.add(block_1, block_2, block_3, block_4)
      
def contact():
    if pg.sprite.groupcollide(player_sprites, bottom_sprites, False, False):
        for sprite in player_sprites:
            sprite.rect.y -= length
            player_sprites.remove(sprite)
            bottom_sprites.add(sprite)
        tetramino()
            
def down():
    collision = False
    if not collision:
        for sprite in player_sprites:
            sprite.rect.y += length            

def rotate():
   x1 = 500
   y1 = 800
   x2 = 0
   y2 = 0
   
   for sprite in player_sprites:
      if sprite.rect.x < x1:
         x1 = sprite.rect.x
      if sprite.rect.x > x2:
         x2 = sprite.rect.x
         
      if sprite.rect.y < y1:
         all_sprites.add(self)
         y1 = sprite.rect.y
      if sprite.rect.y > y2:
         y2 = sprite.rect.y

   point_1 = [x1, y1]
   point_2 = [x2, y2]

   for point in player_sprites:
      point.rect.x 

   

##### Init #####
       
pg.init()
scrn_width = 600
scrn_height = 900
length = 20
gameLoop = True
clock = pg.time.Clock()
start_time = 0
previous = 0

screen = pg.display.set_mode((scrn_width, scrn_height))
pg.display.init()

left_wall = Wall(0)
right_wall = Wall(500)
bottom = Bottom(WHITE)
bottom_sprites.add(bottom)
all_sprites.add(left_wall, right_wall, bottom)

tetramino()

while gameLoop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameLoop = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_BACKSPACE:
                    gameLoop = False
            #movement handling
            elif event.key == pg.K_LEFT:
                for sprite in player_sprites:
                    sprite.left()
            elif event.key == pg.K_RIGHT:
                for sprite in player_sprites:
                    sprite.right()
            elif event.key == pg.K_DOWN:
                for sprite in player_sprites:
                    sprite.down()
    
    time = round(t.clock(), 0)
    if time > previous:
        previous = time
        down()


    contact()
    
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pg.display.flip()
    clock.tick(60)


