import pygame as pg

class Wall(pg.sprite.Sprite):

   def __init__(self, x):

      pg.sprite.Sprite.__init__(self)
      self.image = pg.Surface((50, 900))
      self.image.fill((255, 255, 255))

      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = 0

