#Oppgave 1
#a)
class Parti:
    def __init__(self,partikode,partinavn):
        self.partikode=partikode
        self.partinavn=partinavn
    
    def skriv(self):
        print(self.partinavn, '('+self.partikode+')')

a=Parti('A','Arbeiderpartiet') 
sv=Parti('SV','Sosialistisk Venstreparti') 
rødt=Parti('RØDT','Rødt') 
sp=Parti('SP','Senterpartiet') 
krf=Parti('KRF','Kristelig Folkeparti') 
v=Parti('V','Venstre') 
h=Parti('H','Høyre') 
frp=Parti('FRP','Fremskrittspartiet') 
mdg=Parti('MDG','Miljøpartiet De Grønne') 
nkp=Parti('NKP','Norges Kommunistiske Parti') 
partier=[a,sv,rødt,sp,krf,v,h,frp,mdg,nkp]


#b)
def partiNavn(partikode):
    exists=False
    for parti in partier:
        if parti.partikode==partikode:
            exists=True
            return parti.partinavn
    if exists==False:
        return 'ukjent partikode'


#c)
def partiKode(partinavn):
    exists=False
    for parti in partier:
        if parti.partinavn==partinavn or parti.partikode==partinavn:
            exists=True
            return parti.partikode
    if exists==False:
        return 'ukjent parti'


#d)
class StemmeTall:
    def __init__(self,partikode,antall_stemmer):
        self.partikode=partikode
        self.antall_stemmer=antall_stemmer
    
    def skriv(self):
        print(self.partikode+':',self.antall_stemmer)
    

#e)
def lesStemmer():
    stemmeliste=[]
    for parti in partier:
        stemmer=int(input(f'Antall stemmer for {parti.partinavn}:'))
        ny_stemmetall=StemmeTall(parti.partikode,stemmer)
        stemmeliste=stemmeliste+[ny_stemmetall]
    return stemmeliste

#valgresultat=lesStemmer()

#f)
def finnResultat(valgresultat, partinavn):
    for s in valgresultat:
        if partiKode(partinavn)==s.partikode:
            return s.antall_stemmer


#g)
def flestStemmer(valgresultat):
    flest_stemmer=0
    flest_stemmer_parti=[]
    for s in valgresultat:
        if s.antall_stemmer>flest_stemmer:
            flest_stemmer=s.antall_stemmer
            flest_stemmer_parti=[s.partikode]
        elif s.antall_stemmer==flest_stemmer:
            flest_stemmer_parti=flest_stemmer_parti+[s.partikode]
    
    print('Følgende partier fikk', flest_stemmer, 'stemmer:')
    for parti in flest_stemmer_parti:
        print(partiNavn(parti))

#Oppgave 2
def lesPartier():
    partifil=open('partier.txt', mode='r',encoding='utf-8')
    partier=[]
    for linje in partifil:
        temp=linje.strip().split(',')
        parti=Parti(temp[0],temp[1])
        partier=partier+[parti]
    partifil.close()
    return partier

partier=lesPartier()
for p in partier:
    p.skriv()

#Oppgave 3
#a)
def lesKretser():
    kretsfil=open('kretser.txt', mode='r',encoding='utf-8')
    kretser={}
    for linje in kretsfil:
        temp=linje.strip().split(',')
        kretser[int(temp[0])]=temp[1]
    kretsfil.close()
    return kretser

kretser=lesKretser()

#b)
def kretsNr(kretsnavn):
    svar='ukjent krets'
    for nummer,navn in kretser.items():
        if navn==kretsnavn or nummer==kretsnavn:
            svar=nummer
    return svar


#Oppgave 4
def stemmeTallKonvertering(stemmer):
    fortegnelse={}
    for s in stemmer:
        fortegnelse[s.partikode]=s.antall_stemmer
    return fortegnelse


#Oppgave 5
#a)
def lesValg(årstall,fil,tidligere_år=None):
    år_fil=open(fil,mode='r', encoding='utf-8')
    årsresultat={}
    kretser={}
    for linje in år_fil:
        temp=linje.strip().split(',')
        if temp[0]!='krets':
            if int(temp[0]) not in kretser.keys():
                kretsresultat={}
                kretser[int(temp[0])]=kretsresultat
            kretsresultat[temp[1]]=int(temp[2])
    if tidligere_år!=None:
        årsresultat=tidligere_år
    årsresultat[årstall]=kretser
    år_fil.close()
    return årsresultat


v13=lesValg(2013,'stemmer2013.txt')
v13og17=lesValg(2017,'stemmer2017.txt',v13)
valg=lesValg(2021,'stemmer2021.txt',v13og17)

print(valg)

#Oppgave 6
def stemmerTotalt():
    total=0
    for kretser in valg.values():
        for resultater in kretser.values():
            for partistemmer in resultater.values():
                    total+=partistemmer
    return total


#Oppgave 7
def valgresultat(årstall,krets,parti):
    kretsnr=kretsNr(krets)
    partikode=partiKode(parti)
    if kretsnr=='ukjent krets':
        return kretsnr
    elif partikode=='ukjent parti':
        return partikode
    elif årstall not in valg.keys():
        return 'ukjent år'
    else:
        år=valg[årstall]
        kretsen=år[kretsnr]
        if partikode in kretsen:
            svar=kretsen[partikode]
        else:
            svar='Parti ikke tilstede i valgkrets'
        return svar


