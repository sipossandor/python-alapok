# mehívjuk a print fügvényt és átadjuk neki a 'Hello world' stringet
#a kekettőskeresztel kezdödő sorokat a python nem értelmezi
# a kettőskeresztel kezdödő sorok comment-ek


print('Hello world')
#létrehoztunk egy szöveg nevű változót , az értéke pedig 
# 'sziasztok!' karakterlánc
# ha egy darab egyenlőséget látunk a kódban az minden esetben 
#értékadást jelent. Az egyenlőségjel jobb oldala bekerül az
#egyenlőségjel bal oldalán lévő változóba.

szoveg ='sziasztok!'
print(szoveg)
#szekvencia: a program az utasításokat (sorokat) soronként #hajtja végre egymás után
#a következő sor hibát dobna , mert nem hoztuk még létre a #szoveg2 változót
#print (szoveg2)
szoveg2 = "alma"
#meghívjuk a format fgv-t az aposztrof közötti szövegre
print ('a szoveg2 értéke: {}'.format(szoveg2))
#megnézzük a szöveg2 változó típusát:
print(type(szoveg2))

#ha valahol látunk egy sima zárójelet és előtte valami #szöveget pl.: sdfsdsdf
#ez egy függvényhívást jelent , a függyvény neve a 
# nyitó zárójel elötti rész



#python autocomplete funkció , help ablakkal!!
#autocomplete=intellisence=code complete

print('a szoveg valtozo erteke: {} a szoveg2 valtozo {}'.format(szoveg, szoveg2))
#létrehozuk a szám nevű változót és az érték amit kap ez a változó
#az egy szám lesz (nincs körütötte aposztrof , vagy idézőjel)
#dinamically typed programming language: a változók típusát
#létrehozáskor (deklaráláskor) automatikusan megpróbálja kitalálni
#a futtató környezet (python)
szam = 34
print(type(szam))
szam1 = 10
print (szam+szam1)

#növeljük egyel a a szám változó értékét
szam = szam + 1
#az előző sor rövidebben:
szam +=1
print(szam)

# string = szöveg
# int (integer) = szám

#boolean tipusú változó , két értéke lehet:True vagy False
kapcsolo = True
print(type(kapcsolo))

#elágazás egy olyan kód blokk ami egy adott feltétel alapján
#vagy lfut vagy nem..

if kapcsolo is True:
    print(' A kapcsoló fel van kapcsolva')

print('ez már az if blokkon kívül van..')

a = 3
b = 4

if a > b:
    print('az nagyobb mint b')
else:
    print('a nem nagyobb mint b')


#ciklus: egy adott kódrész többször fut le
#egy adott feltétel szerint

szam = 10
while szam > 0:
    print('a szám változóbol levonunk 1-et: {}'.format(szam))
    #szam = szam - 1
    szam -= 1

#a kapcsos zárójel a python-ban a lista típusú változót jelenti
#a kapcsos zárójelen belülre írjuk a lista elemeit
#a listába több elemet is el lehet tárolni
#más programozási nyelvek ezt tömb-nek hívják
nevsor = ['Pista', 'Kata' , 'Tibor' ] 

#a for ciklus legtöbbször arra használjuk hogy
#végig menjünk egy lista összes elemén és az elemeken
#valamilyen műveletet végezzünk
for nev in nevsor:
    print('a névsorban szerepel: {} '.format(nev))

# pythonban a lista elemeit nullától indexeljük
for index, nev in enumerate(nevsor):
    print('{} : {} '.format(index, nev))

print('a nevsor nulladik eleme: {} '.format(nevsor[0]))


