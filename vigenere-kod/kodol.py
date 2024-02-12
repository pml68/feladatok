#!/bin/python3
import unicodedata

tabla_sorok = []

with open("vtabla.txt", "r", encoding="utf-8") as f:
    tabla_sorok = [[*line.strip()] for line in f.readlines()]

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = zip(*tabla_sorok)

print("1. feladat:")

nyilt_szoveg = input("Nyílt szöveg: ").replace(",", "").replace(" ", "").strip(".?!").upper()

nyilt_szoveg = unicodedata.normalize("NFKD", nyilt_szoveg).encode("ascii", "ignore").decode("utf-8")

print("\n2. feladat:")
print(f'A szöveg átalakítása: {nyilt_szoveg}')

print("\n3. feladat:")
kulcsszo = input("Kulcsszó: ").upper()
print(f'Kulcsszó nagybetűssé alakítása: {kulcsszo}')

maradek = len(nyilt_szoveg) % len(kulcsszo)

kulcsszoveg = ""

while len(kulcsszoveg) < len(nyilt_szoveg) - maradek:
    kulcsszoveg += kulcsszo

for i in range(maradek):
    kulcsszoveg += kulcsszo[i]

print("\n4. feladat:")
print(f'Kulcsszöveg:  {kulcsszoveg}')

kodolt_szoveg = ""

for i in range(len(nyilt_szoveg)):
    oszlop = a.index(nyilt_szoveg[i])
    sor = tabla_sorok[0].index(kulcsszoveg[i])
    kodolt_szoveg += tabla_sorok[oszlop][sor]

print("\n6. feladat:")
print(f'Kódolt szöveg: {kodolt_szoveg}')

with open("kodolt.txt", "w", encoding="utf-8") as f:
    f.write(kodolt_szoveg)
