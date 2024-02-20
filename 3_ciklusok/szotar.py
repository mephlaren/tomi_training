#a szotar pythonon belul JSON reprezentacio: Kulcs - ertek parokat tudunk benne eltarolni
#pythonban a szotarakat dictionary-nek (dict) nevezzuk

#a szotar kulcsa mindig string, erteke a kulcsnak barmi lehet, string, int, float, list (tomb) vagy akar mas szotar is!!
szemely = {
    "nev": "Gabor",
    "kor": 28,
    "programnyelvek": [
        "python",
        "javascript",
        "c++",
        "PHP"
    ],
    "allatok": [
        {
            "nev": "Padlizsan",
            "fajta": "Sziami",
            "szin": "foka",
            "kor": 3
        },
        {
            "nev": "Rozsef",
            "fajta": "nem tul okos",
            "szin": "narancssarga",
            "kor": 3
        },
    ],
}

#muveletek listakkal:
#ertek kiolvasasa
#nev = szemely["nev"]
#Nem letezo kulcsra KeyError exceptiont dob a python!
#munka = szemely["munka"]
#A .get() fuggveny viszaadja a kulcshoz tartozo erteket, ha nem talalja, visszater egy default ertekkel
nev = szemely.get("nev", "Nincs ilyen kulcs!")
print(nev)

#a .pop() fgv. torli a kulcsot es erteket, visszateresi ertek a fgv-nek a kulcs erteke.
kor = szemely.pop("kor", "Nem tudom torolni!")
print(kor)
print(szemely)

#ertek hozzaadasa a szotar vegehez
szemely["munka"] = "programozo"
print(szemely)

#for ciklus a szotaron
print("For ciklus:")
#amennyiben ciklussal vegigmegyunk a szotaron, a kulcsokat fogjuk visszakapni!!! A szotar iteralhato
# for kulcs in szemely:
#     print(f"A {kulcs} kulcs erteke: {szemely.get(kulcs)}")

for kulcs, ertek in szemely.items():
    print(f"A {kulcs} kulcs erteke: {ertek}")