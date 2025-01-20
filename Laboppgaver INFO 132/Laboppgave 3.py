#Oppgave 1
alder=int(input('Angi din alder:'))
if alder<=20:
    print('Etter å ha drukket den magiske drikken, er du nå',alder+10,'år gammel!')
else:
    print('Etter å ha drukket den magiske drikken, er du nå',alder-5,'år gammel!')

#Oppgave 2
inntekt=float(input('Hva er din årlige inntekt:'))
if inntekt>500000:
    print('Du har 30'+'%','skatt og skal betale', inntekt*0.3,'basert på din inntekt.')
else:
    print('Du har 20'+'%','skatt og skal betale', inntekt*0.2,'basert på din inntekt.')

#Oppgave 3
forbruk=int(input('Hvor mange kilowattimer (KWh) bruker du i måneden: '))
if forbruk<200:
    print('Du har et lavt energiforbruk.')
if forbruk>200 and forbruk<=500:
    svar=input('Bruker du energisparende apparater? (ja/nei):')
    if svar=='ja':
        print('Bra jobbet med å redusere energiforbruket!')
    elif svar=='nei':
        print('Vurder å bruk energisparende apparater for å få ned forbruket ditt.')
    else:
        print('Whack!')
else:
    print('Vurder å bruk energisparende apparater for å få ned forbruket ditt')

#Oppgave 4

alder=int(input('Hvor gammel er du:'))
if alder>=18:
    har_stemt=input('Har du allerede stemt (ja/nei):')
    if har_stemt=='nei':
        parti=input('Hvilket parti vil du stemme på:')
        print('Du stemte på:', parti)
    else:
        print('Du kan ikke stemme mer enn en gang')
else:
    print('Du er for ung til å stemme.')

#Oppgave 5

import random
tall=random.randint(1,3)
input('Still et spørsmål\n')
if tall==1:
    print ('Ja')
if tall==2:
    print ('Nei')
if tall==3:
    print ('Kanskje')