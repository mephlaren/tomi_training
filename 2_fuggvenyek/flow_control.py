#Flow control: az ertekek eldontesehez tartozo iranyitas
#Irjunk egy fuggveny, ami megmondja, hogy belephetunk-e a szorakozohelyre. A feltele a belepesnek legalabb 18 eves kor
minimum_kor = 18
max_kor = 80
def beleptetes(kor):
    if kor >= minimum_kor and kor <= max_kor:  # az if mindenkepp lefut!
        return 'Belephetsz'
    elif kor > 80:
        return 'Tul oreg vagy ehhez!'
    else:  # ha barmelyik if False lett (hamis) akkor az else ag ter vissza.
        return 'Nem lephetsz be :('

belepes = beleptetes(112)
#print(belepes)

#Egyeb felhasznalasa az if-nek:
#Az if mindig igazsagot vizsgal! Akkor ertelmezodik, ha az IF feltetele igaz!

# if True:
#     print('true')

az_eg_kek = True
if az_eg_kek:
    print("Valos!")

if 5 == 4:
    print("Valami nem igazan oke!")
else:
    print("A matematika mukodik!")


# Ertekellenorzes!
print("Ertekellenorzes...")
def ertek_ellenorzes(valtozo):
    if valtozo:
        print(f"{valtozo}: A valtozo nem ures, van erteke")
    else:
        print("Ennek a valtozonak NINCS erteke!")

ertek_ellenorzes(5)
ertek_ellenorzes("Paci")
ertek_ellenorzes(None)


# Lehetnek nagyon bonyolult felteltelek is, OR-ral es AND-del
# AND-nel mindket feltetelnek igaznak kell lennie, kulonben hamis
# OR-nal legalabb egy feltetelnek igaznak kell lenni, hogy igazzal terjen vissza. ha mindketto hamis akkor hamissal ter vissza
