# Autor: René Richter
# Datum: 07.11.2021
# Zweck: Tetris weil Nick es nicht hinbekommnt

import pygame
import json
from pygame.constants import KEYDOWN
from Spielfeld import *
from Startbildschirm import *
from random import randint
import tkinter as tk
from tkinter import simpledialog

pygame.init()

class Tetris:

    def __init__(self):
        self.mainLoop()

    def abspeichern(self, name, score):
        pfad = "./assets/rekorde.json"
        try:
            with open(pfad, "r") as datei:
                rekorde = json.load(datei)
                for j in range(len(rekorde)):
                    if rekorde[j]["score"] <= score:
                        rekorde.insert(j, {"name": name, "score": score})
                    elif j+1 == len(rekorde):
                        rekorde.insert(j+1, {"name": name, "score": score})
        except:
            rekorde = [{"name": name, "score": score}]

        with open(pfad, "w") as datei:
            json.dump(rekorde, datei, indent=4)

    # Main lüüp
    def mainLoop(self):
        """ Vor.: -
            Eff.: Die Mainloop des Spiels. Sie wird so lange ausgeführt, bis
                  das Spiel vorbei ist.
            Erg.: -
        """

        # Fenster, Clock, Musik und Font (von pygame)
        self.__win = pygame.display.set_mode((800,600)) # später 850,900
        pygame.display.set_caption("Tetris v0.1")
        self.__clock = pygame.time.Clock()
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load("./assets/tetris.mp3")
        
        # Variablen
        aktiv = True
        ersterDurchlaufImSpiel = True
        nächster = randint(1,7)-1
        nächsteFarbe = randint(0,7)
        ingame = 1 # 1 - im Startbildschirm | 2 - im Spiel | 3 - Game over
        i = 0
        
        # Startbildschirm
        self.__Startbildschirm = Startbildschirm(self.__win)

        # tatsächliche Mainloop
        while aktiv:

            events = pygame.event.get()

            if ingame == 1:
                
                self.__Startbildschirm.Bildschirm(i)
                for event in events:
                    if event.type == pygame.KEYDOWN and (event.key==pygame.K_KP_ENTER or event.key==pygame.K_SPACE):
                        ingame = 2
                    elif event.type == pygame.KEYDOWN and event.key==pygame.K_r:
                        pfad = "./assets/rekorde.json"
                        try:
                            with open(pfad, "r") as datei:
                                rekorde = json.load(datei)
                                print("------------- * -------------")
                                print("      SCOREBOARD TOP 10      ")
                                for j in range(len(rekorde)):
                                    if j < 10:
                                        print(f"{j+1}. Platz: {rekorde[j]['name']} | Score: {rekorde[j]['score']}")
                                print("------------- * -------------")
                        except:
                            print("Keine Rekorde vorhanden!")
 
            if ingame == 2:

                if ersterDurchlaufImSpiel:
                    pygame.display.quit()
                    self.__win = pygame.display.set_mode((850,900))
                    # Spielfeld
                    self.__Spielfeld = Spielfeld(self.__win)
                    self.__Spielfeld.Spielsetup()
                    ersterDurchlaufImSpiel = False
                    fallListe = [29]
                    scoreListe = [40,100,300,1200]
                    pygame.mixer.music.play(-1)


                a = (0,0)
                
                for event in events:
                    if event.type == KEYDOWN:

                        if event.key==pygame.K_q:
                            self.__Spielfeld.dreheBlock(-1)
                            a = (0,1)

                        if event.key==pygame.K_w:
                            self.__Spielfeld.dreheBlock(1)
                            a = (0,-1)

                        if event.key==pygame.K_LEFT:
                            self.__Spielfeld.bewegenX(-1)
                            a = (1,0)

                        if event.key==pygame.K_RIGHT:
                            self.__Spielfeld.bewegenX(1)
                            a = (-1,0)

                        if event.key == pygame.K_e:
                            if len(fallListe) == 1:
                                fallListe = [9,19,29,39,49,59]
                            else:
                                fallListe = [29]
                            
                if not self.__Spielfeld.überprüfen():
                    for j in range(len(a)):
                        if a[j]:
                            if j == 0:
                                self.__Spielfeld.bewegenX(a[j])
                            if j == 1:
                                self.__Spielfeld.dreheBlock(a[j])

                if i in fallListe:
                    self.__Spielfeld.lassBlockFallen()
                    if not self.__Spielfeld.überprüfen():
                        self.__Spielfeld.wiederNachObenUndFestmachen()
                        self.__Spielfeld.spawnBlock(nächster, nächsteFarbe)
                        nächster = randint(1,7)-1
                        nächsteFarbe = randint(0,7)
                
                t = self.__Spielfeld.istTetris()
                if t != None:
                    self.__Spielfeld.addLines(t)
                    self.__Spielfeld.addScore(scoreListe[t-1])

                if i == 59:
                    self.__Spielfeld.sekunde()
                
                if not self.__Spielfeld.überprüfeVerloren():
                    ingame = 3

                self.__Spielfeld.drawTest()
                self.__Spielfeld.drawNächsten(nächster, nächsteFarbe)

            if ingame == 3:
                pygame.mixer.music.pause()
                fenster = tk.Tk()
                fenster.withdraw()
                fenster.attributes("-topmost", True)
                name = simpledialog.askstring("Namen eintragen", "GAME OVER!\nBitte trage deinen Namen für die Bestenliste ein!")
                fenster.attributes("-topmost", False)
                if name != "" and name != None:
                    self.abspeichern(name, self.__Spielfeld.getScore())
                aktiv = False

            # Beenden mit dem roten "X" oder ESC
            for event in events:
                if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                    aktiv = False

            i += 1
            if i >= 60:
                i = 0

            # Display update and 60 FPS
            pygame.display.update()
            self.__clock.tick(60)

        pygame.display.quit()
        pygame.quit()


# --------------
# Hauptprogramm

Tetris()
