#!/bin/python3

tavok = []

with open("tavok.txt", "r", encoding="utf-8") as f:
    tavok = [[int(i) for i in line.split()] for line in f.readlines()]

print("2. feladat:")
print(f'A hét legelső útja {[i[2] for i in tavok if i[0] == 1 and i[1] == 1][0]} km hosszú volt.')

fuvarok_szama = [0 for _ in range(7)]

for i in tavok:
    if i[1] > fuvarok_szama[i[0] - 1]:
        fuvarok_szama[i[0] - 1] = i[1]

legtobb_fuvar = 0

for i in range(len(fuvarok_szama)):
    if fuvarok_szama[i] > fuvarok_szama[legtobb_fuvar]:
        legtobb_fuvar = i

print("\n3. feladat:")
print(f'A hét {legtobb_fuvar + 1}. napján volt a legtöbb fuvar.')

"""
1 – 2 km 	500 Ft
3 – 5 km 	700 Ft
6 – 10 km 	900 Ft
11 – 20 km 	1 400 Ft
21 – 30 km 	2 000 Ft
"""

print("\n4. feladat:")

tavolsag = int(input("Távolság (km): "))

def tavolsagFizetes(tavolsag):
    if 3 > tavolsag:
        dijazas = 500
    elif 6 > tavolsag > 2:
        dijazas = 700
    elif 11 > tavolsag > 5:
        dijazas = 900
    elif 21 > tavolsag > 10:
        dijazas = 1400
    else:
        dijazas = 2000

    return dijazas

dijazas = tavolsagFizetes(tavolsag)

print(f'Díjazás: {dijazas} Ft')

fizetes = 0

for i in tavok:
    fizetes += tavolsagFizetes(i[2])

with open("eredmeny.txt", "w", encoding="utf-8") as f:
    f.write(f'{fizetes} Ft')
