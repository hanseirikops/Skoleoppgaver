#oppgave 6
import random
maskinvalg=random.randint(1,3)
brukervalg=int(input('Velg (1=papir, 2=saks eller 3 sten): '))
print('maskinen valgte', maskinvalg)
print('Jeg vant: ', (maskinvalg-brukervalg)%3==1)
print('Uavgjort: ', maskinvalg==brukervalg)
print('Maskinen vant: ',(brukervalg-maskinvalg)%3==1)

#Oppgave 7a)
#1.
print(2*3+4**5)
print(2*3+(4**5))
print((2*3)+(4**5))
#2.
print(6**5-4/3*2+1)
print((6**5)-4/3*2+1)
print((6**5)-(4/3)*2+1)
print((6**5)-((4/3)*2)+1)
#3.
print(1+2+3*4/5*6-7*8)
print(1+2+(3*4)/5*6-(7*8))
print((1+2)+((3*4)/5)*6-(7*8))
print(((1+2)+((3*4)/5)*6)-(7*8))
#b)
print(6+5*4/2-1)
print(4*2**2-3**2*3**2-3*2)
print((6+5)*4/2-1)
print(4*2**2-3**2*3**2-3*2)
#c)
print (2+4%4==0)
print(2-4%4==0)
print(4%6-2==2)
#%ligger på samme sted som +-