#Oppgave 1
def er_delstreng(a,b):
    print(a in b)

streng1='abc'
streng2='abcdefg'

er_delstreng(streng1,streng2)

#Oppgave 2
def antall_ord(tekst):
    print(len(tekst.split()))

antall_ord('Hallo verden')

#Oppgave 3
def større_enn_fem(listen):
    for i in listen:
        if len(i)>4:
            print(i, end=', ')

større_enn_fem(['eple','pære','banan','drue','ananas'])

def større_enn_n(listen,n):
    for i in listen:
        if len(i)>=n:
            print(i,end=', ')

større_enn_n(['eple','pære','banan','drue','ananas'],4)

#Oppgave 4
print()
def palindrom(tekst):
    print(tekst==tekst[::-1])

palindrom('radar')
palindrom('hei')

#Oppgave 5
def reverse_sentences(liste):
    ny_liste=[]
    for i in liste:
        ny_liste.append(i[::-1])
    print(ny_liste)

reverse_sentences(['Hei','verden','!','Jeg','elsker','Python'])
