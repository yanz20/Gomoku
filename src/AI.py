#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:48:21 2019

@author: freddie
"""
import SimpleAI
import HardAI
from random import randint
import math

# nextmove() defines the simplest AI behaviour, which AI only consider next step.
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
    num = randint(0, num-1)
    return xlist[num], ylist[num]

def intelligentmove(board):
    score, x, y = HardAI.AlphaBeta(board, 3, -math.inf, math.inf, 'AI')
    return x, y

def intelligentmovewhite(board):
    score, x, y = HardAI.AlphaBeta(board, 2, -math.inf, math.inf, 'human')
    return x, y