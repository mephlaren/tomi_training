#Csinaljunk egy programot ami general 10 random szamot 10 es 50 kozott es novekvo sorba rendezi oket
#1. kell egy veletlenszam generalas listaba!
#2. kell egy rendszerezo fuggveny
#3. ki kell irni az eredmenyt!

#importalsz a fajlodba egy teljes modult!!
#import random
#a random modulebol beimportalja a randint fuggvenyt!
from random import randint

# szam = randint(10,50)
# print(szam)

min = 10
max = 50
darab = 10

def generalas(min, max, darab):
    """General darab mennyisegu veletlen szamot min es max kozott"""
    ertekek = []
    for i in range(0, darab):
        szam = randint(min, max)
        ertekek.append(szam)
    
    return ertekek


def rendszerezes(elemek):
    """Ez a fuggveny novekvo sorrendbe teszi a kapott elemeket es visszaadja az uj listat"""
    temp = elemek
    for i in range(0, len(temp)):
        for j in range(i+1, len(temp)):
            if temp[i] >= temp[j]:
                temp[i], temp[j] = temp[j], temp[i]

    return temp

generalt = generalas(min, max, darab)
print(f"Az eredeti listank: {generalt}")
rendezett = rendszerezes(generalt)
print(f"A rendszerezett listank: {rendezett}")


# Feladat:
# Csinalj egy szamkereso jatekot!
# Legyen egy random szam, a user inputtal tippel
# Ha nem talalta el, irjuk ki hogy nem talalt es kerjunk be uj szamot (Ez ciklussal fog menni es if-ek)
# Ha eltalta, irjuk ki hogy Gratulalok, talalt, es alljon le a program (pld. ciklusban break)
# Harom lehetosege van tippelni, ha 3 lehetoseg utan nem talalta el, alljon le a program es irja ki
# hogy vege a jateknak (pld. ciklusban break)