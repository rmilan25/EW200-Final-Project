import pygame
from pygame.sprite import Sprite

class Person(Sprite):
    def __init__(self, screen):
        super(). __init__()
        self.freefall_image = pygame.image.load('images/person.png') #load image
        self.parachute_image = pygame.image.load('images/person_parachute.png')

        self.rect_freefall = self.freefall_image.get_rect()
        self.rect_parachute = self.parachute_image.get_rect()

        self.screen = screen
    def draw_freefall(self):#Do I need this for sprite?
        self.screen.blit(self.freefall_image,self.rect_freefall)

    def draw_parachute(self):
        self.screen.blit(self.parachute_image, self.rect_parachute)

    def fall(self):
        self.rect_freefall.y += 2

    def deploy_parachute(self):
        self.rect_parachute.y += 1
