import pygame
import sys
import random
from turret import Turret
from tank import Tank
from helicopter import Helicopter
from person import Person
from bullet import Bullet

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 700)) #created surface
        self.screen_rect = self.screen.get_rect() #get rect attributes of screen

        self.screen.fill((0,0,0)) #paint the surface background

        self.tank = Tank(self)
        self.tank.rect.midbottom = self.screen_rect.midbottom

        self.turret = Turret(self.tank.rect.midtop)

        self.helicopter = Helicopter(self)
        self.helicopter.rect.left = self.screen_rect.width

        self.persons = pygame.sprite.Group()
        self.deploy()

        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
    def run_game(self):
        while True:
            self.listen_to_events()

            self.screen.fill((0,0,0))

            self.tank.draw()

            self.helicopter.move()
            self.helicopter.draw() #Sprite object??

            self.bullets.update()
            for bullet in self.bullets.sprites():
                bullet.draw()

            for bullet in self.bullets.copy():
                if (bullet.rect.bottom <= 0) or (bullet.rect.left == self.screen_rect.width) or \
                        (bullet.rect.right == 0): #delete bullets past the screen
                    self.bullets.remove(bullet)

            self.persons.draw(self.screen)
            for person in self.persons.sprites():
                person.fall()

            self.turret.update()
            self.turret.draw(self.screen)

            self.collisions()

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
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()
                    #boom = pygame.mixer.Sound('sounds/boom.wav') #sound effect for firing bullet
                    #pygame.mixer.Sound.play(boom)
            elif event.type == pygame.KEYUP:  # listen to keyup events
                if event.key == pygame.K_RIGHT:
                    self.turret.rotate_right = False
                elif event.key == pygame.K_LEFT:
                    self.turret.rotate_left = False

    def deploy(self):
        width = random.randint(0,self.screen_rect.width)
        person = Person(self, (width, 0))
        self.persons.add(person)

    def collisions(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.persons, True, True)
        if collision:
            self.bullets.empty()
            self.deploy()
    def fire_bullet(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)




game = Game()
game.run_game()
