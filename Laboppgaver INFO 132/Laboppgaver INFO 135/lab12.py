import math

def my_function(x):
    if x!=3:
        return 4*math.pi*(math.sqrt(3/x)+x**6)

horisontal_co=[1,2,3,4,5,6,7,8,9,10]
vertical_co=['A','B','C','D','E','F','G']
    
class Ship:
    def __init__(self,name,length):
        self.length=length
        self.coordinates={}
        self.name=name
        self.sunk=False
        self.damage=0
    
    def place_ship(self):
        horisontal=input('Are you placing the ship Horisontally (Yes/No)')
        start_h=int(input('Select coordinates to start placing your ship. Horisontal orianted ships start at its leftmost point. Vertical orianted ships start at its top points \nSelect horisontal starting point (1-10)'))
        start_v=input('Select vertical starting point (A-G)')
        if horisontal=='Yes':
            if (horisontal_co.index(start_h)+self.length)>len(horisontal_co):
                print('This placement does not fit in your grid, try again')
                self.place_ship()
            else:
                h_coordinates=[]
                for i in range(horisontal_co[start_h]-1, horisontal_co[start_h]+self.length-1):
                    h_coordinates.append(i)
                self.coordinates[start_v]=h_coordinates
        elif horisontal=='No':
            if (vertical_co.index(start_v)+self.length)>len(vertical_co):
                print('This placement does not fit in your grid, try again')
                self.place_ship()
            else:
                v_coordinates=[]
                for i in range(vertical_co.index(start_v),vertical_co.index(start_v)+self.length):
                    v_coordinates.append(vertical_co[i])
                self.coordinates[start_h]=v_coordinates

destroyer_1=Ship('HMS You suck', 3)

class Grid:
    def __init__(self, player):
        self.player=player