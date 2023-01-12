
# import json diye library add kore nite hobe

# json.load( somethings ) basically json format ke python a convirt kore dei

# json.dumps( somethings ) python ke json a convirt kore

# json.dumps dile ak line a json dekhabe oita ke easy to read korty indent 4 use korty hobe


#                                   json to python ( json ke load korbo python a)


import json

joy = '{ "name":"joy", "id":"062","age":"24","city":"dh"}'


y = json.loads(joy)
print(y)


for i in y:
    print(i, "=>", y[i])
print("")


#                                   python to json ( python ke dum kore dibo json er majhe )


joy1 = {
    "name": "joy",
    "id": "062",
    "age": "24",
    "address": {
        "city": "dh",
        "street": "dh"
    }
}

# print(joy1["address"]["city"])

x = json.dumps(joy1)
print(x)
print("")

x = json.dumps(joy1, indent=4)
print("using indent ==> 4")
print(x)





#                                          real life deal

# dictionary 
data = {
    "actual_data": [
        {
            "name": "joy",
            "id": "062", 
            "age": "24", 
            "city": "dh"
        },
         {
            "name": "joy",
            "id": "062", 
            "age": "24", 
            "city": "dh"
        },
         {
            "name": "joy",
            "id": "062", 
            "age": "24", 
            "city": "dh"
        },
         {
            "name": "joy",
            "id": "062", 
            "age": "24", 
            "city": "dh"
        }
    ]
}

# dictionary to json
dt=json.dumps(data,indent=4);

# json to dictionary


data2 = json.loads(dt)

for i in data2:
    print(i,":",data2[i])