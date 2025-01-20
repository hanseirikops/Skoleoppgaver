#Task 1
def h(key):
    m=13
    print(key%m)

h(27)
h(130)

#These keys would map to the indexes 1 and 0. Therefore the answer is b)

#Task 2
#Q1
m=11
keys=[11, 12, 14, 17, 18, 19, 20, 21, 25]
load_factor=len(keys)/m
print(load_factor)
#The load factor is 0.8181818181818182 or 9/11

#Q2
liste=[0,0,0,0,0,0,0,0,0,0,0] #A list of zeros with length of 11
for key in keys: #Does the hash function for all the keys
    index=key%11
    insterted=False
    while insterted==False: #Inserts the key if the index is 0, else checks the next index
        if liste[index]==0:
            liste[index]=key
            insterted=True
        elif liste[index]!=0:
            index=index+1
        elif index>11:
            print('ERROR TO MANY COLLISIONS')
            break
print(liste)
#[11, 12, 0, 14, 25, 0, 17, 18, 19, 20, 21]
#Alternative D is correct answer after using linear probing. 
#This is beacuse every key produces a unique output except 14 and 25 which produces the same output. Uisng linear probing, we take the output of 25 and add 1

#Task 3
import hashlib as hl 
import random 

class HashClass: 
    def __init__(self, id_num):
        self.id_num=id_num
        self.hash_id_num=self.hash_it()

    def hash_it(self):
        salt=random.randint(0,1000)
        salted=str(self.id_num+salt)
        return hl.sha1(salted.encode()).hexdigest() #SHA-algoritmen fra forelesningen

    def print_it(self):
        print(self.hash_id_num)

my_hash = HashClass(11011999) 
my_hash.print_it()

#Task 4

def most_frequent_integer(liste):
    frequency=dict()
    for integer in liste: #Creates a dictonary where the elements of the list is the keys and the number of repetitions is the value
        if type(integer)==int:
            if integer not in frequency:
                frequency[integer]=1
            else:
                frequency[integer]=frequency[integer]+1
    
    max_value=0
    for key, value in frequency.items(): #Finds the key to the maximum value
        if value>max_value:
            max_value=value
            max_key=key
    
    return max_key

my_list=[10,2,5,2,0,5,6,8,5,10]
result=most_frequent_integer(my_list)
print(result)