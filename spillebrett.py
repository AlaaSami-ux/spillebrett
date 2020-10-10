from random import randint # importere randint for å velge et telfedig status
from celle import Celle # importere Celle
class Spillebrett: # oppretter et classe Spillebrett
    def __init__(self, rader, kolonner):# konstruktur med tre parameter
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []# oppretter et rutenett som tar antall rader gange antall kolooner.
        for i in range(self._rader):
            self._rutenett.append([])
            for j in range(self._kolonner):
                self._rutenett[i].append(Celle())
        self._generasjonsnummer = 0 # opprette en generasjonsteller.
        self.generer()# kaller på metoden generer


    def generer(self):#oppreter metoden generer
# denne metoden skal gjør slik at hver celle i rutenett har 1/3 sjanse for å være levende
        for i in range(self._rader):
            for j in range(self._kolonner):
                s = randint(0,2)
                if s == 1:
                    self._rutenett[i][j].settLevende()

    def _tegnBrett(self):# oppretter en metode _tegnBrett
    # den skal bruke for løkke for å skrive hver element i rutenett
        print(10*'\n')
        for i in self._rutenett:
            print('')
            for j in i:
                print(j.hentStatusTegn(), end=' ')

    def finnNabo(self, rad, kolonn): # jeg oppretter en metode for å finne naboen
        naboliste = [] # en tom liset
        for i in range(-1,2):# en for løkke som tar fra -1 til og ikke med 2
            for j in range(-1,2):
                nRad = i + rad
                nKolonn = j + kolonn
                gyldig = True
                if nRad == rad and nKolonn == kolonn:# hvis cellen er seg selv er den ikke gyldig
                    gyldig = False
                if nRad >= self._rader or nRad < 0:# ikke gå ut av range
                    gyldig = False
                if nKolonn >= self._kolonner or nKolonn < 0:
                    gyldig = False
                if gyldig:
                    naboliste.append(self._rutenett[nRad][nKolonn])# adder nabocelle til listen
        return naboliste

    def oppdatering(self):# opprette en metode oppdatering som finner levende og døde celler.
        levende = []
        doed = []
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                celle = self._rutenett[i][j]
                naboliste = self.finnNabo(i, j)
                antallLevende = 0
                for nabo in naboliste:
                    if nabo.erLevende():
                        antallLevende += 1
#vet hvor mange levende naboer cellen har
                if celle.erLevende():
                    if antallLevende < 2:
                        doed.append(celle)
                    elif antallLevende >=2 and antallLevende<=3:
                        levende.append(celle)
                    elif antallLevende > 3 :
                        doed.append(celle)
                else:
                    if antallLevende == 3:
                        levende.append(celle)
        #her har vi levende-liste og dod-liste
        for c in levende:# oppdatere status
            c.settLevende()
        for c in doed:
            c.settDoed()
    def hentGnerasjonsnummer(self):# opprette en metude som øker antall generasjoner
        self._generasjonsnummer += 1 #
        return self._generasjonsnummer

    def finnAntallLevende(self):# opprette en metode som kan finne antall levende
        levendeCelle = 0
        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                celle = self._rutenett[i][j]
                if celle.erLevende():
                    levendeCelle += 1
        return levendeCelle
