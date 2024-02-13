#!/bin/python3

szavak = []

betu_kulcsok = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

with open("szavak.txt", "r", encoding="utf-8") as f:
    szavak = [line.strip() for line in f.readlines()]

def betuKod(betu) -> str:
    for i in betu_kulcsok:
        if betu in i:
            szam = str(betu_kulcsok.index(i) + 2)
            mennyiseg = i.index(betu) + 1
            return szam * mennyiseg

    return "Ilyen betű nem létezik"

def szoKod(szo) -> str:
    return "".join([betuKod(i) for i in szo])

betu = input("Betű: ")
print(betuKod(betu))

szo = input("\nSzó: ")
szo = szoKod(szo)
print(szo)

leghosszab_szo = szavak[0]

for i in szavak:
    if len(i) > len(leghosszab_szo):
        leghosszab_szo = i

print(f'\nA leghosszabb szó a(z) {leghosszab_szo}, hosszúsága {len(leghosszab_szo)} karakter.')

rovid_szavak = 0

for i in szavak:
    if 6 > len(i):
        rovid_szavak += 1

print(f'\nAz állományban {rovid_szavak} rövid szó található.')

szo_kodok = [f'{szoKod(szo)}\n' for szo in szavak]

with open("kodok.txt", "w", encoding="utf-8") as f:
    f.writelines(szo_kodok)
