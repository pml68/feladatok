#!/bin/python3

szavak = []

with open("szoveg.txt", "r", encoding="utf-8") as f:
    szavak = [line.strip() for line in f.readlines()]

szo = input("Szó: ")

van_mgh = False

for i in szo:
    if i in ['a', 'e', 'i', 'o', 'u']:
        van_mgh = True

print("Van benne magánhangzó.") if van_mgh else print("Nincs benne magánhangzó.")

print(f'Az állomány {len(szavak)} szót tartalmaz.')

leghosszabb = szavak[0]

for i in szavak:
    if len(i) > len(leghosszabb):
        leghosszabb = i

print(f'A leghosszabb szó a(z) {leghosszabb}, hosszúsága {len(leghosszabb)} karakter.')

a_val_kezdodik_vegzodik = [i for i in szavak if i[0] == "a" and i[-1] == "a"]

print(" ".join(a_val_kezdodik_vegzodik))

print(f'{len(a_val_kezdodik_vegzodik)}/{len(szavak)}: {len(a_val_kezdodik_vegzodik)*100/len(szavak):.2f}%')

ot_karakteres = [f'{i}\n' for i in szavak if len(i) == 5]

with open("otkarakteres.txt", "w", encoding="utf-8") as f:
    f.writelines(ot_karakteres)
