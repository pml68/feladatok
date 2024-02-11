#!/bin/python3
from random import choice, randint

aminosavak = []

with open("aminosav.txt", "r", encoding="utf-8") as f:
    aminosavak = [line.split() for line in f.readlines()]

for i in aminosavak:
    i.append(int(i[2])*12 + int(i[3])*1 + int(i[4])*16 + int(i[5])*14 + int(i[6])*32)

print("3. feladat:")

for i in range(len(aminosavak)):
    for j in range(len(aminosavak)):
        if aminosavak[i][7] < aminosavak[j][7]:
            temp = aminosavak[i]
            aminosavak[i] = aminosavak[j]
            aminosavak[j] = temp

for i in aminosavak:
    print(f'{i[0]} {i[7]}')

bsa = ""

for i in range(randint(1,1000)):
    bsa += choice([i[1] for i in aminosavak])

with open("bsa.txt", "w", encoding="utf-8") as f:
    f.write(bsa)

bsa_osszegkeplet = [0 for _ in range(5)]

_, betuk, _, _, _, _, _, _ = zip(*aminosavak)

for i in bsa:
    for j in range(5):
        bsa_osszegkeplet[j] += int(aminosavak[betuk.index(i)][2:7][j])

for i in range(len(bsa) - 1):
    bsa_osszegkeplet[1] -= 2
    bsa_osszegkeplet[2] -= 1

osszegkeplet = f'C {bsa_osszegkeplet[0]} H {bsa_osszegkeplet[1]} O {bsa_osszegkeplet[2]} N {bsa_osszegkeplet[3]} S {bsa_osszegkeplet[4]}'

print("\n4. feladat:")
print(osszegkeplet)

with open("eredmeny.txt", "w", encoding="utf-8") as f:
    f.writelines([f'{i[0]} {i[7]}\n' for i in aminosavak])
    f.writelines(osszegkeplet)
