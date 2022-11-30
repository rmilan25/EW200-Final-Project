import pygame
from pygame.sprite import Sprite

class Person(Sprite):
    def __init__(self, game, position):
        super(). __init__()
        self.freefall_image = pygame.image.load('images/person.png')

        self.rect = self.freefall_image.get_rect()
        self.rect.center = position

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
    def draw_freefall(self):#Do I need this for sprite?
        self.screen.blit(self.freefall_image,self.rect)
    def freefall(self):
        self.rect.y += 2