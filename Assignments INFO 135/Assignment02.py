#Assignment 2
#Task 1

list_of_numbers=[ 1502, 1560, 1600, 1540, 100, 1660, 1700, 2024 ]

def selection_sort_three_times(liste):
    for times in range(0,3): #Forteller hvor mange ganger koden skal gå gjennom listen
        maximum_index=times
        for i in range(times+1,len(liste)): #Sjekker hvilket element i listen som er størst i den gjenveærende lengden
            if liste[i]>liste[maximum_index]:
                maximum_index=i

                temp=liste[times]
                liste[times]=liste[maximum_index]
                liste[maximum_index]=temp
#Viser med en type selection sort som setter det høyeste tallet først. Ønsket å gjøre dette på en annen måte enn det som ble vist på forelesning.

selection_sort_three_times(list_of_numbers)
print(list_of_numbers)
#The partially sorted list looks like this: [2024, 1700, 1660, 1502, 100, 1560, 1540, 1600, 500]

#Task 2

list_of_numbers_2=[ 400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540 ] 

def bubble_sort_three_times(liste):
    for times in range(0,3): #Forteller hvor mange ganger koden skal gå gjennom listen
        for numbers in range(0, len(liste)-times-1): #Sjekker om neste elementet i listen er mindre.
            if liste[numbers]>liste[numbers+1]:
                temp=liste[numbers]
                liste[numbers]=liste[numbers+1]
                liste[numbers+1]=temp
#Bruker bubble sort for å vise hvordan listen hadde sett ut
bubble_sort_three_times(list_of_numbers_2)
print(list_of_numbers_2)
#The partially sorted list looks like this: [10, 70, 160, 210, 220, 180, 260, 280, 380, 400, 540]

#Task 3

my_list=[5,4,3,2,1,2,3,4,5]

def sort_and_rem_dup(liste):
    for times in range(0,len(liste)):
        for numbers in range(0, len(liste)-times-1):
            if liste[numbers]>liste[numbers+1]:
                temp=liste[numbers]
                liste[numbers]=liste[numbers+1]
                liste[numbers+1]=temp
#Bruker først bubble sort for å sortere listen (copy paste fra forrige oppgave, men med endret range)
                
    liste_2=[]
    for element in liste: #Legger til elementer fra en sortert liste inn i en ny, men kun om den nye listen ikke har et likt element
        if element not in liste_2:
            liste_2.append(element)
    return liste_2
#ikke den mest effektive metoden siden den må gå gjennom listen 2 ganger, men har løst oppgaven

new_list=sort_and_rem_dup(my_list)
print(new_list)

#Task 4

class Queue: #Lager først klasser for queue og stack
    def __init__(self):
        self.contains=[]
    
    def dequeu(self): #Tar ut første element i queuen
        if len(self.contains)>0:
            return self.contains.pop(0)
    
    def enqueu(self, item): #Legger til elementer i queuen
        self.contains.append(item)

class Stack:
    def __init__(self):
        self.contains=[]
    
    def destack(self): #Tar ut siste elementet i stacken
        if len(self.contains)>0:
            return self.contains.pop()
    
    def enstack(self, item): #Legger til elementer i stacken
        self.contains.append(item)

def check_palindrome(word):
    stack=Stack()
    queue=Queue()
    for letter in word: #Lager en stack og en queue med hver bokstav i ordet
        stack.enstack(letter)
        queue.enqueu(letter)

    palindrome=True
    for letter in range(0,len(word)): #Tar ut fra queuen og stacken og sjekker om de er like eller ulike
        if stack.destack()!=queue.dequeu():
            palindrome=False
    
    if palindrome==True:
        return 'Palindrome'
    elif palindrome==False:
        return 'Not Palindrome'    
    
result=check_palindrome('hello')
print(result)
result=check_palindrome('civic')
print(result)