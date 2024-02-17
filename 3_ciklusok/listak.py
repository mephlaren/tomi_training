#A lista egy olyan valtozo ami tobb elemet tartalmaz egy tipusbol!
#Deklaralasakor a [] zarojelekkel nyitom es zarom a tombot! ez az egydimenzios lista!
homersekletek = [20.4, 20.5, 20.3, 20.2, 20.4]  # -> ot elemu tomb!

print(homersekletek)
elso_homerseklet = homersekletek[0]  # a legtobb programozasi nyelvben, a tombok a 0. indexrol indulnak!
print(elso_homerseklet)
masodik_homerseklet = homersekletek[1]
print(masodik_homerseklet)

homersekletek.append(20.9)
print(homersekletek)
torolt = homersekletek.pop(3)  # a .pop() torli az atadott indexen levo elemet a listabol! viszont visszaadja annak az erteket!
print(homersekletek)
print(f"A torolt ertek: {torolt}")  # nem tudunk hozzaferni nem letezo indexhez (out of range). A lista merete dinamikus.
homersekletek_merete = len(homersekletek)
print(f"A lista merete: {homersekletek_merete}")

ures = []  # a dinamikus listat uresen is letrehozhatju
print(ures)
ures.append('Szia')  # futas kozben allitodik a merete
print(ures)
hossz = len(ures[0])
print(f"Szo hossza: {hossz}")