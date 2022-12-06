import pygame
import sys
import random
import time
from turret import Turret
from tank import Tank
from helicopter import Helicopter
from person import Person
from bullet import Bullet

class Game():
    def __init__(self):
        pygame.init()

        pygame.mixer.music.load('sounds/background.wav')
        pygame.mixer.music.play(-1)

        self.game_active = True

        self.screen = pygame.display.set_mode((700, 700)) #created surface
        self.screen_rect = self.screen.get_rect() #get rect attributes of screen

        self.screen.fill((0,0,0)) #paint the surface background

        self.lives = 3
        self.score = 0
        self.level = 10000 #number will decrease allowing difficulty to increase

        self.tank = Tank(self)
        self.tank.rect.midbottom = self.screen_rect.midbottom

        self.turret = Turret(self.tank.rect.midtop)

        self.helicopters = pygame.sprite.Group()
        self.flyover()

        self.persons = pygame.sprite.Group()

        self.bullets = pygame.sprite.Group()

        self.clock = pygame.time.Clock()
    def run_game(self):
        while True:
            self.listen_to_events()

            if self.game_active:
                #All update functions
                for helicopter in self.helicopters.sprites():
                    helicopter.fly()
                for person in self.persons.sprites():
                    person.update()
                for person in self.persons.sprites():
                    person.freefall()
                self.bullets.update()
                self.bullet_person_collision()
                self.bullet_helicopter_collision()
                self.turret.update()

                #check edges
                self.check_bottom()
                self.check_left()
                for bullet in self.bullets.copy():
                    if (bullet.rect.bottom <= 0) or (bullet.rect.left >= self.screen_rect.width) or \
                            (bullet.rect.right <= 0): #delete bullets past the screen
                        self.bullets.remove(bullet)

                #Draw functions
                self.screen.fill((0, 0, 0))
                self.turret.draw(self.screen)
                self.tank.draw()
                for helicopter in self.helicopters.sprites():
                    helicopter.draw()
                for bullet in self.bullets.sprites():
                    bullet.draw()
                for person in self.persons.sprites():
                    person.draw()

                if random.randint(0,self.level) <= 2:
                    self.deploy()

            self.game_over()
            self.display_score()
            pygame.display.flip()
            self.clock.tick(60)
    def listen_to_events(self):
        for event in pygame.event.get():  # listen for events
            if event.type == pygame.QUIT:  # if window is closed, game quits
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.fire_bullet()
                boom = pygame.mixer.Sound('sounds/boom.wav')  # sound effect for firing bullet
                pygame.mixer.Sound.play(boom)
            elif event.type == pygame.KEYDOWN:  # listen to keydown events
                if event.key == pygame.K_RIGHT:
                    self.turret.rotate_right = True
                elif event.key == pygame.K_LEFT:
                    self.turret.rotate_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()
                    boom = pygame.mixer.Sound('sounds/boom.wav') #sound effect for firing bullet
                    pygame.mixer.Sound.play(boom)
                elif event.key == pygame.K_r:
                    self.score = 0
                    self.lives = 3
                    pygame.mixer.music.play(-1)
                    self.flyover()
                    self.game_active = True
            elif event.type == pygame.KEYUP:  # listen to keyup events
                if event.key == pygame.K_RIGHT:
                    self.turret.rotate_right = False
                elif event.key == pygame.K_LEFT:
                    self.turret.rotate_left = False
    def deploy(self):
        width = random.randint(0,self.screen_rect.width)
        person = Person(self, (width, 0))
        self.persons.add(person)

    def flyover(self):
        helicopter = Helicopter(self, self.screen_rect.width)
        self.helicopters.add(helicopter)

    def bullet_person_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.persons, True, True)
        if collision:
            self.score += 1
            self.bullets.empty()
            self.deploy()
            self.difficulty()
    def bullet_helicopter_collision(self):
        collision = pygame.sprite.groupcollide(self.bullets, self.helicopters, True, True)
        if collision:
            self.score += 2
            self.bullets.empty()
            self.deploy()
            self.difficulty()
    def check_bottom(self):
        for person in self.persons.sprites():
            if person.rect.bottom >= self.screen_rect.height:
                self.bullets.empty()
                self.persons.empty()
                self.lives -= 1
                time.sleep(1.0)
                self.deploy()
    def game_over(self):
        if self.lives == 0:
            self.persons.empty()
            self.bullets.empty()
            self.helicopters.empty()
            pygame.mixer.music.stop()
            self.game_over_screen()
            self.game_active = False

        with open('high_score.txt', 'r') as file: #open text file
                self.high_score = int(file.read()) #read the first line and set str as int for high score
        if self.score > int(self.high_score): #allows scores to update
            with open('high_score.txt', 'w') as file: #open txt file and write the new high score
                self.high_score = file.write(str(self.score))
    def game_over_screen(self):
        self.screen.fill((0,0,0))
        font = pygame.font.Font('freesansbold.ttf', 32)
        game_over = font.render("Game Over", True, (255, 255, 255))
        self.screen.blit(game_over, (((self.screen_rect.height)/2), ((self.screen_rect.width)/2)))

    def display_score(self): #helping hand achievment, helped classmate with this code
        font = pygame.font.Font('freesansbold.ttf',15)
        score = font.render("Score :" + str(self.score), True, (255,255,255))
        self.screen.blit(score, (5,5))
        font = pygame.font.Font('freesansbold.ttf', 15)
        high_score_render = font.render("High Score :" + str(self.high_score), True, (255, 255, 255))
        self.screen.blit(high_score_render, (5, 20))

    def difficulty(self):
        if (self.score%10) == 0 and self.score > 0:
            self.flyover()
            self.deploy()
            self.level -= 100
    def check_left(self):
        for helicopter in self.helicopters.sprites():
            if helicopter.rect.right <= 0:
                self.helicopters.empty()
                self.deploy()
    def fire_bullet(self):
        bullet = Bullet(self)
        self.bullets.add(bullet)



game = Game()
game.run_game()
