# variable is the container to store value on it
# python a variable declar korty hoi nah , jkn value assign kori tkn e create hoi

# ; dileu jah nah dileu tai .. kono impact fele nah
x = 20
x = 15

y = 20
z = 10
print(x+y+z)

# python a variable type o reset ( reassign ) kora jai
x = 25  # here x is integer
print(x)

x = "joy"  # here x is string  => python er string a " " r ' ' 2 tai same
print(x)


# python a type jante type() use kora hoi
print(type(x))
print(type(y))


# akn jodi akta variable er type set kore dite cai tahole casting use korte hobe
# 3 int kintu eita ke as a string hisabe assign kortyce . so xx akn string
xx = str(3)
yy = str(3)
print(xx, type(yy))
print(type(xx))
x = 20
y = "10"
# print(x+y) produce an error bcz string+int
print(x+int(y))


# variable naming case sensitive c++ er mto
a = 'joy'
A = "adhikary"
print(A)

# assing multiple values
a, b, c = 20, 26, "joy"
print(a, b, c)

# global variable r local vairable er name same hole o global er value global e thake .change hoi nah
xyz = "Fixed global value"


def function():
    xyz = "value akn local hoye gase , function er majhe cng korle cng hobe"
    print(xyz)


function()
print("global xyz printing => ", xyz)

xyz = "this time global value changed"
print("global xyz printing => ", xyz)


# but global value kono function er majhe use korty and change korty caile global keyword use korty hobe
axyz = "Fixed global value"


def function():
    global axyz
    axyz = "value akn change hoye gase , function er majhe o global value cng hobe"
    print(axyz)


function()
print("global axyz printing => ", axyz)


#                   String operation


# multiline string with same line break
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
# or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# print(a)

#                                 string matching using in
a = 'my name is joy adhikary'
if "joy" in a:
    print("joy is present in string a ")
if "roy" not in a:
    print("roy nai a string a ")

b = "hello world"
print(b[2:5])  # idx 2 3 4  2<=idx<5
print(b[:5])  # start position to index 4 ( 0<=idx<5 )
print(b[3:])  # index 3 to last ( 3<=idx<=len(b))

#                                Spliting using default function

print(b.split(" "))


# format method use kora hoi string er majhe dynamic number use korar jonno

x = 19
y = 20
c = "eita x er dynamic value use korty parbe . value of x is {} , value of y is {} "
print(c.format(x, y))


# split string word it will generate a slice of word 

a="hello , world , hey , jsdaklf , number "
print(a.split(" , "))


