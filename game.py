import pygame
import sys
from turret import Turret
from tank import Tank
from helicopter import Helicopter
from person import Person

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700)) #created surface
        self.screen_rect = self.screen.get_rect() #get rect attributes of screen

        self.screen.fill((0,0,0)) #paint the surface background

        self.tank = Tank(self.screen)
        self.tank.rect.midbottom = self.screen_rect.midbottom

        self.turret = Turret(self.tank.rect.midtop)

        self.helicopter = Helicopter(self.screen)
        self.helicopter.rect.left = self.screen_rect.width

        self.person = Person(self.screen)

        self.clock = pygame.time.Clock()
    def run_game(self):
        while True:
            self.listen_to_events()

            self.screen.fill((0,0,0))
            self.tank.draw(self.screen)
            self.helicopter.move()
            self.helicopter.draw() #Sprite object??
            self.person.fall()
            self.deploy_person()
            self.turret.update()
            self.turret.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)
    def listen_to_events(self):
        for event in pygame.event.get():  # listen for events
            if event.type == pygame.QUIT:  # if window is closed, game quits
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # listen to keydown events
                if event.key == pygame.K_RIGHT:
                    self.turret.rotate_right = True
                elif event.key == pygame.K_LEFT:
                    self.turret.rotate_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:  # listen to keyup events
                if event.key == pygame.K_RIGHT:
                    self.turret.rotate_right = False
                elif event.key == pygame.K_LEFT:
                    self.turret.rotate_left = False

    def deploy_person(self):
        self.person.draw_freefall()




game = Game()
game.run_game()
