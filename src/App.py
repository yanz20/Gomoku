#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:47:22 2019

This module defines how each mode of game works.

@author: freddie
"""

import pygame as pg
import Menu
import sys
import Constants
import AI

class App():
    
    def __init__(self):
        self._display_surf = Constants.display_surf
        self._image_surf = Constants.image_surf
        self.board = [[0 for x in range(15)] for y in range(15)]
        self.lastmovex = None
        self.lastmovey = None
        self.userturn = None
        self.done = False
        self.type = None # indicates three game types
        self.draw()
        
    def quitGame(self):
         pg.quit()
         sys.exit()
         
    def restartGame(self):
        if self.type ==  0:
            self.__init__()
            self.simple_user_first()
        elif self.type == 1:
            self.__init__()
            self.simple_AI_first()
        elif self.type == 2:
            self.__init__()
            self.hard_User_first()       
        elif self.type == 3:
            self.__init__()
            self.hard_AI_first()       
        elif self.type == 4:
            self.__init__()
            self.run_PVP()       
        elif self.type == 5:
            self.__init__()
            self.run_AIVAI() 
            
    def toMenu(self):
        theApp = Menu.Menu()
        theApp.appmenu()
    
    # Wait until the player make his move, then update this move to the board and 
    # indicate this to be the most recent move.
    def user_move(self):
        while self.userturn == True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x >= 20 and x <= 620 and y >= 20 and y <= 620:
                        if self.board[(y-20)//40][(x-20)//40] == 0:
                            self.board[(y-20)//40][(x-20)//40] = 1
                            self.lastmovex = ((x-20)//40+1)*40
                            self.lastmovey = ((y-20)//40+1)*40
                            self.userturn = False
            self.update()
        self.done = self.iswin(self.lastmovex//40 - 1, self.lastmovey//40 - 1)      
        
    # AI ask simple or hard AI for the instruction of the next move, then make
    # this move and update it to the board.
    def AI_move(self, d):
        # take d as input to choose which difficulty to base on, in order to make move.
       if d == 'simple':
            x, y = AI.simplemove(self.board, 'black')
            self.board[y][x] = 2
            self.lastmovex = (x+1)*40
            self.lastmovey = (y+1)*40
            self.userturn = True
            self.update()
            self.done = self.iswin(self.lastmovex//40 - 1, self.lastmovey//40 - 1)   
            
       elif d == 'hard':
            x, y = AI.intelligentmove(self.board)
            self.board[y][x] = 2
            self.lastmovex = (x+1)*40
            self.lastmovey = (y+1)*40
            self.userturn = True
            self.update()
            self.done = self.iswin(self.lastmovex//40 - 1, self.lastmovey//40 - 1)      
         
    #this is similar to uer_move, but this one draws the white piece.        
    def user2_move(self):
        while self.userturn == False:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x >= 20 and x <= 780 and y >= 20 and y <= 780:
                        if self.board[(y-20)//40][(x-20)//40] == 0:
                            self.board[(y-20)//40][(x-20)//40] = 2
                            self.lastmovex = ((x-20)//40+1)*40
                            self.lastmovey = ((y-20)//40+1)*40
                            self.userturn = True
            self.update()
        self.done = self.iswin(self.lastmovex//40 - 1, self.lastmovey//40 - 1) 
     
    # This AI is created to against the current AI, it is the less intelligent one. 
    def AI2_move(self, d):
       if d == 'simple':
            x, y = AI.intelligentmovewhite(self.board)
            self.board[y][x] = 1
            self.lastmovex = (x+1)*40
            self.lastmovey = (y+1)*40
            self.userturn = False
            self.update()
            self.done = self.iswin(self.lastmovex//40 - 1, self.lastmovey//40 - 1) 
    
    #method used to update the board.        
    def update(self):
        for i in range(15):
            for j in range(15):
                if self.board[i][j] == 1:
                    pg.draw.circle(self._display_surf, (255,255,255),(j*40+40,i*40+40), 20, 20)
                elif self.board[i][j] == 2:
                    pg.draw.circle(self._display_surf, (0,0,0),(j*40+40,i*40+40), 20, 20)
        if self.lastmovex != None:
            pg.draw.circle(self._display_surf, (0,255,0),(self.lastmovex, self.lastmovey), 8, 8)
        Constants.menuButton(650, 100, 200, 50, "Menu", Constants.slategrey, Constants.green, self.toMenu)
        Constants.menuButton(650, 100, 500, 50, "Exit", Constants.slategrey, Constants.green, self.quitGame)
        Constants.menuButton(650, 100, 350, 50, "Restart", Constants.slategrey, Constants.green, self.restartGame)
        pg.display.update()
        

        
    def draw(self):
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(self._image_surf, (0,0))
        for i in range(1,16):
            pg.draw.line(self._display_surf,[0,0,0], [40, i*40], [600, i*40], 2)
            pg.draw.line(self._display_surf,[0,0,0], [i*40,40], [i*40,600], 2)        
        pg.display.flip()
     
    # This method is used to draw winning information. 
    def drawwin(self):
        if self.type in {0,1,2,3}:
            if self.userturn == True:
                textsurface = Constants.largeText.render("AI win!", False,(0,0,0))
                self._display_surf.blit(textsurface,(620, 150))
            elif self.userturn == False:
                textsurface = Constants.largeText.render("You win!", False,(0,0,0))
                self._display_surf.blit(textsurface,(620, 150))            
        elif self.type in {4,5}:
            if self.userturn == True:
                textsurface = Constants.largeText.render("Black win!", False,(0,0,0))
                self._display_surf.blit(textsurface,(620, 150))
            elif self.userturn == False:
                textsurface = Constants.largeText.render("White win!", False,(0,0,0))
                self._display_surf.blit(textsurface,(620, 150))            

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT :
                    pg.quit()
                    sys.exit()
            Constants.menuButton(650, 100, 200, 50, "Menu", Constants.slategrey, Constants.green, self.toMenu)
            Constants.menuButton(650, 100, 500, 50, "Exit", Constants.slategrey, Constants.green, self.quitGame)
            Constants.menuButton(650, 100, 350, 50, "Restart", Constants.slategrey, Constants.green, self.restartGame)
            pg.display.update()
            pg.time.Clock().tick(15)
    
    # This method is called after each move, is to check if game is finished.
    # It checks the most recent piece with four directions(- | / \) to see if
    # any contineous five.        
    def iswin(self, x, y): # x stands could be User or AI.
        if self.userturn == False:
            right = self.NumOfDir(x, y, 1, "right")
            left = self.NumOfDir(x, y, 1, "left")
            up = self.NumOfDir(x, y, 1, "up")
            down = self.NumOfDir(x, y, 1, "down")
            top_right = self.NumOfDir(x, y, 1, "top-right")
            top_left = self.NumOfDir(x, y, 1, "top-left")
            down_left = self.NumOfDir(x, y, 1, "down-left")
            down_right = self.NumOfDir(x, y, 1, "down-right")
            if right + left + 1 >= 5 or up + down + 1 >= 5 or top_right + down_left + 1 >= 5 or top_left + down_right + 1 >= 5:
                return True
            else:
                return False
            
        elif self.userturn == True: 
            right = self.NumOfDir(x, y, 2, "right")
            left = self.NumOfDir(x, y, 2, "left")
            up = self.NumOfDir(x, y, 2, "up")
            down = self.NumOfDir(x, y, 2, "down")
            top_right = self.NumOfDir(x, y, 2, "top-right")
            top_left = self.NumOfDir(x, y, 2, "top-left")
            down_left = self.NumOfDir(x, y, 2, "down-left")
            down_right = self.NumOfDir(x, y, 2, "down-right")
            if right + left + 1 >= 5 or up + down + 1 >= 5 or top_right + down_left + 1 >= 5 or top_left + down_right + 1 >= 5:
                return True
            else:
                return False
        
    def NumOfDir(self, x, y, n, d):# x,y is the position of the most recent move, n defines user(1) or AI(2), d is direction to check
        if d == "right":
            num = 0
            x += 1
            while x < Constants.boardwidth and self.board[y][x] == n:
                x += 1
                num += 1
            return num
        
        elif d == "left":
            num = 0
            x -= 1
            while x >= 0 and self.board[y][x] == n:
                x -= 1
                num += 1
            return num     
        
        elif d == "up":
            num = 0
            y -= 1
            while y >= 0 and self.board[y][x] == n:
                y -= 1
                num += 1
            return num     
            
        elif d == "down":
            num = 0
            y += 1
            while y < Constants.boardwidth and self.board[y][x] == n:
                y += 1
                num += 1
            return num                 
    
        elif d == "top-right":
            num = 0
            x += 1
            y -= 1
            while x < Constants.boardwidth and y > 0 and self.board[y][x] == n:
                x += 1
                y -= 1
                num += 1
            return num     
        
        elif d == "top-left":
            num = 0
            x -= 1
            y -= 1
            while x > 0 and y > 0 and self.board[y][x] == n:
                x -= 1
                y -= 1
                num += 1
            return num     
            
        elif d == "down-left":
            num = 0
            x -= 1
            y += 1
            while y < Constants.boardwidth and x > 0 and self.board[y][x] == n:
                x -= 1
                y += 1
                num += 1
            return num         

        elif d == "down-right":
            num = 0
            x += 1
            y += 1
            while x < Constants.boardwidth and y < Constants.boardwidth and self.board[y][x] == n:
                x += 1
                y += 1
                num += 1
            return num     
        
    #Following are all the game modes.   
    def simple_user_first(self):
        self.type = 0
        self.userturn = True
        while not self.done:
            if self.userturn == True:
                self.user_move()
            elif self.userturn == False:
                self.AI_move('simple')
        self.drawwin()
                
    def simple_AI_first(self):
        self.type = 1
        self.userturn = False
        while not self.done:
            if self.userturn == False:
                self.AI_move('simple')
            elif self.userturn == True:
                self.user_move()          
        self.drawwin()
        
    def hard_User_first(self):
        self.type = 2
        self.userturn = True
        while not self.done:
            if self.userturn == True:
                self.user_move()
            elif self.userturn == False:
                self.AI_move('hard')
        self.drawwin()
                
    def hard_AI_first(self):
        self.type = 3
        self.userturn = False
        while not self.done:
            if self.userturn == False:
                self.AI_move('hard')
            elif self.userturn == True:
                self.user_move()          
        self.drawwin()
        
    def run_PVP(self):
        self.type = 4
        self.userturn = True
        while not self.done:
            if self.userturn == True:
                self.user_move()
            elif self.userturn == False:
                self.user2_move()
        self.drawwin()
        
    def run_AIVAI(self):
        self.type = 5
        self.userturn = False
        while not self.done:
            if self.userturn == True:
                self.AI2_move('simple')
            elif self.userturn == False:
                self.AI_move('hard')
        self.drawwin()