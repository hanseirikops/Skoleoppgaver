#Oppgave 1
def skriv_tall(fra,til):
    for fra in range(fra,til):
        print(fra)
        fra+=1
    print(til)

skriv_tall(3,7)

#Oppgave 2
def delbar_3(tall):
    for i in range (1,tall+1):
        if i %3==0:
            print(i)
            print('delbar på 3')
        else:
            print(i)
            i+=1

delbar_3(5)

#Oppgave 3
def sum_partall(tall1):
    sum=0
    for i in range (0,tall1+1,2):
        sum+=i
    print(sum)

sum_partall(10)

#Oppgave 4

def gjennomsnitt(en_liste):
    if len(en_liste)==0:
        return 0
    else:
        print(sum(en_liste)/len(en_liste))

liste=[2,4,6,8,10]
gjennomsnitt(liste)

#Oppgave 5

def stjernepyramide(lengde=3):
    if lengde not in range(1,10):
        lengde=3
    for i in range(lengde):
        print((i)*'*')
        i+=1
    for j in range(lengde):
        print((lengde-j)*'*')

stjernepyramide(4)
stjernepyramide()
stjernepyramide(50)

#Oppgave 6

def antall_tegn(tekst,bokstav):
    antall=tekst.count(bokstav)
    if antall==0:
        print('Tegnet',bokstav,'ble ikke funnet.')
    else:
        print(bokstav,'ble funnet', antall, 'ganger.')

antall_tegn('Hei på deg','a')
antall_tegn('Hei på deg', 'e')

#Oppgave 7
import random
def gjette_spill():
    tall=random.randint(1,100)
    gjetting=int(input('Gjett et tall:'))
    teller=1
    while gjetting!=tall:
        if gjetting>tall:
            print('For høyt!')
        else:
            print('For lavt!')
        gjetting=int(input('Gjett et tall:'))
        teller+=1
    print('Gratulerer, du gjettet riktig! Det tok deg', teller, 'forskøk.')

#gjette_spill()

#Oppgave 8
def multiplikajsonstabell(n):
    for i in range(n):
        i+=1
        for j in range(n):
            j+=1
            print(j*i,' ', end='')
        print()

multiplikajsonstabell(3)
multiplikajsonstabell(5)