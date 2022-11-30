import pygame

class Tank():
    def __init__(self, game):
        self.image = pygame.image.load('images/tank.png') #load image
        self.rect = self.image.get_rect()  # get rect attributes of tank
        self.screen = game.screen
    def draw(self):
        self.screen.blit(self.image,self.rect)

