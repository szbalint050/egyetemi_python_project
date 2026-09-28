from random import randint as veletlen_szam

def ker_ter (a, b):
    k = 2 * a + 2* b
    t = a * b
    # print(f'Kerület:= {k}')
    return k, t

def lotto ():
    from random import randint
    i = 0
    while i < 5:
        print(randint(1, 90))
        i += 1

# FŐPROGRAM
if __name__ == '__main__':
    felhasznalo_kora = 25 # int(input("Hány éves vagy: "))
    if felhasznalo_kora <= 18:
        print("Gyerek")
    elif felhasznalo_kora <=25:
        print('Ifjú')
    elif felhasznalo_kora <=65:
        print('Koros')
    else:
        print('Nyugger')

    uzenet = 'Gyere be' if felhasznalo_kora >= 18 else "Maradj kint"
    print(uzenet)

    i = 1
    while i < 10:
        i += 1
        if i == 3:
            continue
        if i == 5:
            break
        print(i)
    else:
        print('Gond nélkül lefutott!')
    print('vége a ciklusnak')

    alap = 5
    magassag = 3

    kerulet = ker_ter(alap , magassag)[0]
    terulet = ker_ter(alap , magassag)[1]
    print(f'Kerület = {kerulet}\nTerület = {terulet}')

    eredmeny = ker_ter(alap , magassag)
    print(f'Kerület = {eredmeny[0]}\nTerület = {eredmeny[1]}')

    print(f'Kerület = {ker_ter(alap, magassag)[0]}\nTerület = {ker_ter(alap, magassag)[1]}\n')

    i = 0
    while i < 5:
        print(veletlen_szam(1, 90))
        i += 1
    print()

    lotto()