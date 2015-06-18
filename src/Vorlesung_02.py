print('Bitte die gewuenschte Funktion auswaehlen:')
print('    1) Groesster gemeinsamer Teiler nach EUKLIDES mit Itaration Zaehler')
print('    2) Groesster gemeinsamer Teiler nach EUKLIDES')
print('    3) Schnelle Potenz nach LEGENDRE mit Iteration Zaehler')
print('    4) Schnelle Potenz nach LEGENDRE')
print('    5) Zufallsnummer nach HP Alg. von 1977')
print('    6) Gleichheit zwischen zwei realen Nummern')
print('    7) Binomial Koef. nach Pascal')
selFunc=input('Funktionsnummer auswaehlen: ')
if selFunc==1:
    from UtilFunc import GGT_Counting
    x=input('Erste Nummer: ')
    y=input('Zweite Nummer: ')
    print('GGT:',GGT_Counting(x,y))
if selFunc==2:
    from UtilFunc import GGT
    x=input('Erste Nummer: ')
    y=input('Zweite Nummer: ')
    print('GGT:',GGT(x,y))
if selFunc==3:
    from UtilFunc import pot_Counting
    x=input('Base: ')
    y=input('Exp: ')
    print('Potenz: ',pot_Counting(x,y))
if selFunc==4:
    from UtilFunc import pot
    x=input('Base: ')
    y=input('Exp: ')
    print('Potenz: ',pot(x,y))
if selFunc==5:
    from UtilFunc import HPRand
    x=input('Seed: ')
    print('Rnd: ',HPRand(x))
if selFunc==6:
    from UtilFunc import gleich
    x=input('Erste Zahl: ')
    y=input('Zweite Zahl: ')
    print('Gleichheit: ',gleich(x,y))
if selFunc==7:
    from UtilFunc import bino
    x=input('Erste Zahl: ')
    y=input('Zweite Zahl: ')
    print('Binomial Koeff: ',bino(x,y))