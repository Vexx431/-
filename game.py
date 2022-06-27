import pygame
from random import randint
from menu import *


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.button_escape, self.button_space, self.button_down, self.button_up, self.button_a, self.button_d, self.button_return, self.button_w, self.button_s = False, False, False, False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 700, 500
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font = 'arialmt.ttf'
        self.black, self.white, self.blue = (0, 0, 0), (255, 255, 255), (0,255,255)
        self.main_menu = MainMenu(self)
        self.rules = Rules(self)
        self.options = Options(self)
        self.winscore1 = Winscore1(self)
        self.winscore2 = Winscore2(self)
        self.curr_menu = self.main_menu

        self.clock = pygame.time.Clock()

        self.volume_music, self.volume_sounds = 1, 1
        self.shot_sound = pygame.mixer.Sound('shot.wav')
        self.back_sound = pygame.mixer.Sound('back.wav')
        self.shot_sound.set_volume(self.volume_sounds)
        self.back_sound.set_volume(self.volume_sounds)

        self.images1 = pygame.image.load('image1.jpg')

        self.paddleA = Paddle((255, 255, 255), 10, 100)
        self.paddleA.rect.x, self.paddleA.rect.y = 10, 200

        self.paddleB = Paddle((255, 255, 255), 10, 100)
        self.paddleB.rect.x, self.paddleB.rect.y = 680, 200

        self.ball = Ball((255, 255, 255), 10, 10)
        self.ball.rect.x, self.ball.rect.y = self.DISPLAY_W / 2, self.DISPLAY_H / 2

        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.paddleA)
        self.all_sprites_list.add(self.paddleB)
        self.all_sprites_list.add(self.ball)

        self.score, self.score2 = 0, 0
        pygame.mixer.music.load('backround.mp3')
        pygame.mixer.music.set_volume(self.volume_music)
        pygame.mixer.music.play(-1)

        self.status = True

    def uslovie_pobedIb(self):
        if self.score == 11:
            self.playing = False
            self.curr_menu = self.winscore1
        elif self.score2 == 11:
            self.curr_menu = self.winscore2
            self.playing = False
        return self.score, self.score2

    def otskok(self):
        if self.ball.rect.x >= 690:
            pygame.mixer.Sound.play(self.back_sound)
            self.score += 1

            # время задержки в милисекундах
            pygame.time.wait(750)

            self.ball.rect.x, self.ball.rect.y = self.DISPLAY_W / 2, self.DISPLAY_H / 2
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.x <= 0:
            pygame.mixer.Sound.play(self.back_sound)
            self.score2 += 1

            # время задержки в милисекундах
            pygame.time.wait(750)

            self.ball.rect.x, self.ball.rect.y = self.DISPLAY_W / 2, self.DISPLAY_H / 2
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.y > 490:
            self.ball.velocity[1] = -self.ball.velocity[1]
        if self.ball.rect.y < 0:
            self.ball.velocity[1] = -self.ball.velocity[1]

        if pygame.sprite.collide_mask(self.ball, self.paddleA) or pygame.sprite.collide_mask(self.ball, self.paddleB):
            if pygame.sprite.collide_mask(self.ball, self.paddleA):
                pygame.mixer.Sound.play(self.shot_sound)
            if pygame.sprite.collide_mask(self.ball, self.paddleB):
                pygame.mixer.Sound.play(self.shot_sound)
            self.ball.bounce()

    def move_flat(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.paddleA.moveUp(5)
        if keys[pygame.K_s]:
            self.paddleA.moveDown(5)
        if keys[pygame.K_UP]:
            self.paddleB.moveUp(5)
        if keys[pygame.K_DOWN]:
            self.paddleB.moveDown(5)

    def music(self):
        if self.button_space:
            if not self.status:
                self.status = True
                pygame.mixer.music.unpause()
            else:
                self.status = False
                pygame.mixer.music.pause()
            pygame.time.delay(50)

    def draw_score(self):
        font = pygame.font.Font(None, 74)
        text = font.render(str(self.score), 0, self.blue)
        self.window.blit(text, (250, 5))
        text = font.render(str(self.score2), 0, self.blue)
        self.window.blit(text, (420, 5))

    def game_loop(self):
        while self.playing:
            self.check_events()
            self.move_flat()
            self.otskok()
            self.uslovie_pobedIb()
            self.music()
            self.window.blit(self.images1, (0, 0))
            pygame.draw.line(self.window, (255, 255, 255), [350, 0], [350, 500], 3)
            self.draw_score()
            self.all_sprites_list.draw(self.window)
            self.all_sprites_list.update()
            pygame.display.flip()
            self.reset_buttons()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.button_return = True
                if event.key == pygame.K_DOWN:
                    self.button_down = True
                if event.key == pygame.K_UP:
                    self.button_up = True
                if event.key == pygame.K_w:
                    self.button_w = True
                if event.key == pygame.K_s:
                    self.button_s = True
                if event.key == pygame.K_ESCAPE:
                    self.button_escape = True
                if event.key == pygame.K_SPACE:
                    self.button_space = True
                if event.key == pygame.K_d:
                    self.button_d = True
                if event.key == pygame.K_a:
                    self.button_a = True

    def reset_buttons(self):
        self.button_escape, self.button_space, self.button_down, self.button_up, self.button_return, self.button_w, self.button_s, self.button_d, self.button_a = False, False, False, False, False, False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font, size)
        surface_text = font.render(text, True, self.black)
        rect = surface_text.get_rect()
        rect.center = (x, y)
        self.display.blit(surface_text, rect)


class Ball (pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        black = (0, 0, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()
        black = (0, 0, 0)
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        if self.rect.y > 400:
            self.rect.y = 400
