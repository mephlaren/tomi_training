#a tobb dimenzios listaba nem egyes ertekek kerulnek, hanem egyeb listadimenziok
# van egy koordinata mezonk:
# | 1,1 | 1,2 | 1,3 |
# | 2,1 | 2,2 | 2,3 |
# | 3,1 | 3,2 | 3,3 |
# | 4,1 | 4,2 | 4,3 |
# | 5,1 | 5,2 | 5,3 |

#Egy tombon belul a tomb indexen kulon tomboket tudok eltarolni!
koordinatak = [
    [1,1], [1,2], [1,3],
    [2,1], [2,2], [2,3],
    [3,1], [3,2], [3,3],
    [4,1], [4,2], [4,3],
    [5,1], [5,2], [5,3],
]

#print(koordinatak)
#egyszeru for-ciklus:
# for i in range(0, len(koordinatak)):
#     print(f"index: {i}, ertek: {koordinatak[i]}")

#for-each ciklus
# for kulso in koordinatak:
#     for belso in kulso:
#         print(f"Az aktualis matrix erteke: {belso}")

#szorzotabla
for szorzo in range(1,10+1):
    for szorzando in range(1,10+1):
        szorzat = szorzo * szorzando
        print(f"{szorzo}*{szorzando}={szorzat}")