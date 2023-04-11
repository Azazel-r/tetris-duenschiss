# Autor: René Richter
# Datum: 07.07.2021
# Zweck: Klasse Spielfeld für Tetris

import pygame
from block2 import *
from Mauer import *
from random import randint
from scoreboard import *

BG = (158,155,0) # Farben für den
BG2 = (25,25,25) # Hintergrund

class Spielfeld:
    """ Vor.:  -
        Eff.: Ein Spielfeld mit angegebenen Parametern ist erzeugt.
        Erg.: Ein Objekt der Klasse Spielfeld ist geliefert.
    """
    def __init__(self, win:pygame.display) -> "Spielfeld":
        self.__win = win

    def Spielsetup(self):
        self.__posR = [600, 700]
        self.__block = Block2(self.__win, randint(1,7)-1, self.__posR, randint(0,7))
        self.__mauer = Mauer(self.__win)
        self.__mauer.getBlock(self.__block)
        self.__score = Scoreboard(self.__win)
    
    def drawTest(self):
        self.__win.fill(BG2)
        # das grüne spielfeld selbst
        pygame.draw.rect(self.__win, BG, (50,0,500,900))
        pygame.draw.rect(self.__win, BG, (600,700,200,200))
        # die grünen scoreboard felder
        pygame.draw.rect(self.__win, BG, (575, 60, 250, 50))
        pygame.draw.rect(self.__win, BG, (575, 260, 250, 50))
        pygame.draw.rect(self.__win, BG, (575, 460, 250, 50))
        self.__mauer.draw()
        if self.__block != None:
            self.__block.drawNormal()
        self.__score.draw()
    
    def drawNächsten(self, nächster:int, f:int):
        b = Block2(self.__win, nächster, self.__posR, f)
        b.drawR()

    def dreheBlock(self, richtung:int):
        if self.__block != None:
            self.__block.drehen(richtung)
            self.__mauer.setzeBlockEin()

    def spawnBlock(self, n:int, f:int):
        self.__block = Block2(self.__win, n, self.__posR, f)
        self.__mauer.getBlock(self.__block)

    def lassBlockFallen(self):
        if self.__block != None:
            self.__block.move(0, 1)
            self.__mauer.setzeBlockEin()

    def wiederNachObenUndFestmachen(self):
        if self.__block != None:
            self.__block.move(0, -1)
            self.__mauer.setzeBlockEin()
            self.__mauer.macheBlockFEST()
            self.__block = None
            
    def bewegenX(self, richtung:int): # -1 oder 1
        self.__block.move(richtung, 0)
        self.__mauer.setzeBlockEin() 

    def überprüfen(self) -> bool:
        if self.__block != None:
            x, y = self.__block.gibPos()[0], self.__block.gibPos()[1]
            return self.__mauer.überprüfen() and -2 <= x <= 8 and 0 <= y <= 16

    def istTetris(self):
        erg = self.__mauer.istTetris()
        if erg > 0:
            return erg
    
    def überprüfeVerloren(self):
        return self.__mauer.überprüfeVerloren()

    def addLines(self, n:int):
        self.__score.addLines(n)
    
    def addScore(self, s:int):
        self.__score.addScore(s)

    def getScore(self):
        return self.__score.getScore()

    def sekunde(self):
        self.__score.sekunde()

    def gibPos(self):
        return self.__block.gibPos()

    def __str__(self): # war nur zum test
        return f"X: {self.__block.gibPos()[0]} | Y: {self.__block.gibPos()[1]}"

