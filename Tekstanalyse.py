#Tejstabakyse

class Tekstanalyse:

    tekst = [] # teksten som analyseres
    avsnittliste = []  # liste over normaliserte avsnitt i teksten
    ordlister = []  # liste av lister over ord som forekommer i hvert avsnitt
    ordtellinger = []  # liste av lister med ordtellinger for hvert avsnitt

    def __init__(self, tekst):
        self.tekst = tekst
    
    def fjern_ord_med_tall(self,tall=['0','1','2','3','4','5','6','7','8','9']):
        liste=self.tekst.split()
        for i in liste:
            for j in tall:
                if j in i:
                    self.tekst=self.tekst.replace(i,'')
                    break

    def normaliser_tekst(self, spesialtegn=['.',',',':',';','!','?','"',"'",'(',')','[',']','-','_','*','¨','–']):
        "Fjerner spesialtegn fra self.tekst og konverterer til små bokstaver."
        for i in spesialtegn:
            self.tekst=self.tekst.replace(i,'')
        self.tekst=self.tekst.lower()
        

    def til_avsnitt(self, avsnittskille='\n\n'):
        "Deler self.tekst opp i en liste av avsnitt som lagres i self.avsnitt ."
        self.avsnittliste=self.tekst.split(avsnittskille)
        

    def lag_ordliste(self, avsnittekst):
        "Lager en liste av ord som forekommer i avsnittet."
        rålsite=avsnittekst.split()
        liste=[]
        for i in rålsite:
            if i not in liste:
                liste.append(i)
        return(liste)

    def tell_ordforekomster(self, ordliste, avsnittekst):
        "Lager en liste over antall forekomster av ordene i ordliste i avsnittet."
        ordforekomster=[]
        råliste=avsnittekst.split()
        for i in ordliste:
            ordforekomster.append(råliste.count(i))
        return ordforekomster


    def analyser_tekst(self):
        "Lager en ordliste og teller ordforekomster for hvert avsnitt i teksten."
        ordlister = []
        ordtellinger = []
        for avsnittekst in self.avsnittliste:
            ordliste = self.lag_ordliste(avsnittekst)
            ordtelling = self.tell_ordforekomster(ordliste, avsnittekst)
            ordlister.append(ordliste)
            ordtellinger.append(ordtelling)
        self.ordlister = ordlister
        self.ordtellinger = ordtellinger

    def skriv_ut(self):
        "Skriver ut analyseresultatene for hvert avsnitt på skjermen."
        tall=0
        for i in self.avsnittliste:
            print('\tAvsnitt',tall+1)
            print('\tAvsnitttekst:', self.avsnittliste[tall])
            print('\tOrdliste:',self.ordlister[tall])
            print('\tOrdtelling:',self.ordtellinger[tall])
            print()
            tall+=1

    def lagre_til_fil(self, filnavn):
        "Lagrer analyseresultatene for hvert avsnitt i en fil."
        fil=open(filnavn,'w',encoding='utf-8')
        tall=0
        for i in self.avsnittliste:
            fil.write('Avsnitt'+str(tall+1)+'\n')
            fil.write('\tAvsnitttekst: '+ self.avsnittliste[tall]+'\n')
            fil.write('\tOrdliste: '+str(self.ordlister[tall])+'\n')
            fil.write('\tOrdtelling: '+str(self.ordtellinger[tall])+'\n\n')
            tall+=1


# testkjøring
filnavn = 'eksempeltekst.txt'
eksempeltekst = open(filnavn,encoding='utf-8').read()
tekstanalyse = Tekstanalyse(eksempeltekst)
tekstanalyse.fjern_ord_med_tall()
tekstanalyse.normaliser_tekst()
tekstanalyse.til_avsnitt()
tekstanalyse.analyser_tekst()
tekstanalyse.skriv_ut()
tekstanalyse.lagre_til_fil('Hovedoppgaveresultat.txt')