#Oppgave 1
def bergegn_tips(sum,prosent=10):
    print(sum*prosent/100)

bergegn_tips(1500,prosent=15)

#Oppgave 2
def alderstest(alder):
    if alder>=18:
        print('Du er gammel nok til å kjøre bil')
    elif alder<18:
        print('Du må vente', 18-alder, 'år til før du kan kjøre bil')

alderstest(16)
alderstest(19)

#Oppgave 3
import random
def gjett_tall():
    tall=random.randint(1,10)
    print(tall)
    forsøk_en=int(input('Gjett et tall mellom 1 og 10 (1 av 3 forsøk):'))
    if forsøk_en == tall:
        print('Gratulerer du gjettet riktig')
    else:
        if forsøk_en>tall:
            forsøk_to=input(int('For høyt!\nGjett et tall mellom 1 og 10 (forsøk 2 av 3):'))
        elif forsøk_en<tall:
            forsøk_to=input(int('For lavt!\nGjett et tall mellom 1 og 10 (forsøk 2 av 3):'))
        if forsøk_to==tall:
            print('Gratulerer du gjettet riktig')
        if forsøk_to!=tall:
            if forsøk_to>tall:
                forsøk_tre=input(int('For høyt!\nGjett et tall mellom 1 og 10 (forsøk 3 av 3):'))
            if forsøk_to<tall:
                forsøk_tre=input(int('For lavt!\nGjett et tall mellom 1 og 10 (forsøk 3 av 3):'))
            if forsøk_tre==tall:
                print('Gratulerer du gjettet riktig')
            if forsøk_tre!=tall:
                print('Det var synd')

gjett_tall()