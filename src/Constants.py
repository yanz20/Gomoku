#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:26:19 2019

@author: freddie
"""

import pygame as pg

display_surf = pg.display.set_mode((800,700), pg.HWSURFACE)
image_surf = pg.transform.scale(pg.image.load("assets/board.png").convert(),(800,700))
image_menu = pg.transform.scale(pg.image.load("assets/menu.png").convert(),(500,500))
pg.font.init()

slategrey = (112,128,144)
green = (0,128,0)
white = (255,255,255)
gameDisplay = pg.display.set_mode((800,700))
smallText = pg.font.Font('freesansbold.ttf', 20)
largeText = pg.font.Font('freesansbold.ttf', 30)
boardwidth = 15

def textObjects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def menuButton(dimWidth, buttonWidth, dimHeight, buttonHeight, text, color, colorChanged, action = None):
    global button_down
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if (dimWidth + buttonWidth) > mouse[0] > (dimWidth) and (dimHeight + buttonHeight) > mouse[1] > (dimHeight):
        pg.draw.rect(gameDisplay, colorChanged, (dimWidth, dimHeight, buttonWidth, buttonHeight))
        if click[0] == 1 and not button_down and action != None:
            button_down = True
            action()
        elif click[0] == 0:
            button_down = False
    else:
        pg.draw.rect(gameDisplay, color, (dimWidth, dimHeight, buttonWidth, buttonHeight))
    textSurf, textRect = textObjects(text, smallText)
    textRect.center = ((dimWidth + buttonWidth/2), (dimHeight + buttonHeight/2))
    gameDisplay.blit(textSurf, textRect)

