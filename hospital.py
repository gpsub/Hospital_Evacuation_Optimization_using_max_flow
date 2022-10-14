## Graph visualization
import sys
import networkx as nx
from pyvis.network import Network
from calc import calc_loads,get_floor_weights

def create_hospital():
    hospital = nx.DiGraph()

    hospital.add_node(0,label='exit',x=175,y=500)
    
    loads = calc_loads()
    floor_weight_list = get_floor_weights( loads ) 
    print(floor_weight_list)
    avg = sum(loads)/len(loads)


    hospital.add_node(0,label='Finalexit',x=200,y=500)

    hospital.add_node(1,label="Ward1",x=50,y=50)
    hospital.add_node(2,label="Floor3Exit1",x=150,y=100)
    hospital.add_node(3,label="Floor3Exit2",x=350,y=100)
    hospital.add_node(4,label="Ward2",x=450,y=50)
    #floor2
    hospital.add_node(5,label="Ward3",x=50,y=150)
    hospital.add_node(6,label="Floor2 Exit1",x=150,y=200)
    hospital.add_node(7,label="Floor2 Exit2",x=350,y=200)
    hospital.add_node(8,label="Ward4",x=450,y=150)
    #floor1
    hospital.add_node(9,label="Ward5",x=50,y=250)
    hospital.add_node(10,label="Floor1 Exit1",x=150,y=300)
    hospital.add_node(11,label="Floor1 Exit2",x=350,y=300)
    hospital.add_node(12,label="Ward6",x=450,y=250)
    #floor0
    hospital.add_node(13,label="ICU ward",x=50,y=350)
    hospital.add_node(14,label="Ground exit1",x=150,y=400)
    hospital.add_node(15,label="Ground Exit2",x=350,y=400)
    hospital.add_node(16,label="Trauma ward",x=450,y=350)

    hospital.add_edge(1,2,capacity=700)
    hospital.add_edge(1,3,capacity=700)
    hospital.add_edge(4,2,capacity=700)
    hospital.add_edge(4,3,capacity=700)

    # exit1
    hospital.add_edge(2,7,capacity=1200)
    hospital.add_edge(2,6,capacity=1200)

    hospital.add_edge(3,7,capacity=1200)
    hospital.add_edge(3,6,capacity=1200)


    hospital.add_edge(5,6,capacity=800)
    hospital.add_edge(5,7,capacity=800)
    hospital.add_edge(8,6,capacity=800)
    hospital.add_edge(8,7,capacity=800)

    #exit2
    hospital.add_edge(6,10,capacity=2800)
    hospital.add_edge(6,11,capacity=2800)

    hospital.add_edge(7,10,capacity=2800)
    hospital.add_edge(7,11,capacity=2800)


    hospital.add_edge(9,10,capacity=800)
    hospital.add_edge(9,11,capacity=800)
    hospital.add_edge(12,10,capacity=800)
    hospital.add_edge(12,11,capacity=800)

    #exit3

    hospital.add_edge(10,14,capacity=4200)
    hospital.add_edge(11,15,capacity=4200)

    hospital.add_edge(10,15,capacity=4200)
    hospital.add_edge(11,14,capacity=4200)

    hospital.add_edge(13,14,capacity=1000)
    hospital.add_edge(13,15,capacity=1000)
    hospital.add_edge(16,15,capacity=1000)
    hospital.add_edge(16,14,capacity=1000)

    #finalexit
    hospital.add_edge(14,0,capacity=10000)
    hospital.add_edge(15,0,capacity=10000)
    ## super source vertex
    hospital.add_edge(20,1,capacity=int(floor_weight_list[0][0]))
    hospital.add_edge(20,4,capacity=int(floor_weight_list[0][1]))

    hospital.add_edge(20,5,capacity=int(floor_weight_list[1][0]))
    hospital.add_edge(20,8,capacity=int(floor_weight_list[1][1]))

    hospital.add_edge(20,9,capacity=int(floor_weight_list[2][0]))
    hospital.add_edge(20,12,capacity=int(floor_weight_list[2][1]))

    hospital.add_edge(20,13,capacity=int(floor_weight_list[3][0]))
    hospital.add_edge(20,16,capacity=int(floor_weight_list[3][1]))




    def temp(x):
        return int(x)
    
    nt1 = Network('800px','800px')
    nt1.from_nx(hospital,edge_weight_transf=temp)
    nt1.toggle_drag_nodes(True)
    nt1.toggle_physics(False)
    nt1.show("hospital.html")
    return hospital,loads,avg,temp

