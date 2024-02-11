#!/bin/python3
lotto_szamok = []

with open("lottosz.txt", "r", encoding="utf-8") as f:
    lotto_szamok = f.readlines()
    for i in range(len(lotto_szamok)):
        lotto_szamok[i] = lotto_szamok[i].split()
        for j in range(5):
            lotto_szamok[i][j] = int(lotto_szamok[i][j])

utolso_het = []

for i in range(1, 6):
    szam = int(input(f'{i}. szám: '))
    while szam > 90 or szam < 1:
        szam = int(input(f'{i}. szám: '))

    utolso_het.append(szam)

lotto_szamok.append(utolso_het)

het_sorszam = int(input("A hét sorszáma: "))

while het_sorszam > 52 or het_sorszam < 1:
    het_sorszam = int(input("A hét sorszáma: "))

for i in lotto_szamok[het_sorszam - 1]:
    print(i, end=" ")

print("")

hany_42 = 0
paratlan_szamok = 0

# 4. feladat
for i in lotto_szamok:
    if 42 in i:
        hany_42 += 1
    #5. feladat
    for j in i:
        if j % 2 != 0:
            paratlan_szamok += 1

print(f'A 42-es számot {hany_42} alkalommal húzták ki az 52 hét során.')
print(f'Az 52 hét során {paratlan_szamok} alkalommal húztak ki páratlan számot.')

statisztika = [0 for _ in range(90)]

for i in lotto_szamok:
    for j in i:
        statisztika[j - 1] += 1

for i in range(len(statisztika)):
    statisztika[i] = f'{i+1}: {statisztika[i]} db\n'

with open("statisztika.txt", "w", encoding="utf-8") as f:
    f.writelines(statisztika)
