import pygame as pg

class Block(pg.sprite.Sprite):

    def __init__(self, x, y, colour):

        self.length = 20
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.length, self.length))

        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = x + 100
        self.rect.y = y

        self.x = x
        self.y = y
##        all_sprites.add(self)
##        player_sprites.add(self)

    def left(self):
        self.rect.x -= self.length
        for sprite in player_sprites:
           if sprite.rect.x < 100:
              for sprite in player_sprites:
                 sprite.rect.x += self.length
                 
    def right(self):
        self.rect.x += self.length
        for sprite in player_sprites:
           if sprite.rect.x + self.length > scrn_width - 100:
              for sprite in player_sprites:
                 sprite.rect.x -= self.length

    def down(self):
        self.rect.y += self.length