def calculate_output_flow(hospital,loads,avg,temp):
    flow_value, flow_dict = nx.maximum_flow(hospital,20,0)
    print("Flow value="+ str(flow_value)+"\n\n")
    print("flow dict="+str(flow_dict)+"\n\n")
    people = flow_value//avg
    total = len(loads)
    print("\n\n"+str(people)+ " people evacuated out of "+ str(total)+" people in hospital")
    output = nx.DiGraph()


    output.add_node(0,label='Finalexit',x=200,y=500)

    output.add_node(1,label="Ward1",x=50,y=50)
    output.add_node(2,label="Floor3Exit1",x=150,y=100)
    output.add_node(3,label="Floor3Exit2",x=350,y=100)
    output.add_node(4,label="Ward2",x=450,y=50)
    #floor2
    output.add_node(5,label="Ward3",x=50,y=150)
    output.add_node(6,label="Floor2 Exit1",x=150,y=200)
    output.add_node(7,label="Floor2 Exit2",x=350,y=200)
    output.add_node(8,label="Ward4",x=450,y=150)
    #floor1
    output.add_node(9,label="Ward5",x=50,y=250)
    output.add_node(10,label="Floor1 Exit1",x=150,y=300)
    output.add_node(11,label="Floor1 Exit2",x=350,y=300)
    output.add_node(12,label="Ward6",x=450,y=250)
    #floor0
    output.add_node(13,label="ICU ward",x=50,y=350)
    output.add_node(14,label="Ground exit1",x=150,y=400)
    output.add_node(15,label="Ground Exit2",x=350,y=400)
    output.add_node(16,label="Trauma ward",x=450,y=350)

    output.add_edge(1,2,weight=int(flow_dict[1][2]))
    output.add_edge(1,3,weight=int(flow_dict[1][3]))
    output.add_edge(4,2,weight=int(flow_dict[4][2]))
    output.add_edge(4,3,weight=int(flow_dict[4][3]))

    # exit1
    output.add_edge(2,7,weight=int(flow_dict[2][7]))
    output.add_edge(2,6,weight=int(flow_dict[2][6]))

    output.add_edge(3,7,weight=int(flow_dict[3][7]))
    output.add_edge(3,6,weight=int(flow_dict[3][6]))


    output.add_edge(5,6,weight=int(flow_dict[5][6]))
    output.add_edge(5,7,weight=int(flow_dict[5][7]))
    output.add_edge(8,6,weight=int(flow_dict[8][6]))
    output.add_edge(8,7,weight=int(flow_dict[8][7]))

    #exit2
    output.add_edge(6,10,weight=int(flow_dict[6][10]))
    output.add_edge(6,11,weight=int(flow_dict[6][11]))

    output.add_edge(7,10,weight=int(flow_dict[7][10]))
    output.add_edge(7,11,weight=int(flow_dict[7][11]))


    output.add_edge(9,10,weight=int(flow_dict[9][10]))
    output.add_edge(9,11,weight=int(flow_dict[9][11]))
    output.add_edge(12,10,weight=int(flow_dict[12][10]))
    output.add_edge(12,11,weight=int(flow_dict[12][11]))

    #exit3

    output.add_edge(10,14,weight=int(flow_dict[10][14]))
    output.add_edge(11,15,weight=int(flow_dict[11][15]))

    output.add_edge(10,15,weight=int(flow_dict[10][15]))
    output.add_edge(11,14,weight=int(flow_dict[11][14]))

    output.add_edge(13,14,weight=int(flow_dict[13][14]))
    output.add_edge(13,15,weight=int(flow_dict[13][15]))
    output.add_edge(16,15,weight=int(flow_dict[16][15]))
    output.add_edge(16,14,weight=int(flow_dict[16][14]))

    #finalexit
    output.add_edge(14,0,weight=int(flow_dict[14][0]))
    output.add_edge(15,0,weight=int(flow_dict[15][0]))

    # output.add_edge(20,1,weight=flow_dict[20][1])
    # output.add_edge(20,4,weight=flow_dict[20][4])

    # output.add_edge(20,5,weight=flow_dict[20][5])
    # output.add_edge(20,8,weight=flow_dict[20][8])

    # output.add_edge(20,9,weight=flow_dict[20][9])
    # output.add_edge(20,12,weight=flow_dict[20][12])

    # output.add_edge(20,13,weight=flow_dict[20][13])
    # output.add_edge(20,16,weight=flow_dict[20][16])



    nt = Network('800px','800px')
    nt.from_nx(output,edge_weight_transf=temp)
    nt.toggle_drag_nodes(True)
    nt.toggle_physics(False)
    nt.show("hospital.html")

if __name__=="__main__":
    hospital,loads,avg,temp = create_hospital()
    print("Open hospital.html to view initial state of hospital")
    option = input("Press 'a' to view result after max flow calculation")
    if (option=='a'):
        calculate_output_flow(hospital,loads,avg,temp)
        print("Reload/view hospital.html again to view result after network flow optimization.")