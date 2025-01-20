#Oppgave 1
frukt_liste=['banan','eple','pære','vannmelon','tomat']
print(frukt_liste)
frukt_liste=frukt_liste + ['blåbær']
print(frukt_liste)
frukt_liste.pop(1)
print(frukt_liste)
print(len(frukt_liste))
if 'banan' in frukt_liste:
    print('ja')
else:
    print('nei')

#Oppgave 2
class Student:
    def __init__(self,navn,alder,studieretning):
        self.navn=navn
        self.alder=alder
        self.studieretning=studieretning

    def skriv_navn(self):
       print('Studenten heter', self.navn)
    
    def returner_alder(self):
        return self.alder
    
    def skriv_studieretning(self):
        print(self.navn,'studerer', self.studieretning)

student1=Student('Alice',20,'Informatikk')
student2=Student('Bob',22,'Matematikk')
student1.skriv_navn()
print(student1.returner_alder())
student1.skriv_studieretning()
student2.skriv_navn()
print(student2.returner_alder())
student2.skriv_studieretning()

#Oppgave 3b
import geometri
geometri.areal_firkant(5,10)
geometri.areal_sirkel(3)

#Oppgave 4a
class Personer:
    def __init__(self,navn,alder):
        self.navn=navn
        self.alder=alder

#b
class Bil:
    def __init__(self,merke,modell,eier):
        self.merke=merke
        self.modell=modell
        self.eier=eier
    
    def skriv_eier(self):
        print(self.eier.navn,'eier bilen')

alice=Personer('Alice',30)
bob=Personer('Bob',25)
camry=Bil('Toyota','Camry',alice)
focus=Bil('Ford','Focus',bob)
camry.skriv_eier()
focus.skriv_eier()

#Oppgave 5
def erstatt_vokaler(tekst):
    ny_tekst=tekst.replace('a','*')
    ny_tekst=ny_tekst.replace('A','*')
    ny_tekst=ny_tekst.replace('e','*')
    ny_tekst=ny_tekst.replace('E','*')
    ny_tekst=ny_tekst.replace('i','*')
    ny_tekst=ny_tekst.replace('I','*')
    ny_tekst=ny_tekst.replace('o','*')
    ny_tekst=ny_tekst.replace('O','*')
    ny_tekst=ny_tekst.replace('u','*')
    ny_tekst=ny_tekst.replace('U','*')
    ny_tekst=ny_tekst.replace('y','*')
    ny_tekst=ny_tekst.replace('Y','*')
    ny_tekst=ny_tekst.replace('æ','*')
    ny_tekst=ny_tekst.replace('Æ','*')
    ny_tekst=ny_tekst.replace('ø','*')
    ny_tekst=ny_tekst.replace('Ø','*')
    ny_tekst=ny_tekst.replace('å','*')
    ny_tekst=ny_tekst.replace('Å','*')
    print(ny_tekst)

erstatt_vokaler('Hallo Verden!')