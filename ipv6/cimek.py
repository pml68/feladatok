#!/bin/python3

cimek = []

with open("ip.txt", "r", encoding="utf-8") as f:
    cimek = [i.split('\n')[0] for i in f.readlines()]

print("2. feladat:")
print(f'Az állományban {len(cimek)} darab adatsor van.\n')

print("3. feladat:")
print("A legalacsonyabb tárolt IP-cím:")
print(min(cimek) + "\n")

print("4. feladat:")
print(f'Dokumentációs cím: {len([i for i in cimek if i[:9] == "2001:0db8"])}')
print(f'Globális egyedi cím: {len([i for i in cimek if i[:7] == "2001:0e"])}')
print(f'Helyi egyedi cím: {len([i for i in cimek if i[:2] == "fc" or i[:2] == "fd"])}\n')

sortxt_sorok = []

for i in cimek:
    nullak = 0
    for j in i:
        if j == "0":
            nullak += 1

    if nullak > 17:
        sortxt_sorok.append(f'{cimek.index(i) + 1} {i}')

with open("sor.txt", "w", encoding="utf-8") as f:
    f.writelines(sortxt_sorok)

print("6. feladat:")
sorszam = int(input("Kérek egy sorszámot: "))
print(cimek[sorszam-1])
