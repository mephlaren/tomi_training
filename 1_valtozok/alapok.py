# valtozo deklarasa
kor = 28
# 3 reszbol all a deklaralt valtozo:
# (tipus) neve erteke -> a tipus pythonban nem szamit, ugyanis NEM TIPUSOS NYELV!!!
# mit jelent? a python futasido alatt kitalalja a valtozo tipusat!
nevem = "Gabor"  # ennek koszonhetoen pythonban csak nevet es erteket adunk!
# tipusos nyelvek eseten a tipust EXPLICIT deklaralni kell -> string nevem = "Gabor"
# EXPLICIT tipuskonverzio? Amikor rabirjuk a futtatokornyezetet, hogy az adott valtozo valamilyen tipust vegyen fel!
szul_ev = "1995" # -> alapbol string!
szul_ev_int = int(szul_ev) # -> integerkent szeretnem latni!

#ellenorzes?
print(f"{szul_ev} - {szul_ev_int}")  # -> nem lehetep benne biztos, hogy az egyik tenyleg int lett! Vagy hogy egyaltalan mi a TIPUSUK
#valodi ellenorzes!
print(f"valtozo: szul_ev \ttipusa: {type(szul_ev)}\nvaltozo: szul_ev_int \ttipusa: {type(szul_ev_int)}")
#Escape karakter: a backslash(\). tabulalas: \t uj sor: \n
#print('Can\'t')

#valtozok tipusa:
#string
allat="cica"
jarmu='bicikli'
 
#int
kerekek=4

#float
homerseklet=20.4

#boolean (igaz/hamis)
kek_az_eg=True
zold_az_eg=False

#None
ures_ertek=None