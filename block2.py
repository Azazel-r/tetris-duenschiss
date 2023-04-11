# Autor: René Richter
# Datum: 10.02.2022
# Zweck: Klasse Block2 zum testen für Tetris

# Es gibt folgende Blöcke:
# L-Block, J-Block, I-Block, S-Block, Z-Block, T-Block, O-Block

import pygame
from random import randint

SPRITES = [pygame.image.load("./assets/block1.png"), pygame.image.load("./assets/block2.png"),
           pygame.image.load("./assets/block3.png"), pygame.image.load("./assets/block4.png"),
           pygame.image.load("./assets/block5.png"), pygame.image.load("./assets/block6.png"),
           pygame.image.load("./assets/block7.png"), pygame.image.load("./assets/block8.png"),]

GRIDS0 = [[[0,0,0,0], # O
          [0,1,1,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,0,0,0], # I
          [1,1,1,1],
          [0,0,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # T
          [1,1,1,0],
          [0,1,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # S
          [0,1,1,0],
          [1,1,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # Z
          [1,1,0,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,0,0,0], # L
          [1,1,1,0],
          [1,0,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # J
          [1,1,1,0],
          [0,0,1,0],
          [0,0,0,0]]]

GRIDS1 = [[[0,0,0,0], # O
          [0,1,1,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,0,1,0], # I
          [0,0,1,0],
          [0,0,1,0],
          [0,0,1,0]],

         [[0,1,0,0], # T
          [1,1,0,0],
          [0,1,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # S
          [0,1,0,0],
          [0,1,1,0],
          [0,0,1,0]],

         [[0,0,0,0], # Z
          [0,0,1,0],
          [0,1,1,0],
          [0,1,0,0]],

         [[1,1,0,0], # L
          [0,1,0,0],
          [0,1,0,0],
          [0,0,0,0]],

         [[0,1,0,0], # J
          [0,1,0,0],
          [1,1,0,0],
          [0,0,0,0]]]

GRIDS2 = [[[0,0,0,0], # O
          [0,1,1,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,0,0,0], # I
          [0,0,0,0],
          [1,1,1,1],
          [0,0,0,0]],

         [[0,1,0,0], # T
          [1,1,1,0],
          [0,0,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # S
          [0,0,0,0],
          [0,1,1,0],
          [1,1,0,0]],

         [[0,0,0,0], # Z
          [0,0,0,0],
          [1,1,0,0],
          [0,1,1,0]],

         [[0,0,1,0], # L
          [1,1,1,0],
          [0,0,0,0],
          [0,0,0,0]],

         [[1,0,0,0], # J
          [1,1,1,0],
          [0,0,0,0],
          [0,0,0,0]]]

GRIDS3 = [[[0,0,0,0], # O
          [0,1,1,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,1,0,0], # I
          [0,1,0,0],
          [0,1,0,0],
          [0,1,0,0]],

         [[0,1,0,0], # T
          [0,1,1,0],
          [0,1,0,0],
          [0,0,0,0]],

         [[0,0,0,0], # S
          [1,0,0,0],
          [1,1,0,0],
          [0,1,0,0]],

         [[0,0,0,0], # Z
          [0,1,0,0],
          [1,1,0,0],
          [1,0,0,0]],

         [[0,1,0,0], # L
          [0,1,0,0],
          [0,1,1,0],
          [0,0,0,0]],

         [[0,1,1,0], # J
          [0,1,0,0],
          [0,1,0,0],
          [0,0,0,0]]]

# hierbei handelt es sich NICHT zwingend um Code-Duplizierung, da alle 4 Listen
# (GRIDS0 bis GRIDS3) alle Gitter der Blöcke in einer bestimmten Rotation
# beinhalten, und somit alle Listen komplett verschieden sind.

class Block2:

    def __init__(self, win:pygame.display, n:int, posR:list, f:int):
        self.__win = win
        self.__pos = [3, 0]
        self.__posR = posR
        self.__sprite = SPRITES[f]
        self.__grids = [GRIDS0[n], GRIDS1[n], GRIDS2[n], GRIDS3[n]]
        self.__aGrid = 0

    def move(self, x:int, y:int):
        """ Vor.: -
            Eff.: Der Block wurde um die angegeben Werte bewegt.
            Erg.: -
        """
        self.__pos[0] += x
        self.__pos[1] += y

    def drehen(self, richtung): # 0 oder 1 ??
        a = self.__aGrid
        self.__aGrid += int(richtung)
        if self.__aGrid > 3:
            self.__aGrid = 0
        elif self.__aGrid < 0:
            self.__aGrid = 3

    def drawR(self):
        xx, yy = 0, 0
        for y in range(0,200,50):
            for x in range(0,200,50):
                if self.__grids[self.__aGrid][yy][xx]:
                    self.__win.blit(self.__sprite, (self.__posR[0]+x, self.__posR[1]+y))
                xx += 1
            xx = 0
            yy += 1

    def drawNormal(self):
        xx, yy = 0, 0
        for y in range(0,200,50):
            for x in range(0,200,50):
                if self.__grids[self.__aGrid][yy][xx]:
                    self.__win.blit(self.__sprite, (50+self.__pos[0]*50+x, self.__pos[1]*50+y))
                xx += 1
            xx = 0
            yy += 1

    def getAktivesGrid(self):
        return self.__grids[self.__aGrid]

    def gibPos(self) -> list:
        return self.__pos
