# Autor: René Richter
# Datum: 10.03.2022
# Zweck: blazing throughhh endless nights~

import pygame

class Scoreboard:

    def __init__(self, win):
        self.__win = win
        self.__score = 0
        self.__lines = 0
        self.__zeit = 0 # anz. sekunden seit spielbeginn
        self.__font1 = pygame.font.Font("./assets/PetMe64.ttf", 40)
        self.__schriftzug1 = self.__font1.render("Score", False, (255,255,255)) # Score text
        self.__schriftzug2 = self.__font1.render("Lines", False, (255,255,255)) # Lines text
        self.__schriftzug3 = self.__font1.render("Zeit", False, (255,255,255)) # Zeit text
        self.__schriftzug4 = self.__font1.render(str(self.__score), False, (25,25,25)) # Score wert
        self.__schriftzug5 = self.__font1.render(str(self.__lines), False, (25,25,25)) # Lines wert
        self.__schriftzug6 = self.__font1.render(str(self.__zeit), False, (25,25,25)) # Zeit wert
        
    def draw(self):
        # text
        self.__win.blit(self.__schriftzug1, (600, 10))
        self.__win.blit(self.__schriftzug2, (600, 210))
        self.__win.blit(self.__schriftzug3, (625, 410))
        # werte
        self.__win.blit(self.__schriftzug4, (600, 67))
        self.__win.blit(self.__schriftzug5, (600, 267))
        self.__win.blit(self.__schriftzug6, (600, 467))

    def addScore(self, s:int):
        self.__score += s
        self.__schriftzug4 = self.__font1.render(f"{self.__score}", False, (25,25,25))

    def addLines(self, n:int):
        self.__lines += n
        self.__schriftzug5 = self.__font1.render(f"{self.__lines}", False, (25,25,25))

    def sekunde(self):
        self.__zeit += 1
        self.__schriftzug6 = self.__font1.render(f"{self.__zeit}", False, (25,25,25))

    def getScore(self):
        return self.__score