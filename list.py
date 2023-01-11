#  new element last theke insert hoi like array

list1=["joy","adhikary","hello"]

print(list1[0])

# list can contain different values 

joy=["joy",3333,'hey',True,4.0]

print(joy)

print(joy[3:])

# push new element 
list1.append("world")

print(len(list1))

# ( - )index means it start from last

print(joy[-3])


# pop element  fromt last 
joy.pop()

print(joy)


# pop a specified element 
joy.pop(2)
print(joy)



# simple for loop using indexing 

for i in range(len(joy)):
    print(joy[i])

print("printing useing for in ")

for i in joy:
    print(i)

