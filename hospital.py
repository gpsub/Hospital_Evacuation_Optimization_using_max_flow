## Graph visualization
import networkx as nx
from pyvis.network import Network
hospital = nx.DiGraph()

## rooms are 1 -2 -3 -4
#           |        |
#           5- 6-7 - 8
#               |           
#               0=exit
#


corridors=[(1,2),(2,3),(3,4),(4,8),(8,7),(7,6),(6,5),(5,1),(6,0),(7,0)]

hospital.add_edges_from(corridors)

nt = Network('600px','600px')
nt.from_nx(hospital)
nt.show("hospital.html")