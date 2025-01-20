#Assignment 2 task 3.py
import gurobipy as gp
from gurobipy import GRB
import networkx as nx

#Setting up the data (rooms and doorways)
rooms=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
doorways=[['A','B'],['B','C'],['C','D'],['C','E'],['E','F'],['E','G'],['G','H'],['E','I'],['I','J'],['I','K'],['K','L'],['L','M'],['L','N'],['K','O'],['O','P'],['P','Q'],['Q','R'],['R','S'],['S','T'],['P','T'],['P','U'],['U','W'],['U','X'],['X','Y'],['U','Z'],['A','Z']]

#Creating the graph
G=nx.Graph()
G.add_nodes_from(rooms)
G.add_edges_from(doorways)

#Creating the model
warehouse_model=gp.Model('Warehouse')

x=warehouse_model.addVars(G.edges,vtype=GRB.BINARY, name='x') #Sets decision variable. Equals 1 if fan is set in doorway.

warehouse_model.setObjective(x.sum(),GRB.MINIMIZE) #Creates objective function

#Makes it so all rooms are connected to at least one fan
warehouse_model.addConstrs(gp.quicksum(x[e] for e in G.edges if e in G.edges(i))>=1 for i in G.nodes)

warehouse_model.optimize()

#Show the sulotion
for v in warehouse_model.getVars():
    if v.X==1:
        print(v.VarName)