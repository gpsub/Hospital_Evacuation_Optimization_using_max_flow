import pandas as pd
data = pd.read_csv("data.csv")
# print(data)
loads = []
for index,i in data.iterrows():
    if i["gender"] == "M":
        load = i["age"]*0.5+i['severity']*2+i['weight']*0.5
    elif i["gender"] == "F":
        load = i["age"]*0.5+0.5*0.2+i['severity']*2+i['weight']*0.5
    loads.append(load)
    # print(load)
    i["load"] = load


# each floor has 20 rooms and each floor has 2 sides and two exits in middle
weight_floor = []
print(len(data))
for i in range(0,len(data),20):
    sum_a = 0
    sum_b = 0
    for a in range(i,i+10):
        sum_a += loads[a]
    for b in range(i+10,i+20):
        sum_b += loads[b]
    weight_floor.append([sum_a,sum_b])

print(weight_floor)
   
