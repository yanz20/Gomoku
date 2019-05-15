#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:52:24 2019

This module is used to build the main menu.

@author: freddie
"""

import pygame as pg
import sys 
import Constants
import App
import random

## Class Menu defines all the entries to the game and the exit.
class Menu:
    
##load the image to build the window and background.
    def __init__(self):
        self.menu = True
        pg.init()
        self._display_surf = Constants.display_surf
        self._image_surf = Constants.image_surf
        self._image_menu = Constants.image_menu
        pg.display.set_caption('Gomoku AI')
        
    def quitGame():
        pg.quit()
        sys.exit()

# start simple AI vs human , user draw first
    def startGame0(self):
        self.menu = False
        app = App.App()
        rand = random.randint(0,1)
        if rand == 0:
            app.simple_user_first()
        else:
            app.simple_AI_first()

# start hard AI vs human , user draw first        
    def startGame1(self):
        self.menu = False
        app = App.App()
        rand = random.randint(0,1)
        if rand == 0:
            app.hard_User_first()
        else:
            app.hard_AI_first()        
        
# start Player vs Player mode
    def startGame2(self):
        self.menu = False
        app = App.App()
        app.run_PVP()

# start AI vs AI mode     
    def startGame3(self):
        self.menu = False
        app = App.App()
        app.run_AIVAI()
        

# build the UI and entries      
    def appmenu(self):
        self.menu = True
        while self.menu:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            self._display_surf.fill((255,255,255))
            self._display_surf.blit(self._image_surf, (0,0))
            self._display_surf.blit(self._image_menu, (100,70))
            # User first entry    
            textsurface = Constants.largeText.render("Select game:", False,(0,0,0))
            self._display_surf.blit(textsurface,(605,70))
            #Constants.menuButton(650, 100, 80, 40, "UserFirst", Constants.slategrey, Constants.green, self.startGame0)
            Constants.menuButton(650, 100, 140, 40, "Simple", Constants.slategrey, Constants.green, self.startGame0)

            # AI fisrt entry
            #textsurface = Constants.smallText.render("Hard AI:", False,(0,0,0))
           # self._display_surf.blit(textsurface,(620,200))
            Constants.menuButton(650, 100, 230, 40, "Hard", Constants.slategrey, Constants.green, self.startGame1)
            #Constants.menuButton(650, 100, 280, 40, "AIFirst", Constants.slategrey, Constants.green, self.startGame3)
            # P V P entry
            #textsurface = Constants.smallText.render("To start with PVP:", False,(0,0,0))
            #self._display_surf.blit(textsurface,(620,340))
            Constants.menuButton(650, 100, 320, 40, "P V P", Constants.slategrey, Constants.green, self.startGame2)
            
            #textsurface = Constants.smallText.render("AI VS. AI:", False,(0,0,0))
            #self._display_surf.blit(textsurface,(620,430))
            Constants.menuButton(650, 100, 410, 40, "AI Vs. AI", Constants.slategrey, Constants.green, self.startGame3)
        #To exit the game            
            #textsurface = Constants.smallText.render("To exit:", False,(0,0,0))
            #self._display_surf.blit(textsurface,(620,510))
            Constants.menuButton(650, 100, 500, 40, "Exit", Constants.slategrey, Constants.green, Menu.quitGame)
            pg.display.update()
            