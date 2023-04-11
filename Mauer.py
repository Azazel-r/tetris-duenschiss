# Autor: René Richter
# Datum: 25.01.2022
# Zweck: Klasse Mauer für Tetris

import pygame
from block2  import *
from copy import deepcopy

class Mauer:

    def __init__(self, win):
        self.__win = win
        self.__mauer = [[0 for i in range(12)] for j in range(20)]
        for y in range(len(self.__mauer)):
            for x in range(len(self.__mauer[y])):
                if x == 10 or x == 11 or y == 18 or y == 19:
                    self.__mauer[y][x] = 1
        self.__mauerMitBlock = deepcopy(self.__mauer)
        self.__sprite = pygame.image.load("./assets/block0.png")
        self.__block = None

    def istTetris(self) -> int: #mmmmmmmmmh working i guess
        erg = []
        for y in range(len(self.__mauer)-2):
            if self.__mauer[y] == [1 for i in range(12)]:
                erg.append(y)
        for i in erg:
            self.__mauer = self.__mauer[:i] + self.__mauer[i+1:]
        for i in range(len(erg)):
            self.__mauer = [[0,0,0,0,0,0,0,0,0,0,1,1]] + self.__mauer
        return len(erg)

    def draw(self):
        for y in range(len(self.__mauer)-2):
            for x in range(len(self.__mauer[y])-2):
                if self.__mauer[y][x] == 1:
                    self.__win.blit(self.__sprite, (x*50+50, y*50))
                elif self.__mauer[y][x] == 0:
                    continue
                #else:
                    #print(self.__mauer[y][x]) # um irgendwelche fehler zu catchen

    def getBlock(self, b):
        self.__block = b

    def setzeBlockEin(self):
        self.__mauerMitBlock = deepcopy(self.__mauer)
        pos = self.__block.gibPos()
        g = self.__block.getAktivesGrid()
        yy, xx = 0, 0
        for y in range(pos[1], pos[1]+4, 1):
            for x in range(pos[0], pos[0]+4, 1):
                try:
                    self.__mauerMitBlock[y][x] += g[yy][xx]
                except:
                    pass
                xx += 1
            xx = 0
            yy += 1

    def macheBlockFEST(self):
        pos = self.__block.gibPos()
        g = self.__block.getAktivesGrid()
        yy, xx = 0, 0
        for y in range(pos[1], pos[1]+4, 1):
            for x in range(pos[0], pos[0]+4, 1):
                self.__mauer[y][x] += g[yy][xx]
                xx += 1
            xx = 0
            yy += 1

    def überprüfen(self) -> bool:
        erg = True
        for y in range(20):
            for x in range(12):
                if self.__mauerMitBlock[y][x] > 1:
                    erg = False
        return erg

    def überprüfeVerloren(self) -> bool:
        erg = True
        for y in range(2):
            for x in range(10):
                if self.__mauer[y][x] != 0:
                    erg = False
        return erg

    def __str__(self):
        l = ["0", "1", "2"]
        string = ""
        for y in range(20):
            for x in range(12):
                string += str(l[self.__mauerMitBlock[y][x]])
            string += "\n"
        return string + f"{len(self.__mauerMitBlock)-1}"
                
# --------------------------
# Test für Mauer.istTetris()
"""
m = Mauer("t") # lol
print(m)
m.einsetzen([i, 17] for i in [3,4,5,6])
m.einsetzen([i, 16] for i in range(10))
m.einsetzen([i, 15] for i in [0,1,8,9])
m.einsetzen([i, 14] for i in [0,9])
print(m)
m.istTetris()
print(m)
"""
"""
# Test für Block einsetzen usw
from block2 import *
b = Block2(1,5,[600,700])
m = Mauer(5)
print(m)
m.getBlock(b)
m.setzeBlockEin()
print(m)
b.move(0,5)
m.setzeBlockEin()
print(m)
b.drehen(1)
b.move(3,0)
m.setzeBlockEin()
print(m)
b.move(2,0)
m.setzeBlockEin()
print(m.überprüfen())
"""
