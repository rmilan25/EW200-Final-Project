import pygame
import random
from pygame.sprite import Sprite

class Person(Sprite):
    def __init__(self, game):
        super(). __init__()
        self.image = pygame.image.load('images/person_parachute.png')

        self.rect = self.image.get_rect()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
    def draw(self):#Do I need this for sprite?
        height = random.randint(0,self.screen.height)
        width = random.randint(0,self.screen_rect.width)
        print(self.rect)
        self.screen.blit(self.image,self.rect)
    def fall(self):
        self.rect.y += 1