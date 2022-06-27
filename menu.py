import math
import sys

import pygame

import game


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 50, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('→', 20, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_buttons()

    @staticmethod
    def exit():
        sys.exit()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Старт"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h -120)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            # цвет меню
            self.game.display.fill(self.game.blue)

            # Описание
            self.game.draw_text('Старт', 40, self.mid_w, self.mid_h -120)
            self.game.draw_text("Настройки", 40, self.mid_w, self.mid_h - 60)
            self.game.draw_text("Правила", 40, self.mid_w, self.mid_h)
            self.game.draw_text('Выход', 40, self.mid_w, self.mid_h + 60)
            self.draw_cursor()
            self.blit_screen()

    # перемещение
    def move_cursor(self):
        if self.game.button_down:
            if self.state == 'Старт':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 60)
                self.state = 'Настройки'
            elif self.state == 'Настройки':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h )
                self.state = 'Правила'
            elif self.state == 'Правила':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 60)
                self.state = 'Выход'
            elif self.state == 'Выход':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h -120)
                self.state = 'Старт'
        elif self.game.button_up:
            if self.state == 'Старт':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 60)
                self.state = 'Выход'
            elif self.state == 'Выход':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h )
                self.state = 'Правила'
            elif self.state == 'Правила':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 60)
                self.state = 'Настройки'
            elif self.state == 'Настройки':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 120)
                self.state = 'Старт'

    # активация кнопок
    def check_input(self):
        self.move_cursor()
        if self.game.button_return:
            if self.state == 'Старт':
                self.game.playing = True
                self.run_display = False
            elif self.state == 'Настройки':
                self.game.curr_menu = self.game.options
                self.run_display = False
            elif self.state == 'Правила':
                self.game.curr_menu = self.game.rules
                self.run_display = False
            elif self.state == 'Выход':
                self.exit()
        elif self.game.button_escape:
            self.exit()
            self.run_display = False


class Winscore1(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Назад"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.blue)
            self.game.draw_text("Выиграл игрок 1", 50, self.mid_w, self.mid_h -20)
            self.game.draw_text('Назад', 20, self.mid_w, self.mid_h + 200)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        pass

    # активация кнопок
    def check_input(self):
        self.move_cursor()
        if self.game.button_return:
            if self.state == 'Назад':
                self.game.curr_menu = self.game.main_menu
            self.run_display = False


class Winscore2(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Назад"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.blue)
            self.game.draw_text("Выиграл игрок 2", 50, self.mid_w, self.mid_h -20)
            self.game.draw_text('Назад', 20, self.mid_w, self.mid_h + 200)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        pass

    # активация кнопок
    def check_input(self):
        self.move_cursor()
        if self.game.button_return:
            if self.state == 'Назад':
                self.game.curr_menu = self.game.main_menu
            self.run_display = False


class Rules(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Назад"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            # цвет меню
            self.game.display.fill(self.game.blue)

            self.game.draw_text("Правила игры", 40, self.mid_w, self.mid_h -200)
            self.game.draw_text("Игроки должны передвигать свою платформу для защиты ворот.", 20, self.mid_w, self.mid_h -150)
            self.game.draw_text("В начале каждого раунда мячик подаётся одному из игроков.", 20, self.mid_w, self.mid_h - 110)
            self.game.draw_text('Раунд продолжается до тех пор, пока один из игроков не заработает очко.', 20, self.mid_w, self.mid_h - 70)
            self.game.draw_text('Это происходит тогда, когда его противник не может отбить мячик.', 20, self.mid_w, self.mid_h -30)
            self.game.draw_text('Управление', 40, self.mid_w, self.mid_h +20)
            self.game.draw_text('Осуществляется нажатием клавиш на клавиатуре.', 20, self.mid_w, self.mid_h +70)
            self.game.draw_text('Для 1 игрока: w- вверх и s- вниз.', 20, self.mid_w, self.mid_h +110)
            self.game.draw_text('Для 2 игрока: up- вверх и down- вниз.', 20, self.mid_w, self.mid_h +150)

            self.game.draw_text('Назад', 25, self.mid_w, self.mid_h + 200)

            # Рисунок
            self.draw_cursor()

            self.blit_screen()

    def move_cursor(self):
        pass

    # активация кнопок
    def check_input(self):
        self.move_cursor()
        if self.game.button_return:
            if self.state == 'Назад':
                self.game.curr_menu = self.game.main_menu
            self.run_display = False


class Options(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Громкость музыки"
        self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h -100)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()

            # цвет меню
            self.game.display.fill(self.game.blue)
            self.game.draw_text('Настройки игры', 40, self.mid_w, self.mid_h - 200)
            self.game.draw_text('Громкость музыки', 23, self.mid_w, self.mid_h -100)
            self.game.draw_text('Громкость звуков', 23, self.mid_w, self.mid_h -50)

            # Кнопка назад
            self.game.draw_text('Назад', 25, self.mid_w, self.mid_h + 200)

            # Рисунок
            self.draw_cursor()

            self.blit_screen()

    def move_cursor(self):
        if self.game.button_up:
            if self.state == 'Громкость музыки':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)
                self.state = 'Назад'
            elif self.state == 'Назад':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 50)
                self.state = 'Громкость звуков'
            elif self.state == 'Громкость звуков':
                self.state = 'Громкость музыки'
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 100)
        elif self.game.button_down:
            if self.state == 'Громкость музыки':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 50)
                self.state = 'Громкость звуков'
            elif self.state == 'Громкость звуков':
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h + 200)
                self.state = 'Назад'
            elif self.state == 'Назад':
                self.state = 'Громкость музыки'
                self.cursor_rect.midtop = (self.mid_w + self.offset, self.mid_h - 100)

    # активация кнопок
    def check_input(self):
        self.move_cursor()
        if self.game.button_return:
            if self.state == 'Назад':
                self.game.curr_menu = self.game.main_menu
            self.run_display = False
        if self.game.button_a:
            if self.state == 'Громкость музыки':
                if self.game.volume_music > 0:
                    self.game.volume_music -= 0.1
                    pygame.mixer.music.set_volume(math.trunc(self.game.volume_music))

            if self.state == 'Громкость звуков':
                if self.game.volume_sounds > 0:
                    self.game.volume_sounds -= 0.1
                    self.game.shot_sound.set_volume(math.trunc(self.game.volume_sounds))
                    self.game.back_sound.set_volume(math.trunc(self.game.volume_sounds))

        if self.game.button_d:
            if self.state == 'Громкость музыки':
                if self.game.volume_music < 1:
                    self.game.volume_music += 0.1
                    pygame.mixer.music.set_volume(math.trunc(self.game.volume_music))

            if self.state == 'Громкость звуков':
                if self.game.volume_sounds > 1:
                    self.game.volume_sounds += 0.1
                    self.game.shot_sound.set_volume(math.trunc(self.game.volume_sounds))
                    self.game.back_sound.set_volume(math.trunc(self.game.volume_sounds))
