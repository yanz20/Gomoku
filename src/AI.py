#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:48:21 2019

This module is to deal with the request of instruction.

@author: freddie
"""
import SimpleAI
import HardAI
from random import randint
import math

# simplemove will return the x,y for the next suggested move, using simple AI.
def simplemove(board, c):
    xmin, xmax, ymin, ymax = SimpleAI.fourcorner(board)
    score = 0
    xlist = []
    ylist = []
    num = 0
    for i in range(xmin, xmax+1):
        for j in range(ymin, ymax+1):
            if board[j][i] == 0:
                temp = SimpleAI.position_score(board, i, j, c)
                if temp > score:
                    score = temp
                    xlist, ylist = [], []
                    xlist.append(i)
                    ylist.append(j)
                    num = 1
                elif temp == score:
                    xlist.append(i)
                    ylist.append(j)
                    num += 1
    num = randint(0, num-1) #Add random in order to make movement unpredictabl3.
    return xlist[num], ylist[num]

# intelligentmove return the x,y for next suggest move, using more intelligent AI,
# depth to consider is 3.
def intelligentmove(board):
    score, x, y = HardAI.AlphaBeta(board, 3, -math.inf, math.inf, 'AI')
    return x, y

# intelligentmove return the x,y for next suggest move, using more intelligent AI,
# depth to consider is 2.
# This is used to build AI vs AI mode. 
def intelligentmovewhite(board):
    score, x, y = HardAI.AlphaBeta(board, 2, -math.inf, math.inf, 'human')
    return x, y