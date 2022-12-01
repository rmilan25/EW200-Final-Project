import pygame
from pygame.sprite import Sprite

class Person(Sprite):
    def __init__(self, game, position):
        super(). __init__()
        self.freefall_image = pygame.image.load('images/person.png')
        self.parachute_image = pygame.image.load('images/person_parachute.png')

        #Start as freefall image
        self.image = self.freefall_image
        self.rect = self.image.get_rect()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
    def draw(self):
        self.screen.blit(self.image,self.rect)
        if self.rect.midbottom == ((self.screen_rect.height)/4):
            self.image = self.parachute_image

    def freefall(self):
        self.rect.y += 2