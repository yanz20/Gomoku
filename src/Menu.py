#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:52:24 2019

@author: freddie
"""

import pygame as pg
import sys 
import Constants
import App


class Menu:
 
    def __init__(self):
        self.menu = True
        pg.init()
        self._display_surf = Constants.display_surf
        self._image_surf = Constants.image_surf
        pg.display.set_caption('Gomoku AI')
        
        
    def quitGame():
        pg.quit()
        sys.exit()
        
    def startGame0(self):
        self.menu = False
        app = App.App()
        app.simple_user_first()
    
    def startGame1(self):
        self.menu = False
        app = App.App()
        app.simple_AI_first()
        
    def startGame2(self):
        self.menu = False
        app = App.App()
        app.hard_User_first()
        
    def startGame3(self):
        self.menu = False
        app = App.App()
        app.hard_AI_first()
        
    def startGame4(self):
        self.menu = False
        app = App.App()
        app.run_PVP()
        
    def startGame5(self):
        self.menu = False
        app = App.App()
        app.run_AIVAI()
        

        
    def appmenu(self):
        self.menu = True
        while self.menu:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self._display_surf.fill((255,255,255))
            self._display_surf.blit(self._image_surf, (0,0))
            for i in range(1,16):
                pg.draw.line(self._display_surf,[0,0,0], [40, i*40], [600, i*40], 2)
                pg.draw.line(self._display_surf,[0,0,0], [i*40,40], [i*40,600], 2)
            # User first entry    
            textsurface = Constants.smallText.render("Simple AI:", False,(0,0,0))
            self._display_surf.blit(textsurface,(620,50))
            Constants.menuButton(650, 100, 80, 40, "UserFirst", Constants.slategrey, Constants.green, self.startGame0)
            Constants.menuButton(650, 100, 140, 40, "AIFirst", Constants.slategrey, Constants.green, self.startGame1)

            # AI fisrt entry
            textsurface = Constants.smallText.render("Hard AI:", False,(0,0,0))
            self._display_surf.blit(textsurface,(620,200))
            Constants.menuButton(650, 100, 230, 40, "UserFirst", Constants.slategrey, Constants.green, self.startGame2)
            Constants.menuButton(650, 100, 280, 40, "AIFirst", Constants.slategrey, Constants.green, self.startGame3)
            # P V P entry
            textsurface = Constants.smallText.render("To start with PVP:", False,(0,0,0))
            self._display_surf.blit(textsurface,(620,340))
            Constants.menuButton(650, 100, 370, 40, "P V P", Constants.slategrey, Constants.green, self.startGame4)
            
            textsurface = Constants.smallText.render("AI VS. AI:", False,(0,0,0))
            self._display_surf.blit(textsurface,(620,430))
            Constants.menuButton(650, 100, 460, 40, "AI Vs. AI", Constants.slategrey, Constants.green, self.startGame5)
        #To exit the game            
            textsurface = Constants.smallText.render("To exit:", False,(0,0,0))
            self._display_surf.blit(textsurface,(620,510))
            Constants.menuButton(650, 100, 540, 40, "Exit", Constants.slategrey, Constants.green, Menu.quitGame)
            pg.display.update()
            