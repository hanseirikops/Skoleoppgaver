#1
#Option a) A  B  D  G  H  E  I  C  F  J is the pre-order traversal of the tree

#2
#compute_result() is based on the knapsack problem from the lecture notes
class QuizGift:

    def compute_result(self,question_points,question_time,time,iterations):
        if time==0 or iterations==0: #Checks if the quiztaker is out of time or have checked all questions
            return 0
        
        if question_time[iterations-1]>time: #Checks if the question takes more time than the quizer have left
            return self.compute_result(question_points,question_time,time,iterations-1)
        
        else:
            #Adds the last question not checked to the possible sulotions
            new_time=time-question_time[iterations-1]
            with_new_question=self.compute_result(question_points,question_time,new_time,iterations-1)
            new_points=question_points[iterations-1]+with_new_question
            #Checks the result without doing the question
            without_new_question=self.compute_result(question_points,question_time,time,iterations-1)
        
        return max(new_points,without_new_question)

    def print_result(self, result):
        prize='watch' #The basic prize
        if result>250: #Changes prize on reaching points milestone
            prize='smartphone'
        if result>750: #Changes prize on reaching points milestone
            prize='laptop'
        print('Congratulations on the quiz! You gained',result,'points and won a', prize+'!')

    question_points=[120,200,150,350,100,90]
    question_time=[15,20,40,50,20,10]
    time=100
    iterations=len(question_points)

quiz=QuizGift()
quiz.print_result(quiz.compute_result(quiz.question_points,quiz.question_time,quiz.time,quiz.iterations))

#3
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass

class Square(Shape):
    def __init__(self,side):#Constructor
        super().__init__()
        self.side=side
    
    def compute_area(self):#Calculates the area
        area=self.side*self.side
        print(area)

class Circle(Shape):
    def __init__(self,radius):#Constructor
        super().__init__()
        self.radius=radius
    
    def compute_area(self):#Calculates the area
        area=self.radius*self.radius*3.14
        print(area)

class Triangle(Shape):
    def __init__(self,a,b,c):#Constructor
        self.a=a
        self.b=b
        self.c=c
    
    def compute_area(self):#Calculates the area
        s=(self.a+self.b+self.c)/2
        area=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        print (area)

my_square = Square(2) 
my_circle = Circle(2) 
my_triangle = Triangle(5, 4, 3) 
print('Area of square:', end=' ') 
my_square.compute_area() 
print('Area of circle:', end=' ') 
my_circle.compute_area() 
print('Area of triangle:', end=' ') 
my_triangle.compute_area()

#4

class House:
    def __init__(self,owner,price,condition): #Constructor
        self.owner=owner
        self.price=price
        self.condition=condition
        self.cost=0
        self.sold=False
        House.count+=1 #adds one house to the total number of houses
    
    count=0 #sets the baseline number of houses

    def sell(self, new_owner): #Changes owner and prints profit
        self.owner=new_owner
        self.sold=True
        print('House sold! Profit:', self.price-self.cost)
    
    def change_price(self, new_price): #Changes price if the house has not been sold
        if self.sold:
            print('House has been sold')
        else:
            self.price=new_price
    
    def renovate(self, expense, new_condition): #Changes conditions and cost of a house
        self.cost+=expense
        self.condition=new_condition
        print('House renovated!')
    
    def print_info(self): #prints the owner, condition and price
        print(f'Owner: {self.owner}, Condition: {self.condition}, Price: {self.price} [$]')

house1=House('John',100000,'Good')
house2=House('Sara',250000, 'Bad')

house1.print_info()
house2.print_info()
house1.renovate(50000,'Great')
house1.sell('Leo')
house1.print_info()
house1.change_price(1)
house2.change_price(200000)
house2.print_info()
print('Total number of houses:', House.count)