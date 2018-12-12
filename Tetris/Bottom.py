import pygame as pg

class Bottom(pg.sprite.Sprite):

   def __init__(self, colour):

       pg.sprite.Sprite.__init__(self)
       self.image = pg.Surface((600, 100))
       self.image.fill(colour)

       self.rect = self.image.get_rect()
       self.rect.x = 0
       self.rect.y = 800
