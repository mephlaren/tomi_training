print("Login fuggveny!")

def belepes(usernev, jelszo):
    if usernev=="sajat" and jelszo=="abcd":
        return "admin ur"  # ->  ezt le tudjuk egyszerusiteni shorthanddel!
    else:
        return None  # -> ezt kivehetjuk, mert a default visszateresi ertek az a None!
    # return "admin ur" if usernev == "admin" and jelszo == "admin" else None  # egyszerusites! ternaris operatorokkal! de inkabb irjuk ki vegig ameg tanulunk!

def print_login(user):
    if user:
        print(f'Sikeresen belepett mint {user}!')
    else:
        print('Hiba a beleptetes folyaman, rossz jelszo, vagy felhasznalonev!')

user = belepes('sajat', 'abcd')
print_login(user)

user = belepes('paci', 'patko')
print_login(user)
