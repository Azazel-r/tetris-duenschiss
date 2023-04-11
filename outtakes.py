# --------------------------------------------------------
# Dinge die ich rausgenommen habe, weil sie so nicht mehr
# funktionieren, ich sie aber evtl. noch aufheben wollte
# --------------------------------------------------------


# Klasse Spielfeld

"""def bewegenX(self, richtung):
        obj = self.__block
        obj.move(int(50*richtung),0)

        if obj.gibPos()[0] == 0:
            if not obj.istSpalteFrei(0):
                obj.move(int(50),0)

        elif obj.gibPos()[0] == -50:
            if not obj.istSpalteFrei(1):
                obj.move(int(50),0)

        elif obj.gibPos()[0] == 400:
            if not obj.istSpalteFrei(3):
                obj.move(int(-50),0)

        elif obj.gibPos()[0] == 450:
            if not obj.istSpalteFrei(2):
                obj.move(int(-50),0)

        elif obj.gibPos()[0] < -50 or obj.gibPos()[0] > 450:
            obj.move(int(-50*richtung),0)"""

"""def macheBlockFest(self):
    erg = []
    for e in self.__block.gibPosEinzelnerTeile():
        erg.append(((e[0]-50)//50, e[1]//50))
    self.__mauer.einsetzen(erg)
    print(erg)
    print(self.__mauer) # noch nich fertig, aber so halb"""
    
    #def doBlocksHitGround(self):
        #for e in self.blocks:
            #lT = e.
            #if e.pos[1] == 

    #def speichern(self):
    #    if self.überprüfen():
    #        self.__zurück = self.__block.gibPos()
    #        return True


# Klasse Mauer

"""def löseBlockHeraus(self):
        pos = self.__block.gibPos()
        g = self.__block.getAktivesGrid()
        yy, xx = 0, 0
        for y in range(pos[1], pos[1]+4, 1):
            for x in range(pos[0], pos[0]+4, 1):
                self.__mauer[y][x] -= g[yy][xx] # geht nicht???!??!
                xx += 1
            xx = 0"""



    """def einsetzen(self, l:list):
        for e in l:
            for y in range(len(self.__mauer)):
                for x in range(len(self.__mauer[y])):
                    if e[0] == x and e[1] == y:
                        self.__mauer[y][x] = 1"""
