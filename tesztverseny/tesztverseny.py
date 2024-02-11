#!/bin/python3
# 1. feladat
helyes_megoldasok = ""
versenyzok = []
versenyzo_megoldasok = []

with open("valaszok.txt", 'r', encoding="UTF-8") as f:
    data = f.readlines()
    helyes_megoldasok = data[0]
    for i in data[1:]:
        versenyzok.append(i.split()[0])
        versenyzo_megoldasok.append(i.split()[1])
    f.close()

# 2. feladat
print(f'A vetélkedőn {len(versenyzok)} versenyző indult.')

# 3. feladat
kert_versenyzo = input("A versenyző azonosítója = ")

print(versenyzo_megoldasok[versenyzok.index(kert_versenyzo)])

# 4. feladat
print(helyes_megoldasok, end="")

for i in range(len(versenyzo_megoldasok[versenyzok.index(kert_versenyzo)])):
    if versenyzo_megoldasok[versenyzok.index(kert_versenyzo)][i] == helyes_megoldasok[i]:
        print("+", end="")
    else:
        print(" ", end="") 

print("\n")

# 5. feladat
versenyzo_helyes_megoldasok = 0

feladat_sorszam = int(input("A feladat sorszáma = "))

for i in versenyzo_megoldasok:
    if i[feladat_sorszam-1] == helyes_megoldasok[feladat_sorszam-1]:
        versenyzo_helyes_megoldasok += 1
    else:
        continue

helyes_megoldasok_atlag = versenyzo_helyes_megoldasok / len(versenyzok) * 100

print(f'A feladatra {versenyzo_helyes_megoldasok} fő, a versenyzők {helyes_megoldasok_atlag:.2f}%-a adott helyes választ.')

# Általános
def kiir(szoveg):
    with open("pontszam.txt", "w", encoding="UTF-8") as f:
        f.write(szoveg)
        f.close()

# 6. feladat
pontszam_kert_versenyzo = input("A versenyző kódja: ")

if pontszam_kert_versenyzo not in versenyzok:
    kiir("A versenyen nem vett rész ilyen kódszámú versenyző.")
    exit(0)

pontszam = 0

for i in range(len(versenyzo_megoldasok[versenyzok.index(pontszam_kert_versenyzo)])):
    if versenyzo_megoldasok[versenyzok.index(pontszam_kert_versenyzo)][i] == helyes_megoldasok[i]:
        if 4>=i>=0:
            pontszam += 3
        elif 9>=i>=5:
            pontszam += 4
        elif 12>=i>=10:
            pontszam += 5
        elif i == 13:
            pontszam += 6
    else:
        continue

kiir(f'{pontszam_kert_versenyzo} {pontszam} pont')
