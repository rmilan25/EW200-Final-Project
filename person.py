import pygame
from pygame.sprite import Sprite

class Person(Sprite):
    def __init__(self, game, position):
        super(). __init__()
        self.freefall_image = pygame.image.load('images/person.png')
        self.parachute_image = pygame.image.load('images/person_parachute.png')
        self.position = position

        #Start as freefall image
        self.image = self.freefall_image
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
    def draw(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.rect.bottom >= ((self.screen_rect.height)/4):
            self.image = self.parachute_image

    def freefall(self):
        if self.image == self.freefall_image:
            self.rect.y += 4
        elif self.image == self.parachute_image:
            self.rect.y += 1