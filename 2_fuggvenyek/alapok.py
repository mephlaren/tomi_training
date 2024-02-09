#A fuggvenyek utasitasok sorat tartalmazza, meghivasra lefutnak. Ketfele fuggvenyrol beszelhetunk: Az egyiknek van, a masiknak NINCS visszateresi erteke! (void)
#fgv. letrehozasa:
def hello():
    print("Hello!")

hello()

#mi valtozott? A fgv. kapott egy parametert (nev), amit fel tud hasznalni.
def koszonto(nev):
    print(f"Hello {nev}!")

koszonto("Gabor")

#visszateresi ertekek
#alapesetben nincs!
def osszead(a, b):
    print(a + b)

osszead(1, 4)

#Akarhol van a fgv. belul a return kulcsszo, OTT VISSZATER
def osszead1(a,b):
    eredmeny = a + b

    return eredmeny

osszeadas_eredmenye = osszead1(1,6)
print(osszeadas_eredmenye)

#A scope lefele epul, egy alarendelt scope (pld. fgv) hozza fer egy felsobbrendu scope ertekehez (pld. root scope)
pi = 3.14
def kor_kerulete(r):
    return 2 * r * pi

k = kor_kerulete(4)
print(k)