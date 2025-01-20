#Exercise 1

class Bruker:
    def __init__(self,startinskudd, navn):
        self.penger=startinskudd
        self.regningsliste=[]
        self.navn=navn
    
    def transfer(self, til, mengde):
        self.regningsliste.append((til,mengde))

#Exercise 2

def fibonacci(lengde):
    fibonacci_liste=[]
    for i in range(lengde):
        if len(fibonacci_liste)<2:
            fibonacci_liste.append(1)
        else:
            fibonacci_liste.append(fibonacci_liste[i-1]+fibonacci_liste[i-2])
    print(fibonacci_liste)

fibonacci(200)
#Jeg tror dette er O(n)

#Exercise 3
#A
#*           *  
# *         *   
#  *       *    osv osv
n=15
for i in range(n):
    for j in range(n):
        if (i==j) or ((n-j-1)==i):
            print('*',end='')
        else:
            print(' ',end='')
    print('')
#Jeg hadde riktig

#B
#    +    
#   +++   
#  +++++  
# +++++++ 
#+++++++++
def a_space_classic(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print('+',end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()
a_space_classic(5)
#Jeg hadde riktig igjen

#Extra task

class Fridge:
    def __init__(self, temperature=4, open=False):
        self.temperature=temperature
        self.open=open
        self.containing=[]
    
    def openfridge(self):
        self.open=True
        print('Fridge is open')
    
    def closefridge(self):
        self.open=False
        print('Fridge is closed')
    
    def additem(self, item):
        if self.open==True:
            self.containing.append(item)
            print(item.navn,'added to fridge')
        else:
            print('ERROR: Fridge is closed!')
    
    def removeitem(self, item):
        if self.open==True:
            self.containing.remove(item)
            print(item.navn,'removed from fridge')
        else:
            print('ERROR: Fridge is closed!')
    
    def decreasetemperature(self):
        self.temperature=self.temperature-1
    
    def increasetemperature(self):
        self.temperature=self.temperature+1
    
    def check_experation_date(self, item):
        if self.open==True and item  in self.containing:
            print (item.experation_date)
        else:
            print('ERROR: Item not in fridge or fridge is closed')
    
class Item:
    def __init__(self,navn, experation_date):
        self.experation_date=experation_date
        self.navn=navn

samsung_smart_fridge=Fridge()
milk=Item('Melk','26.02.2024')
cheese=Item('Jarlsberg', '25.05.2024')
samsung_smart_fridge.openfridge()
samsung_smart_fridge.additem(milk)
samsung_smart_fridge.additem(cheese)
samsung_smart_fridge.removeitem(cheese)
samsung_smart_fridge.check_experation_date(milk)
samsung_smart_fridge.closefridge()