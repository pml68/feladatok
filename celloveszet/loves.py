#!/bin/python3

versenyzok_szama = 0
eredmenyek = []

with open("verseny.txt", "r", encoding="utf-8") as f:
    adatok = f.readlines()
    versenyzok_szama = adatok[0]
    eredmenyek = [line.strip() for line in adatok[1:]]

ket_loves = ""

for i in eredmenyek:
    if i[:2] == "++":
        ket_loves += str(eredmenyek.index(i) + 1) + " "

print(ket_loves)

legtobb_index = 0

for i in range(len(eredmenyek)):
    lovesek = eredmenyek[i].count("+")

    if lovesek > eredmenyek[legtobb_index].count("+"):
        legtobb_index = i

print(f'\nA legtöbb lövést leadó versenyző rajtszáma: {legtobb_index + 1}')

def loertek(sor: str) -> int:
    aktpont = 20
    ertek = 0

    for i in range(len(sor)):
        if aktpont > 0 and sor[i] == "-":
            aktpont -= 1
        else:
            ertek += aktpont

    return ertek

"""
Adjon meg egy rajtszámot! 2

5a. feladat: Célt erő lövések: 2 4 5 6

5b. feladat: Az eltalált korongok száma: 4

5c. feladat: A versenyző pontszáma: 73
"""

statisztika_rajtszam = int(input("\nAdjon meg egy rajtszámot! ")) - 1

celt_ero_lovesek = ""

for i in range(len(eredmenyek[statisztika_rajtszam])):
    if eredmenyek[statisztika_rajtszam][i] == "+":
        celt_ero_lovesek += f'{i + 1} '

print(f'Célt érő lövések: {celt_ero_lovesek}')
print(f'Az eltalált korongok száma: {len([i for i in celt_ero_lovesek.split()])}')
print(f'A versenyző pontszáma: {loertek(eredmenyek[statisztika_rajtszam])}')

eredmenyek = [[eredmenyek.index(i) + 1, i, loertek(i)] for i in eredmenyek]


for i in range(len(eredmenyek)):
    for j in range(len(eredmenyek)):
        if eredmenyek[i][2] > eredmenyek[j][2]:
            temp = eredmenyek[i]
            eredmenyek[i] = eredmenyek[j]
            eredmenyek[j] = temp

sorrend = [f'{i[0]} {i[2]}\n' for i in eredmenyek]

with open("sorrend.txt", "w", encoding="utf-8") as f:
    f.writelines(sorrend)
