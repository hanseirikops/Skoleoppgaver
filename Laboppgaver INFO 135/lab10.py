#Excercise 1 
v=[120,200,150,350,100,90]
w=[15,20,40,50,20,10]
c=100

def detailed_knap_sack(capacity, wheigts, values):
    n=len(values)
    wheigts_used=[]
    grid=[[0 for x in range (capacity+1)] for x in range(n+1)]

    for i in range (1,n+1):
        for w in range(1,capacity+1):
            if wheigts[i-1]<=w:
                grid[i][w]=max(values[i-1]+grid[i-1][w-wheigts[i-1]],grid[i-1][w])
            else:
                grid[i][w]=grid[i-1][w]
    print (grid[n][capacity])
    print (wheigts_used)


detailed_knap_sack(c,w,v)

import time
class Rocket:
    def __init__(self,engine,stearing_fins,radio,control_panel):
        self.optimal_cruising_speed='precalculated speed'
        self.optimal_cruising_angle='precalculated angle'
        self.speed_needed_to_enter_cruising='precalculatet speed'
        self.engine=engine
        self.stearing_fins=stearing_fins
        self.radio=radio
        self.control_panel=control_panel

    def launch(self):
        self.engine.set_trottle(100)

    def land():
        print('land')

    def cruise(self):
        if self.control_panel.read_speed()>=self.speed_needed_to_enter_cruising:
            while self.control_panel.read_tilt()<self.optimal_cruising_angle:
                self.stearing_fins.increase_x(5)
                time.sleep(5)

    def send_radio_message():
        print('radio gaga')
    
class Engine:
    def __init__(self):
        self.trottle=0
    
    def returner_trottle(self):
        return self.trottle
    
    def increase_trottle(self,percentage):
        if percentage + self.trottle > 100:
            self.trottle=percentage+self.trottle
        else:
            self.trottle=100
    
    def decrease_trottle(self,percentage):
        if self.trottle-percentage>0:
            self.trottle=self.trottle-percentage
        else:
            self.trottle=0
    
    def set_trottle(self,percentage):
        if percentage <=100 and percentage >=0:
            self.trottle=percentage

class StearingFins:
    def __init__(self):
        self.x_fin=0
        self.y_fin=0

    def returner_x(self):
        return self.x_fin
    
    def increase_x(self,percentage):
        if percentage + self.x_fin > 100:
            self.x_fin=percentage+self.x_fin
        else:
            self.x_fin=100
    
    def decrease_x(self,percentage):
        if self.x_fin-percentage>0:
            self.x_fin=self.x_fin-percentage
        else:
            self.x_fin=0
    
    def set_x(self,percentage):
        if percentage <=100 and percentage >=0:
            self.x_fin=percentage
    
    def returner_y(self):
        return self.y_fin
    
    def increase_y(self,percentage):
        if percentage + self.y_fin > 100:
            self.y_fin=percentage+self.y_fin
        else:
            self.y_fin=100
    
    def decrease_y(self,percentage):
        if self.y_fin-percentage>0:
            self.y_fin=self.y_fin-percentage
        else:
            self.y_fin=0
    
    def set_y(self,percentage):
        if percentage <=100 and percentage >=0:
            self.y_fin=percentage

class Radio:
    def send_message(message):
        print('Following message has been sent:',message)

class ControlPanel:
    def __init__(self):
        self.speed=0
        self.tilt=0
    
    def read_speed(self):
        pass

    def read_tilt(self):
        pass