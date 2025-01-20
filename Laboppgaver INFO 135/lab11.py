from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name=name
        self.species=species
        self.alive=True
    
    def kill(self):
        self.alive=False

    @abstractmethod
    def speak(self):
        pass

class Mammal (Animal):
    skin='Hair'

    def __init__(self, name, species, herbivore=True):
        super().__init__(name, species)
        self.herbivore=herbivore
    
    def speak(self):
        if self.alive==True:
            print('MOOO')

class Reptile(Animal):
    skin='Scales'
    def __init__(self, name, species, herbivore=True, venomous=False):
        super().__init__(name, species)
        self.herbivore=herbivore
        self.venomous=venomous
    
    def speak(self):
        if self.alive==True:
            print('hiss')

class Bird(Animal):
    skin='Feathers'
    herbivore=True
    def __init__(self, name, species, flightless=False):
        super().__init__(name, species)
        self.flightless=flightless
    
    def speak(self):
        if self.alive==True:
            print('Wake up its 5 am')

class Enclosure:
    def __init__(self, name, animals=[]):
        self.name=name
        self.animals=animals
    
    def add_animal(self, animal):
        self.animals.append(animal)
        self.check_herbivore(animal)
    
    def print_animals(self):
        print('The following animal(s) is in the enclosure')
        for animal in self.animals:
            print(animal.name)
    
    def check_herbivore(self, animal):
        if len(self.animals)>0:
            if self.animals[0].herbivore==True:
                if animal.herbivore==False:
                    self.animals.remove(animal)
                    print('You put a carnivore in a herbivore enclosure, the following animal(s) are now dead')
                    for i in self.animals:
                        print(i.name)
                        self.animals.remove(i)
                        self.animals.append(animal)
                        i.kill()
            elif self.animals[0].herbivore==False:
                if animal.herbivore==True:
                    print('You put a herbivore in a carnivore enclosure. Say goodbye to', animal.name)
                    self.animals.remove(animal)
                    animal.kill()

fido=Mammal('Fido','Dog',False)
lambert=Mammal('Lambert','Sheep')
arena=Enclosure('Arena')
arena.add_animal(lambert)
arena.add_animal(fido)
lambert.speak()
arena.print_animals()