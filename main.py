from spillebrett import Spillebrett # jeg imortere spillebrettet
def main():
    dimensjon1 = input("oppgi dimensjoner på spillebrettet.\n rader : ")
    dimensjon2 = input ("kolonner : ") # per brukeren om å teste antall rader og kolonner
    klasse=Spillebrett(int(dimensjon1),int(dimensjon2))#definere en objke (kasse)
    klasse._tegnBrett()# kaller på _tegnBrett
    a = input('\nprss enter for å gå videre til neste steg og q for å avslutte programmet ')
    while a != "q":# lager en while løkke og skrive ut programet.
        klasse.oppdatering()
        klasse._tegnBrett()
        print('\ngenerasjonsnummer er : ', klasse.hentGnerasjonsnummer())
        print('\nantal levende er : ', klasse.finnAntallLevende())
        a = input('\nprss enter for å gå videre til neste steg og q for å avslutte programmet ')

main()
