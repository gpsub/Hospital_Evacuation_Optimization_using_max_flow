## Graph visualization
import sys
import networkx as nx
from pyvis.network import Network
from calc import calc_loads,get_floor_weights

hospital = nx.DiGraph()

floor_weight_list = get_floor_weights( calc_loads() ) 

hospital.add_node(0,label='exit',x=200,y=300)
hospital.add_node(1,x=100,y=100)
hospital.add_node(2,x=125,y=100)
hospital.add_node(3,x=150,y=100)
hospital.add_node(4,x=175,y=100)
hospital.add_node(5,x=100,y=200)
hospital.add_node(6,x=125,y=200)
hospital.add_node(7,x=150,y=200)
hospital.add_node(8,x=175,y=200)


corridors=[(1,2),(2,3),(3,4),(4,8),(8,7),(7,6),(6,5),(5,1),(6,0),(7,0)]

hospital.add_edges_from(corridors)

nt = Network('600px','600px')
nt.from_nx(hospital)
nt.toggle_drag_nodes(True)
nt.toggle_physics(False)
nt.show("hospital.html")