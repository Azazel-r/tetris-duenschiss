# Autor: René Richter
# Datum: 25.01.2021
# Zweck: Klasse Startbildschirm

import pygame
from random import randint

class Startbildschirm:

    def __init__(self, win):
        self.__win = win
        self.__farbL = [randint(0,255) for i in range(3)]
        self.__faktorL = [1,1,1]
        self.__font1 = pygame.font.Font("./assets/PetMe64.ttf", 85)
        self.__font2 = pygame.font.Font("./assets/PetMe64.ttf", 22)
        self.__schriftzug1 = self.__font1.render("Tetris", False, (0,0,0))
        self.__schriftzug2 = self.__font2.render("Drücke Leertaste zum beginnen!", False, (0,0,0))
        self.__schriftzug3 = self.__font2.render("Drücke R für die Bestenliste!", False, (0,0,0))

    def ändereFarben(self):
        for j in range(len(self.__farbL)):
            if randint(0,60) == 22:
                self.__faktorL[j] *= -1
            self.__farbL[j] += self.__faktorL[j] * randint(1,3)
            if self.__farbL[j] > 255:
                self.__farbL[j] = 255
                self.__faktorL[j] = -1
            elif self.__farbL[j] < 0:
                self.__farbL[j] = 0
                self.__faktorL[j] = 1

    def Bildschirm(self, i):
        self.__win.fill((self.__farbL[0], self.__farbL[1], self.__farbL[2]))
        self.__win.blit(self.__schriftzug1, (125, 75))
        if i > 29:
            self.__win.blit(self.__schriftzug2, (75, 500))
            self.__win.blit(self.__schriftzug3, (75, 300))
        self.ändereFarben()
