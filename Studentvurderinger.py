class Student:

    def __init__(self, navn, e_post, vurderinger=[]):
        self.navn=navn
        self.e_post=e_post
        self.vurderinger=vurderinger

    def skriv_ut(self):
        print('Navn:', self.navn, 'e-post:', self.e_post)
        if len(self.vurderinger)>0:
            print('Vurderinger:\n', self.vurderinger)

    def ny_vurdering(self, emnekode, kommentar, karakter):
        if type(karakter)==int and karakter>0 and karakter<7:
            if type(emnekode)==Emne:
                vurdering = Vurdering (self, emnekode, kommentar, karakter)
                self.vurderinger.append(vurdering)
                emnekode.legg_til_vurdering(vurdering)
            else:
                print('Finner ikke emnet. Du kan legge til emne ved å bruke funksjonen: eks153=Emne("EKS153", Eksempler i eksemplering)')
        else:
            print('Karakteren må være et heltall mellom 1 og 6')
    
    def til_streng(self):
        return self.navn

    def skriv_ut(self):
        print('Navn:', self.navn, 'e-post:', self.e_post)
        #Skjønner ikke hvorfor alle sine vurderinger blir lagt til i self.vurderinger, men quickfix-variablen fungerer
        quickfix=[]
        for vurdering in self.vurderinger:
            if vurdering.hent_student()==self.navn:
                quickfix.append(vurdering)
        if len(quickfix)>0:
            print('Vurderinger:') 
            for vurdering in quickfix:
                print(vurdering.til_streng())

class Emne:

    alle_vurderinger=[]

    def __init__(self, emnekode, emnenavn):
        self.emnekode=emnekode
        self.emnenavn=emnenavn
    
    def legg_til_vurdering(self, vurdering):
        self.alle_vurderinger.append(vurdering)
    
    def til_streng(self):
        return self.emnekode
    
    def skriv_ut(self):
        print('Emne', self.emnekode + ':', self.emnenavn)
        sum=0
        #Quickfix er lagt inn av samme grunn som i klassen student
        quickfix=[]
        for vurdering in self.alle_vurderinger:
            if vurdering.hent_emne()==self.emnekode:
                quickfix.append(vurdering)
        if len(quickfix)>0:
            print('Vurderinger:')
            for vurdering in quickfix:
                print(vurdering.hent_student()+',', vurdering.til_streng())
                sum=sum+vurdering.karakter
            print('Gjennomsnittlig vurdering:', sum/len(self.alle_vurderinger))

class Vurdering:

    def __init__(self,student, emne, kommentar, karakter):
        self.student=student
        self.emne=emne
        self.kommentar=kommentar
        self.karakter=karakter

    def til_streng(self):
        return self.emne.til_streng()+': '+self.kommentar + ' skår='+str(self.karakter)
    
    def hent_student(self):
        return self.student.til_streng()
    
    def hent_emne(self):
        return self.emne.til_streng()

alina=Student('Alina Farschian', 'afa754@student.uib.no')
alina.skriv_ut()
print()

info132=Emne('INFO132', 'Innføring i programmering')
info132.skriv_ut()
print()

alina.ny_vurdering(info132, 'Kjempebra emne! Jeg tar det om igjen til neste høst!',5)
alina.skriv_ut()
info132.skriv_ut()

olea = Student('Olea Haldorsen', 'oha356@student.uib.no')
olea.skriv_ut()
olea.ny_vurdering(info132, 'Sånn passe. DATA110 om våren dekker omtrent det samme.', 3)
olea.skriv_ut()
info132.skriv_ut()