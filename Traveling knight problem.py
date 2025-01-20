#Assignment 2 task 2.py
import gurobipy as gp
from gurobipy import GRB
import networkx as nx

#Insert board with board values
board=[[36, 18, 64, 56, 23, 54, 59, 13],
       [17, 47, 20,  4, 15, 16, 53, 30],
       [ 2, 14, 26, 31, 57, 43, 12, 41],
       [10,  6,  3, 50, 42, 22, 48, 34],
       [38, 11,  1, 44, 55, 25, 29, 63],
       [33, 52, 27, 46, 62, 35, 28,  5],
       [24,  7, 21,  9, 37, 40, 39,  8],
       [19, 49, 32, 58, 51, 60, 45, 61]]

#Insert possible moves for a knight
knight_moves=[(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]

#Create Graph
G=nx.Graph()

for row in range(8):
    for column in range(8):
        G.add_node(board[row][column]) #adds each square on the board as a node in the graph

        for x,y in knight_moves:
            new_row,new_column=row+x,column+y #Shows what coordinates the knight can jump to from each square

            if 0<=new_row<=7 and 0<=new_column<=7: #Checks if the move is leagal
                G.add_edge(board[row][column],board[new_row][new_column]) #Adds the move as an edge between the two squares.

#Create the model
chess_model=gp.Model('Chess')

#Create the decision variable
x=chess_model.addVars(G.edges,vtype=GRB.BINARY,name='x')

#Create the objective function. Including the cost
chess_model.setObjective(gp.quicksum(abs(e[0]-e[1])*x[e] for e in G.edges), GRB.MINIMIZE)

#Makes it so each node is present in 2 of the selected edges. One for the knight arriving at the square and one for the knight leaving. 
#The task says to start from bottom right, but it does not matter where the knight starts from, as long as it needs to return.
chess_model.addConstrs(gp.quicksum(x[e] for e in G.edges if e in G.edges(i))==2 for i in G.nodes)

chess_model.optimize()

#Showing the solution. 
for v in chess_model.getVars():
    if v.X==1:
        print(v.VarName)