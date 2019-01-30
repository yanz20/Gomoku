#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:45:56 2019

This module is to define the methods to find the best postion for next move, use more intelligent way.
@author: freddie
"""
import SimpleAI

# This method is to manage a desending list.
# because we want to cut off the low scored positions to imporve the efficency.
def  get_position(listt, e):
    if len(listt) == 0:
        return 0
    else:
        i = 0
        while i < len(listt) and listt[i] > e:
            i += 1
        return i

# This return the score of the position, similar to simple AI.
# It helps to eliminate the lowed scored postions. 
def position_score(board, x, y, role):
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

    if role == 'AI':
        score = SimpleAI.black_line_score(line) + SimpleAI.black_line_score(line1) + SimpleAI.black_line_score(line2) + SimpleAI.black_line_score(line3)
    elif role == 'human':
        score = SimpleAI.white_line_score(line) + SimpleAI.white_line_score(line1) + SimpleAI.white_line_score(line2) + SimpleAI.white_line_score(line3)        
    return score + SimpleAI.boardscore[y][x]

# To generate available moves from current board for the role(AI or human)
def GenerateMoves(board, role):
    legalmovex = []
    legalmovey = []  
    points = []
    xmin, xmax, ymin, ymax = SimpleAI.fourcorner(board)
    for i in range(xmin, xmax+1):
        for j in range(ymin, ymax+1):
            if board[j][i] == 0:
                if role == 'AI':
                    board[j][i] = 2
                    score = position_score(board,i,j,'AI')
                    board[j][i] = 1
                    score += position_score(board,i,j,'human')
                    board[j][i] = 0
                    p = get_position(points, score)
                    points.insert(p, score)
                    legalmovex.insert(p, i)
                    legalmovey.insert(p, j)                  
                elif role == 'human':
                    board[j][i] = 1
                    score = position_score(board,i,j,'human')
                    board[j][i] = 2
                    score += position_score(board,i,j,'AI')
                    board[j][i] = 0
                    p = get_position(points, score)
                    points.insert(p, score)
                    legalmovex.insert(p, i)
                    legalmovey.insert(p, j)
    legalmovex, legalmovey = legalmovex[:15], legalmovey[:15]
    #we only take the first 15 items, because there is a very high possibility
    #for them to be cutted off by alpha-beta cutting. 
    return legalmovex, legalmovey

def MakeNextMove(board, xlist, ylist, role):
    x = xlist[0]
    y = ylist[0]
    if role == 'human':
        board[y][x] = 1
    elif role == 'AI':
        board[y][x] = 2

# This method evaluate the current board and return the score of this situation.
# For the score, we must not only consider the AI, but also the human.
def evaluate(board):
        AIscore = 0
        humscore = 0
        for i in range(0,15):
            for j in range(0,15):
                if board[i][j] == 0 :
                    pass
                elif board[i][j] == 1:
                    humscore += position_score(board, j, i, 'human')
                elif board[i][j] == 2:
                    AIscore += position_score(board, j, i, 'AI')
        return humscore-AIscore
                    
        
def rolerev(role):
    if role == 'human':
        return 'AI'
    elif role == 'AI':
        return 'human'

# depth is how deep you want the AI to consider the move.
# To generate the move, AI must consider both "make myself best" and "let human into trouble"
# This algorithm bases on : AI choose the best from the worst given by human.
def AlphaBeta(board, depth, alpha, beta, role):
    xfinal, yfinal = None, None
    if depth == 0:
        return evaluate(board), None, None
    legx, legy = GenerateMoves(board, role)
    while len(legx) > 0:
        MakeNextMove(board, legx, legy, role) #make the move
        val = -AlphaBeta(board, depth - 1, -beta, -alpha, rolerev(role))[0]
        x = legx.pop(0) # Unmake the move
        y = legy.pop(0)
        board[y][x] = 0
        if val >= beta:
            return beta, None, None
        if val > alpha:
            alpha = val
            xfinal = x
            yfinal = y
    return alpha, xfinal, yfinal