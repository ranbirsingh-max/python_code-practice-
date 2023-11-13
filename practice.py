x=int(input("enter the num_1:"))
y=int(input("enter the num_2:"))
def add(x,y):
    while(y!=0):
        carry=x & y
        x= x ^ y
        y= carry<<1
    return x
print(add(x,y))
