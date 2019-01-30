#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 16:09:44 2019

@author: freddie
"""
import re

# Black represents AI(int 2), and white represents human(int 1)
# Use regular expression to find existence of each type

blackfive = ['22222'] #score 50000
blacklive4 = ['022220'] #score 4320
blackmid = ['022200', '002220', '022020', '020220', '22220',
            '02222', '22022', '20222', '22202'] #score 720
blacklow = ['002200', '002020', '020200'] #score 120
blacksingle = ['000200', '002000']  #score 20

whitefive = ['11111'] #score 50000
whitelive4 = ['011110'] #score 4320
whitemid = ['011100', '001110', '011010', '010110', '11110',
            '01111', '11011', '10111', '11101'] #score 720
whitelow = ['001100', '001010', '010100'] #score 120
whitesingle = ['000100', '001000']  #score 20

boardscore = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,1,2,2,2,2,2,2,2,2,2,2,2,1,0],
              [0,1,2,3,3,3,3,3,3,3,3,3,2,1,0],
              [0,1,2,3,4,4,4,4,4,4,4,3,2,1,0],
              [0,1,2,3,4,5,5,5,5,5,4,3,2,1,0],
              [0,1,2,3,4,5,6,6,6,5,4,3,2,1,0],
              [0,1,2,3,4,5,6,7,6,5,4,3,2,1,0],
              [0,1,2,3,4,5,6,6,6,5,4,3,2,1,0],
              [0,1,2,3,4,5,5,5,5,5,4,3,2,1,0],
              [0,1,2,3,4,4,4,4,4,4,4,3,2,1,0],
              [0,1,2,3,3,3,3,3,3,3,3,3,2,1,0],
              [0,1,2,2,2,2,2,2,2,2,2,2,2,1,0],
              [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

# foucorner(board) is to find a area which we evaluate points in this area only
def fourcorner(board):
    xmin, xmax, ymin, ymax = 0, 14, 0, 14
    while ymin < 15 and sum(board[ymin]) == 0 :
        ymin += 1
    if ymin - 5 < 0 or ymin == 15:
        ymin = 0
    else:
        ymin = ymin - 5
        
    while ymax >= 0 and sum(board[ymax]) == 0:
        ymax -= 1
    if ymax + 5 > 14 or ymax == -1:
        ymax = 14
    else:
        ymax = ymax + 5
        
    i, j = 0, 0
    while j < 15 and board[i][j] == 0 :
        i += 1
        if i > 14:
            i = 0
            j += 1
    if j - 5 > 0 and j - 5 != 10:
        xmin = j - 5
    else:
        xmin = 0
        
    i, j = 0, 14
    while j >= 0 and board[i][j] == 0:
        i += 1
        if i > 14:
            i = 0
            j -= 1
    if j + 5 < 14 and j + 5 != 4:
        xmax = j + 5    
    else:
        xmax = 14
    
    return xmin, xmax, ymin, ymax


def black_line_score(line):
    score = 0
    result = re.search(blackfive[0], line)
    if result != None:
        score = 50000
    else:
        result = re.search(blacklive4[0], line)
        if result != None:
            score = 4320
        else:
            for x in blackmid:
                if re.search(x, line) != None:
                    score = 720
                    return score
            for y in blacklow:
                if re.search(y, line) != None:
                    score = 120
                    return score
            for z in blacksingle:
                if re.search(z, line) != None:
                    score = 20
                    return score
    return score                   
    
def white_line_score(line):
    score = 0
    result = re.search(whitefive[0], line)
    if result != None:
        score = 50000
    else:
        result = re.search(whitelive4[0], line)
        if result != None:
            score = 4320
        else:
            for x in whitemid:
                if re.search(x, line) != None:
                    score = 720
                    return score
            for y in whitelow:
                if re.search(y, line) != None:
                    score = 120
                    return score
            for z in whitesingle:
                if re.search(z, line) != None:
                    score = 20
                    return score
    return score  

def position_score(board, x, y, c):
    score = 0
    if c == 'black':
        board[y][x] = 2
    elif c == 'white':
        board[y][x] = 1
    
    line = ''   
    left, right = x-4, x+4
    if left < 0:
        left = 0
    if right > 14:
        right = 14
    for i in range(left, right+1):
        line += str(board[y][i])

    line1 = ''
    top, down = y-4, y+4
    if top < 0:
        top = 0
    if down > 14:
        down = 14   
    for j in range(top, down+1):
        line1 += str(board[j][x])
    
    line2 = ''
    left, right = x-4, x+4
    top, down = y-4, y+4
    while left < 0 or top < 0:
        left += 1
        top += 1
    while right > 14 or down > 14:
        right -= 1
        down -= 1
    while left <= right:
        line2 += str(board[top][left])
        left += 1
        top += 1

    line3 = ''
    left, right = x-4, x+4
    top, down = y-4, y+4
    while left < 0 or down > 14:
        left += 1
        down -= 1
    while right > 14 or top < 0:
        right -= 1
        top += 1
    while left <= right:
        line3 += str(board[down][left])
        left += 1
        down -= 1 
    
    if c == 'black':
        score =  black_line_score(line) +  black_line_score(line1) +  black_line_score(line2) + black_line_score(line3)
    elif c == 'white':
        score =  white_line_score(line) +  white_line_score(line1) +  white_line_score(line2) + white_line_score(line3)
    board[y][x] = 0
    return score + boardscore[y][x]


    
    

