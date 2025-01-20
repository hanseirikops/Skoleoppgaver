#Classes

#Exercise 1

class Person:
    def __init__(self, name):
        self.name=name
    
    def greets(self, greeted):
        print(f'{self.name}: "Hello, {greeted.name}!"')

alice=Person('Alice')
bob=Person('Bob')
alice.greets(bob)

#Exercise 2

class Employe:
    def __init__(self,first_name,last_name,salary=10000):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    
    def get_fullname(self):
        return(self.first_name + ' '+ self.last_name)
    
    def print_email(self):
        print(f'{self.first_name.lower()}.{self.last_name.lower()}@company.com')
    
    def increase_salary(self,rate):
        self.salary=self.salary*rate

hans_eirik=Employe('Hans Eirik','Opsahl')
print(hans_eirik.get_fullname())
hans_eirik.print_email()
hans_eirik.increase_salary(1.1)

#Binary search

#Exercise 1

#a) you can do binary search on lists number 1, 3 and 5

#b)


def binary_search(liste, goal):
    guess=len(liste)//2
    print(guess)
    while goal!=liste[guess]:
        if liste[guess]<goal and guess !=0 and guess!=-1:
            print(guess)
        if liste[guess]>goal and guess!=0 and guess !=-1:
            guess=guess//2
            print(guess)
        if goal==liste[guess]:
            print(guess,'er riktig')
            break
        if guess==0 or guess==-1:
            print('not in list')
            break

liste1=[1,3,5,7,9,13,19,21]
binary_search(liste1,19)