#Oppgave 8
def kretsÅr(krets,årstall):
    kretsnr=kretsNr(krets)
    if kretsnr=='ukjent krets':
        return kretsnr
    elif årstall not in valg.keys():
        return 'ukjent år'
    else:
        år=valg[årstall]
        kretsen=år[kretsnr]
        return kretsen


def samlet(årstall):
    totalt={}
    if årstall not in valg.keys():
        return 'ukjent år'
    else:
        år=valg[årstall]
        for resultater in år.values():
            for parti in resultater.keys():
                if parti not in totalt:
                    totalt[parti]=resultater[parti]
                else:
                    totalt[parti]+=resultater[parti]
        return totalt


def prosentvisfordeling(årstall):
    if årstall not in valg.keys():
        return 'ukjent år'
    else:
        total=0
        år=valg[årstall]
        for resultat in år.values():
            for stemmer in resultat.values():
                total+=stemmer
        resultat=samlet(årstall)
        fordeling={}
        for parti in resultat:
            fordeling[parti]=round((resultat[parti]/total)*100,2)
        return fordeling


def endring(fra_år,til_år):
    if fra_år and til_år not in valg.keys():
        print('ukjent år')
    else:
        fra=prosentvisfordeling(fra_år)
        til=prosentvisfordeling(til_år)
        for parti in fra.keys():
            if parti in til.keys():
                forandring=round(fra[parti]-til[parti],2)
                if forandring>0:
                    print(f'{partiNavn(parti)} går tilbake {abs(forandring)} prosentpoeng')
                if forandring<0:
                    print(f'{partiNavn(parti)} går fram {forandring} prosentpoeng')
                if forandring==0:
                    print(f'{partiNavn(parti)} beholder sin andel')
            else:
                print(f'{partiNavn(parti)} er ikke valgbar i {til_år}')
        if parti in til.keys() and not fra.keys():
            print(f'{partiNavn(parti)} er ikke valgbar i {fra_år}')


#Oppgave 12
def kretsOversikt():
    årstall=int(input('Oppgi årstall og kretsnavn \nÅr:'))
    kretsinput=input('Krets:')
    krets=kretsNr(kretsinput)
    år=valg[årstall]
    kretsen=år[krets]
    total=0
    for stemmer in kretsen.values():
        total+=stemmer
    partier=[]
    for key in kretsen.keys():
        partier.append(partiNavn(key))
    partier.sort()
    for parti in partier:
        print(f'{parti} fikk {kretsen[partiKode(parti)]} stemmer ({round(((kretsen[partiKode(parti)]/total)*100),1)}%)')

#kretsOversikt()

def kretsOversikt_alternativ():
    årstall=int(input('Oppgi årstall og kretsnavn \nÅr:'))
    kretsinput=input('Krets:')
    krets=kretsNr(kretsinput)
    år=valg[årstall]
    kretsen=år[krets]
    total=0
    for stemmer in kretsen.values():
        total+=stemmer
    partier=sorted(kretsen,key=kretsen.get)
    partier.reverse()
    for parti in partier:
        print(f'{parti} fikk {kretsen[partiKode(parti)]} stemmer ({round((kretsen[partiKode(parti)]/total),1)}%)')


#Oppgave 13
def partiOversikt():
    årstall=int(input('Oppgi årstall og partinavn \nÅr:'))
    partinavn=input('Parti:')
    år=valg[årstall]
    total=0
    for_partiet=0
    parti=partiKode(partinavn)
    minimum=[]
    maximum=[]
    minimum_value=100
    maximum_value=0
    for krets, resultat in år.items():
        krets_stemmer=0
        parti_stemmer=resultat[parti]
        for_partiet+=parti_stemmer

        for stemmer in resultat.values():
            total+=stemmer
            krets_stemmer+=stemmer

        if minimum_value>round((parti_stemmer/krets_stemmer)*100,2):
            minimum=[krets]
            minimum_value=round((parti_stemmer/krets_stemmer)*100,2)

        if maximum_value<round((parti_stemmer/krets_stemmer)*100,2):
            maximum=[krets]
            maximum_value=round((parti_stemmer/krets_stemmer)*100,2)

        elif minimum_value==round((parti_stemmer/krets_stemmer)*100,2):
            minimum.append(krets)    

        elif maximum_value==round((parti_stemmer/krets_stemmer)*100,2):
            maximum.append(krets)

    andel=round((for_partiet/total)*100,3)
    print(f'{partinavn} fikk {for_partiet} stemmer ({andel}%) i {årstall}')
    
    maximum_navn=[]

    for kretsnr in maximum:
        kretsnavn=kretser[kretsnr]
        maximum_navn.append(kretsnavn)

    minimum_navn=[]

    for kretsnr in minimum:
        kretsnavn=kretser[kretsnr]
        minimum_navn.append(kretsnavn)

    maximum_navn=list(set(maximum_navn))
    minimum_navn=list(set(minimum_navn))
    maximum_navn.sort()
    minimum_navn.sort()
    maximum_navn=str(maximum_navn).replace('[','')
    maximum_navn=str(maximum_navn).replace(']','')
    minimum_navn=str(minimum_navn).replace('[','')
    minimum_navn=str(minimum_navn).replace(']','')
    print(f'Høyest oppslutning ({maximum_value}%): {(maximum_navn)}')
    print(f'Lavest oppslutning ({minimum_value}%): {(minimum_navn)}')