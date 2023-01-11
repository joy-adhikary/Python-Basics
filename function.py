

def main(): 
    print("hello")

main()


def joy1(x,y):
   print(x,y);
   z=x+y;
   print(z);

joy1(20,40)



# sending only data or pass in tuples type 
def joy2(*number):
    print(number);
    sum=0;
    for i in number:
        sum=sum+i;
    print(sum);

joy2(1,2,3,4)
joy2(5,10)



# sending key value pair or pass in a dictionary type 
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
def joy3(**parameter):
    x=len(parameter);
    print("length of parameter : ", x);
    for i in parameter:
        print(parameter[i]);

joy3(Fname="joy",Lname="adhikary",ID="062")
joy3(Fname="joy",Lname="adhikary")




# sending list as a parameter 
def joy4(parameter):
    x=len(parameter);
    print("length of parameter : ", x);
    for i in parameter:
        print(i);   
        # eijaigai  print(parameter[i]); eita hobe nah karon list a just value thake 

List=["joy","joy3","joy2"]
joy4(List)