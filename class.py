

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# The __init__() function is called automatically every time the class is being used to create a new object

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.



class joy:
    def __init__(self,x,y): 
        self.age = x
        self.name = y

p1=joy(30,"mr.")
# reassign value of class property
p1.age=22
print(p1.age,p1.name)


class joy1:
    def __init__(self ,**parameter):
        self.age=parameter["age"]
        self.name=parameter["name"]
        
p2=joy1(age='30',name='joy',last='adhikary',id=62)
print(p2.age,p2.name)



# The __str__() function jodi set  thake tahole obj ke direct print korle  __str__() er majhe jah jah set kore dibo tai print korbe 
# If the __str__() function jodi set nah thake tahole obj ke direct print korle just object print hbe 



class joy3:
    def __init__(self,**joy):
        self.age=joy["age"]
        self.name=joy["name"]
        self.last=joy["last"]
       

    def __str__(self,**joy):
        return f"name:{self.name},last:{self.last},age:{self.age}"


p3=joy3(name='joy',age=30,last="adhikary")
print(p3)




class joy4:
    def __init__(self,x,y):
        self.name=x
        self.msg=y
        # init er majhe sob assign er kaj kortei hobe baki ta hok bah nah hok 

    def pri(abc):
        print("using abc instade of self > and it will work",abc.msg)
    


p5=joy4("joy","self => abc => jah khusi tai deya jai")
p5.pri()



#                                    inheritance start from here 

# this child class will use all joy4 properties 
# pass add korsi karon ami ei child class a kisu add korchi nah ajonno jodi kisu add kortam tkn eita pass nah diye properties diye ditam

class child(joy4):  
    pass;

p6=child("joy","child")
p6.pri()



# 1. ei jaigai child_with_init class ta hocche joy4 er child class . akn child class a init() use kora hoise jodi kono properties add kori tkn eita diye assign or access korty parbo .
# 2. akn ei init() parent class er init() ke ovverride korbe . ajonno amr child class er init er por por e abr parent class er init ke call kore dibo 

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:


class child_with_init(joy4):
    def __init__(self,x,y,child,id):
        joy4.__init__(self,x,y)
        self.child=child
        self.id=id


p7=child_with_init("joy","x","child",62)
print("this is last ")
p7.pri()
print(p7.child)


