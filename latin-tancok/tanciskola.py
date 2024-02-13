#!/bin/python3

tancok = []

with open("tancrend.txt", "r", encoding="utf-8") as f:
    adatok = [line.strip() for line in f.readlines()]
    tancok = [adatok[i*3:i*3+3] for i in range(len(adatok) // 3)]

print("2. feladat:")
print(f'Az iskola tanulói összesen {len(tancok)} tancot adatak elő.')

print("\n3. feladat:")
print(f'Az első táncot {tancok[0][1]} táncolta.')

samba_bemutatok = 0

for i in tancok:
    if i[0] == "samba":
        samba_bemutatok += 1

print("\n4. feladat:")
print(f'A sambát {samba_bemutatok} pár mutatta be.')

print("\n5. feladat:")
valasztott_tanc = input("Tánc: ")

luca_par_szoveg = ""

for i in tancok:
    if i[0] == valasztott_tanc and i[1] == "Luca":
        luca_par_szoveg = f'A {valasztott_tanc} bemutatóján Luca párja {i[2]} volt.'
        break
    else:
        luca_par_szoveg = f'Luca a {valasztott_tanc} táncot nem táncolta'
        continue

print(luca_par_szoveg)

fiuk = [sor[2] for sor in tancok]
fiuk = list(dict.fromkeys(fiuk))

with open("fiuk.txt", "w", encoding="utf-8") as f:
    f.writelines([f'{fiu}\n' for fiu in fiuk])
