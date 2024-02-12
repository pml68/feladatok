#!/bin/python3

szavazatok = []

with open("szavazatok.txt", "r", encoding="utf-8") as f:
    szavazatok = [line.split() for line in f.readlines()]

keruletek, szavazatok_szama, vezeteknevek, keresztnevek, partok = zip(*szavazatok)

print(f'A helyhatósági választáson {len(szavazatok)} képviselőjelölt indult.')

vezeteknev = input("Vezetéknév: ")
keresztnev = input("Keresztnév: ")

if vezeteknev in vezeteknevek and keresztnev in keresztnevek and vezeteknevek.index(vezeteknev) == keresztnevek.index(keresztnev):
    print(f'{vezeteknev} {keresztnev} {szavazatok_szama[vezeteknevek.index(vezeteknev)]} szavazatot kapott a választásokon.')
else:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")

reszvevo_szazalek = sum([int(i) for i in szavazatok_szama])*100/12345

print(f'A választáson {sum([int(i) for i in szavazatok_szama])} állampolgár, a jogosultak {reszvevo_szazalek:.2f}%-a vett részt.')

part_szavazatok = [0 for _ in range(5)]

for i in szavazatok:
    match i[4]:
        case "GYEP":
            part_szavazatok[0] += int(i[1])
        case "HEP":
            part_szavazatok[1] += int(i[1])
        case "TISZ":
            part_szavazatok[2] += int(i[1])
        case "ZEP":
            part_szavazatok[3] += int(i[1])
        case _:
            part_szavazatok[4] += int(i[1])

print(f'Gyümölcsevők Pártja = {part_szavazatok[0]*100/sum([int(i) for i in szavazatok_szama]):.2f}%')
print(f'Húsevők Pártja = {part_szavazatok[1]*100/sum([int(i) for i in szavazatok_szama]):.2f}%')
print(f'Tejivók Szövetsége = {part_szavazatok[2]*100/sum([int(i) for i in szavazatok_szama]):.2f}%')
print(f'Zöldségevők Pártja = {part_szavazatok[3]*100/sum([int(i) for i in szavazatok_szama]):.2f}%')
print(f'Független jelöltek = {part_szavazatok[4]*100/sum([int(i) for i in szavazatok_szama]):.2f}%')

szavazatok_szama = [int(i) for i in szavazatok_szama]

gyoztes_index = szavazatok_szama.index(max([i for i in szavazatok_szama]))

if partok[gyoztes_index] == "-":
    gyoztes = f'{szavazatok_szama[gyoztes_index]} {vezeteknevek[gyoztes_index]} {keresztnevek[gyoztes_index]} független'
else:
    gyoztes = f'{szavazatok_szama[gyoztes_index]} {vezeteknevek[gyoztes_index]} {keresztnevek[gyoztes_index]} {partok[gyoztes_index]}'

with open("gyoztes.txt", "w", encoding="utf-8") as f:
    f.write(gyoztes)
