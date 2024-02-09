# a legfontosabb ciklus a for ciklus: elotesztelo ciklus!
# for i in range(0,10): # 0 < i < 10
#     print(f"A ciklus jelenlegi erteke: {i}")
# for i in range(0, 10, 2):
#     print(i)

homersekletek = [20.4, 20.5, 20.3, 20.2, 20.4] 

#Irjunk egy fuggvenyt, ami kiatlagolja a homersekletet!
def atlag():
    """Az atlag kiszamitasa: osszes elem osztva az elemek osszegevel (szum(elemek)/elemek szama)"""
    elemek_osszege = 0
    for homerseklet in homersekletek:
        elemek_osszege = elemek_osszege + homerseklet

    elemek_szama = len(homersekletek)

    return elemek_osszege / elemek_szama  

atlag_homerseklet = atlag()
print(f"Az atlag homerseklet: {atlag_homerseklet}")

#Kovetkezo feladatok kozosen:
#1. ismerjuk meg a szotarakat, rakjunk bele allatokat es hogy hany fokon elnek meg
#2. generaljunk veletlenszeru homersekleteket (24 darabot ami 1 napot reprezental - orankent 1 ertek)
#3. ellenorizzuk, hogy melyik allat tud megelni azon a homersekleten!


#Feladatok Tominak:
#Irj egy programot ami bekeri hany ora van (csak az orat 24 oras formatumban, pld. 18 vagy 22 vagy 5)
#A program koszonjon napszaknak megfeleloen: jo reggelt 4 es 9 kozott, szep napot 10 es 14 kozott, szep delutant 15 es 19 kozott egyebkent pedig jo estet irjon ki.
#ertek bekerese usertol: input()

# korod = input("Hany eves vagy?")  # ADDIG ALL A PROGRAM AMIG NEM NYOM A USER ENTERT. minden amit beolvas az string!!!
# print(f"A korod: {korod}, tipusa: {type(korod)}")
# szuletesi_ev = 2024 - int(korod)  # AT KELL KONVERTALNI INT-E HOGY SZAMOLJUNK AZ INPUTTAL!
# print(f"{szuletesi_ev}-ben szulettel!")
