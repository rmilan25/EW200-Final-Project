import pygame

class Tank():
    def __init__(self, screen):
        self.image = pygame.image.load('images/tank.png') #load image
        self.rect = self.image.get_rect()  # get rect attributes of tank
        self.screen = screen
    def draw(self,screen):
        self.screen.blit(self.image,self.rect)

