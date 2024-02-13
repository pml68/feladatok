#!/bin/python3

fizetesek = [[]]

befejezesek = []

with open("penztar.txt", "r", encoding="utf-8") as f:
    adatok = [line.strip() for line in f.readlines()]
    for i in adatok:
        if i == "F":
            fizetesek.append([])
        else:
            fizetesek[-1].append(i)

fizetesek.pop(-1)

print("2. feladat:")
print(f'A fizetések száma: {len(fizetesek)}')

print("\n3. feladat:")
darabszam = int(input("Darabszám: "))

def fizetendo(darabszam) -> int:
    ar_per_darab = 500
    ar = 0
    for i in range(darabszam):
        if ar_per_darab > 400:
            ar += ar_per_darab
            ar_per_darab -= 50
        else:
            ar += ar_per_darab
    return ar

print(f'{darabszam} vételekor fizetendő: {fizetendo(darabszam)} Ft')

print("\n4. feladat:")
print(f'Az első vásárló {len(fizetesek[0])} darab árucikket vásárolt.')

minden_termek = []

for i in fizetesek:
    minden_termek += i

leghosszabb = minden_termek[0]

for i in minden_termek:
    if len(i) > len(leghosszabb):
        leghosszabb = i

with open("hosszu.txt", "w", encoding="utf-8") as f:
    f.write(f'A leghosszabb terméknév a(z) {leghosszabb}, hosszúsága {len(leghosszabb)} karakter.')

print("\n6. feladat:")
for i in fizetesek:
    print(f'{fizetesek.index(i) + 1}: {fizetendo(len(i))} Ft')
