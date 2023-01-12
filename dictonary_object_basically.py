
# dirtionaries nothing but joyect in js and interface in go

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


joy = {
    "name": "joy",
    "age": "22",
    "address": "address nai",
    "city": "city nai ",
    "state": "state nai ",
    "country": "country uganda ",
    "year": 2023,
    "description": [1, 2, 3, 4, 4, 5],
    "full_address": {
            "name": "joy",
            "id": "062",
            "age": "24",
            "city": "dh"
    }
}


#         part one


# print(joy)

# # only keys
# print(joy.keys())

# # only values
# print(joy.values())

# #  accessing properties of joy
# print(joy["name"])
# print(joy.get("name"))


# # reassigning value of properties
# joy["year"]=2022
# print(joy)


# # accessing nested properties of joy
# print(joy["description"][2])


# # add items
# joy["new add"]="example"
# print(joy)


# #pop items
# joy.pop("state")
# print(joy)

# # delete last items
# joy.popitem()
# print(joy)


#                 part two


# loop only in keys
for x in joy:
    print(x)


# loop only in values
for x in joy:
    print(joy[x])


# loop key => value
for key, value in joy.items():
    print(key, "=>", value)
