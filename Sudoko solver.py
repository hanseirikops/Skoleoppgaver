#Assignment 2 task1.py
import gurobipy as gp
from gurobipy import GRB

#Represent the sudoko board using numbers
numbers=list(range(1,10))
squares=list(range(1,82))
subgrid1=[1,2,3,10,11,12,19,20,21]
subgrid2=[4,5,6,13,14,15,22,23,24]
subgrid3=[7,8,9,16,17,18,25,26,27]
subgrid4=[28,29,30,37,38,39,46,47,48]
subgrid5=[31,32,33,40,41,42,49,50,51]
subgrid6=[34,35,36,43,44,45,52,53,54]
subgrid7=[55,56,57,64,65,66,73,74,75]
subgrid8=[58,59,60,67,68,69,76,77,78]
subgrid9=[61,62,63,70,71,72,79,80,81]
subgrids=[subgrid1,subgrid2,subgrid3,subgrid4,subgrid5,subgrid6,subgrid7,subgrid8,subgrid9]

#Numbers allready put in
decided_numbers=[[1,9],[2,17],[3,18],[4,21],[5,24],[1,31],[3,41],[6,43],[7,48],[5,52],[8,53],[6,59],[7,60],[1,65],[4,69],[5,73],[2,74]]

#Creating the model
sudoko_model=gp.Model('Sudoko')

x=sudoko_model.addVars(numbers,squares,vtype=GRB.BINARY, name='x') #sets the decicion variable. Equals 1 if selected number is in selected square, otherwise 0

sudoko_model.setObjective(x.sum(),GRB.MAXIMIZE) #Creates objective function. GRB.MAXIMIZE can be changed as the answer will always be 81.

#Inserts the given numbers
for i in decided_numbers:
    sudoko_model.addConstr((x[i[0],i[1]])==1)

#Makes it so there is only one number per square
for i in squares:
    sudoko_model.addConstr(gp.quicksum(x[j, i] for j in numbers) == 1)

#Makes it so one number only appears once per row
for i in numbers:
    for j in range(9):
            sudoko_model.addConstr(gp.quicksum(x[i,j*9+k+1] for k in range(9))==1)

#Makes it so one number is only appears once per collumn
for i in numbers:
    for j in range(9):
            sudoko_model.addConstr(gp.quicksum(x[i,k*9+j+1] for k in range(9))==1)

#Makes it so one number only appears once per subgrid
for i in numbers:
    for j in subgrids:
        sudoko_model.addConstr(gp.quicksum(x[i,k] for k in j)==1)

sudoko_model.optimize()

#Shows the solution
solution=[]
for v in sudoko_model.getVars():
    if v.X==1:
        solution.append(v.VarName[2:-1].split(','))

for i in range(1,82):
    for j in solution:
        if int(j[1])==i:
            print(j[0],end=' ')
            if i%9==0:
                print()