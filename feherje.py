#1. feladat

txt = open(r'..\feherje_feladat\aminosav.txt', 'r')
sor = txt.readline()

tablazat = {'G': (2, 5, 2, 1, 0), 'A': (3, 7, 2, 1, 0), 'R':(6, 14, 2 ,4, 0), 'F' :(9, 11, 2, 1, 0), 'C' :(3, 7, 2, 1, 1), 'W' :(11, 12, 2 ,2, 0), 'V':(5, 11, 2, 1, 0),
            'L':(6, 13, 2, 1, 0) ,'I' :(6, 13 ,2 ,1 ,0), 'M' :(5, 11, 2, 1, 1), 'P' :(5, 9, 2, 1, 0), 'S' :(3, 7, 3, 1 ,0),
            'T': (4, 9, 3, 1, 0), 'N': (4 ,8 ,3 ,2 ,0),  'Q' :(5, 10, 3, 2, 0), 'Y': (9, 11, 3, 1, 0), 'H': (6, 9 ,2 ,3 ,0),
            'K': (6, 14, 2, 2, 0), 'D': (4, 7, 4, 1, 0), 'E' :(5, 9 ,4 ,1 ,0)}


molekula_tomeg = (12, 1, 16, 14, 32)

#2. feladat

beolvasott = []
reszenkent_beolvasott = []


while sor != '':
    reszenkent_beolvasott = []
    for i in range(7):
        reszenkent_beolvasott.append(sor.strip())
        sor = txt.readline()

    beolvasott.append(reszenkent_beolvasott)

txt.close()

tablazat_szotar = {}

for i in range(len(beolvasott)):
    tablazat_szotar[beolvasott[i][1]] = tuple(int(szam) for szam in beolvasott[i][2:7])

mol_tomegek = {}

for kulcs in tablazat_szotar.keys():
    tomeg = 0
    for index in range(len(tablazat_szotar[kulcs])):
        tomeg += tablazat_szotar[kulcs][index]*molekula_tomeg[index]

    mol_tomegek[kulcs] = tomeg


#3. feladat

rendezett_lista = []
maxhoz = 0
max_kulcs = 0

while len(mol_tomegek.keys()) != 0:
    maxhoz = 0
    max_kulcs = 0
    for kulcs, ertek in mol_tomegek.items():
        if ertek > maxhoz:
            maxhoz = ertek
            max_kulcs = kulcs

    rendezett_lista.append(tuple([max_kulcs, mol_tomegek.pop(max_kulcs)]))

fajl = open(r'..\feherje_feladat\eredmeny.txt', 'w')

for i in range(len(rendezett_lista)):
    print(f'{rendezett_lista[-i-1][0]} {rendezett_lista[-i-1][1]}')
    fajl.writelines(f'{rendezett_lista[-i-1][0]} {rendezett_lista[-i-1][1]}\n')



#4. feladat

c = 0
h = 0
s = 0
o = 0
n = 0
bsa_sorok_szama = 0
osszeg_tuple = ()


bsa_txt = open(r'..\feherje_feladat\bsa.txt', 'r')
sor = bsa_txt.readline()
bsa_lista = []

while sor != '':
    bsa_sorok_szama += 1
    bsa_lista.append(sor.strip())
    sor = bsa_txt.readline()


for i in range(bsa_sorok_szama):
    osszeg_tuple = tablazat_szotar[bsa_lista[i]]
    c += osszeg_tuple[0]
    h += osszeg_tuple[1]
    o += osszeg_tuple[2]
    n += osszeg_tuple[3]
    s += osszeg_tuple[4]

h = h-2*(bsa_sorok_szama-1)
o = o-bsa_sorok_szama+1

print(f'C {c} H {h} O {o} N {n} S {s}')
fajl.writelines(f'C {c} H {h} O {o} N {n} S {s}')
fajl.close()

#5. feladat

atmeneti_hasitas = []
hasitas = []
hasitok = tuple(['Y', 'W', 'F'])
leghosszabb_darab = 0
kezdet_helye = 0

for i in range(bsa_sorok_szama):
    atmeneti_hasitas.append(bsa_lista[i])
    if bsa_lista[i] in hasitok:
        hasitas.append(atmeneti_hasitas)
        atmeneti_hasitas = []

for i in range(len(hasitas)):
    if leghosszabb_darab < len(hasitas[i]):
        leghosszabb_darab = len(hasitas[i])

hasitas_darab = 0

while len(hasitas[hasitas_darab]) != leghosszabb_darab:
    kezdet_helye += len(hasitas[hasitas_darab])
    hasitas_darab += 1

print(f"A leghosszabb lánc hossza: {leghosszabb_darab} Kezdet helye: {kezdet_helye} Végének a helye: {kezdet_helye+leghosszabb_darab}")

hasitok = tuple(['R'])
atmeneti_hasitas = []
hasitas = []

for i in range(bsa_sorok_szama-1):
    atmeneti_hasitas.append(bsa_lista[i])
    if bsa_lista[i] in hasitok and (bsa_lista[i+1] == 'A' or bsa_lista[i+1] == 'V'):
        hasitas.append(atmeneti_hasitas)
        break

cisztein = 0

for i in range(len(hasitas[0])):
    if "C" == hasitas[0][i]:
        cisztein += 1

print(f"{cisztein} darab Ciszteint tartalmaz az első fehérjelánc.")
input("A program Enter lenyomása után bezárul...")