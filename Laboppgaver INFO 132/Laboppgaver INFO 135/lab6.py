#Lab 6
#Exercise 1 
def recur_factorial(tall):
    if tall<=1:
        return tall
    else:
        return tall*recur_factorial(tall-1)

print(recur_factorial(5))
print(recur_factorial(-1))

#Exercise 2
#a)
def truncation_key(key):
    string=str(key)
    liste=list(string)
    ny_liste=[]
    for index in range(0,len(liste)):
        if (index+1)%3==0 or (index+1)%5==0:
            ny_liste.append(liste[index])
    new_string=''
    for i in ny_liste:
        new_string=new_string+i
    return int(new_string)

print(truncation_key(94283641911))

#b)
def string_hash(key):
    answer=1
    for letter in key:
        answer=answer*ord(letter)
    return answer

print(string_hash('key'))

def hash(key):
    hash1=string_hash(key)
    return truncation_key(hash1)

#Exercise 3

class PasswordDatabase:
    def __init__(self):
        self.passwords={}
    
    #a)
    def create_user(self):
        username=input('Vennligst skriv et brukernavn:')
        password=input('Vennligst skriv et passord:')
        password=hash(password)
        self.passwords[username]=password
    
    
    #b)
    def check_password(self):
        username=input('Hva er brukernavnet ditt?')
        password=input('Skriv inn ditt passord:')
        password=hash(password)
        if username not in self.passwords:
            return False
        elif self.passwords[username]==password:
            return True
        else:
            return False
    
    #c)
    def update_password(self):
        print('Update password')
        username=input('Hva er brukernavnet ditt?')
        password=input('Skriv inn ditt passord:')
        password=hash(password)
        if username not in self.passwords:
            print('Feil brukernavn')
        elif self.passwords[username]==password:
            password=input('Skriv inn nytt passord:')
            password=hash(password)
            self.passwords[username]=password
            print('Passord oppdatert')
        else:
            print('Feil passord')

database=PasswordDatabase()

database.create_user()
database.check_password()
database.update_password()
print(database.check_password())
print(database.passwords)