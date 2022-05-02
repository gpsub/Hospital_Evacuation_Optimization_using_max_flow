## Graph visualization
import sys
import networkx as nx
from pyvis.network import Network
from calc import calc_loads,get_floor_weights

hospital = nx.DiGraph()

hospital.add_node(0,label='exit',x=175,y=500)
#floor3
floor_weight_list = get_floor_weights( calc_loads() ) 
print(floor_weight_list)

hospital.add_node(0,label='exit',x=200,y=300)
hospital.add_node(1,x=100,y=100)
hospital.add_node(2,x=150,y=100)
hospital.add_node(3,x=200,y=100)
hospital.add_node(4,x=250,y=100)
#floor2
hospital.add_node(5,x=100,y=200)
hospital.add_node(6,x=150,y=200)
hospital.add_node(7,x=200,y=200)
hospital.add_node(8,x=250,y=200)
#floor1
hospital.add_node(9,x=100,y=300)
hospital.add_node(10,x=150,y=300)
hospital.add_node(11,x=200,y=300)
hospital.add_node(12,x=250,y=300)
#floor0
hospital.add_node(13,x=100,y=400)
hospital.add_node(14,x=150,y=400)
hospital.add_node(15,x=200,y=400)
hospital.add_node(16,x=250,y=400)


hospital.add_edge(1,2,capacity=100)
hospital.add_edge(1,3,capacity=80)
hospital.add_edge(4,2,capacity=80)
hospital.add_edge(4,3,capacity=100)

# exit1
hospital.add_edge(2,7,capacity=100)
hospital.add_edge(2,6,capacity=100)

hospital.add_edge(3,7,capacity=100)
hospital.add_edge(3,6,capacity=100)


hospital.add_edge(5,6,capacity=220)
hospital.add_edge(5,7,capacity=200)
hospital.add_edge(8,6,capacity=220)
hospital.add_edge(8,7,capacity=200)

#exit2
hospital.add_edge(6,10,capacity=100)
hospital.add_edge(6,11,capacity=100)

hospital.add_edge(7,10,capacity=200)
hospital.add_edge(7,11,capacity=200)



hospital.add_edge(9,10,capacity=350)
hospital.add_edge(9,11,capacity=300)
hospital.add_edge(12,10,capacity=350)
hospital.add_edge(12,11,capacity=300)

#exit3

hospital.add_edge(10,14,capacity=100)
hospital.add_edge(11,15,capacity=100)

hospital.add_edge(10,15,capacity=200)
hospital.add_edge(11,14,capacity=200)

hospital.add_edge(13,14,capacity=500)
hospital.add_edge(13,15,capacity=550)
hospital.add_edge(16,15,capacity=550)
hospital.add_edge(16,14,capacity=500)

#finalexit
hospital.add_edge(14,0,capacity=200)
hospital.add_edge(15,0,capacity=200)



def foo1(x):
    return int(x)



nt = Network('800px','800px')
nt.from_nx(hospital,edge_weight_transf=foo1)
nt.toggle_drag_nodes(True)
nt.toggle_physics(False)
nt.show("hospital.html")