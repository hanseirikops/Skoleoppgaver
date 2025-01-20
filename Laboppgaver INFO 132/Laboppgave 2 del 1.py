#Oppgave 1
#Exercise 1
5
x=5
x+1

#Exercise 2
navn=input('Enter your name: ')
print('Hello ', navn)

#Exercise 3
antall_timer=float(input('Enter hours: '))
timelønn=float(input('Enter rate: '))
print('Pay: ', antall_timer*timelønn)

#Exercise 4
width=17
height=12.0
#Jeg tror svaret av width//2 er 8
print(width//2)
#jeg tror svaret av widt/2.0 er 8,5
print(width/2.0)
#jeg tror svaret av height/3 er 4.0
print(height/3)
#jeg tror svaret av 1+2*5 er 11
print(1+2*5)

#Oppgave 2
start_tall=int(input('Fra: '))
slutt_tall=int(input('Til: '))

#Oppgave 3
import random
antall_spørsmålstegn=random.randint(0,9999)
print('?'*antall_spørsmålstegn)
gjetting=int(input('Gjett antall spørsmåltegn: '))
print('That`s', gjetting==antall_spørsmålstegn, '!')
if gjetting!=antall_spørsmålstegn:
    print (antall_spørsmålstegn, 'er det riktige svaret.')

#Oppgave 4
import math
siffer_1=input('1. siffer: ')
siffer_2=input('2. siffer: ')
tall1=siffer_1+siffer_2
tall2=siffer_2+siffer_1
tall1int=int(tall1)
tall2int=int(tall2)
print('Kvadratroten av', tall1, '*', tall2, '=', math.sqrt(tall1int*tall2int))

#Oppgave 5
tresifret_tall=input('Oppgi et tresifret tall: ')
tosifret_tall=int(tresifret_tall)%100
et_siffer=str(int(tresifret_tall)//100)
minste_siffer=min(str(tosifret_tall))
største_siffer=max(str(tosifret_tall))
print('Permutasjoner: ',et_siffer+minste_siffer+største_siffer, et_siffer+største_siffer+minste_siffer,minste_siffer+et_siffer+største_siffer, minste_siffer+største_siffer+et_siffer,største_siffer+et_siffer+minste_siffer, største_siffer+minste_siffer+et_siffer)