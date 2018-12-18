import pygame as pg

class Block(pg.sprite.Sprite):

    def __init__(self, x, y, colour):

        self.length = 25
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((self.length, self.length))

        self.image.fill(colour)

        self.rect = self.image.get_rect()
        self.rect.x = int(x) * self.length + 50
        self.rect.y = int(y) * self.length + 50

        self.x = int(x)
        self.y = int(y)
        print self.x, self.y

    def left(self):
        self.rect.x -= self.length

    def right(self):
        self.rect.x += self.length

    def down(self):
        self.rect.y += self.length
        
        
    
