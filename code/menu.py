#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.constants import KEYDOWN
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_ORAGEM, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./assets/MenuBg.png')
        self.rect = self.surf.get_rect(left=0,top=0)

    def run(self, ):
        menu_option = 0
        #play the background music
        pygame.mixer_music.load('./assets/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
        #Show the Menu
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50,"Mountain",(COLOR_ORAGEM),((WIN_WIDTH/2),70))
            self.menu_text(50, "Shooter", (COLOR_ORAGEM), ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20,MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()
        #Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # closed window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size,text,text_color,text_center_pos):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",size=text_size)
        text_surf: Surface = text_font.render(text,True,text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf,dest=text_rect)