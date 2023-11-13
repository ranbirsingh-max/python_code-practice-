import math
num_1=int(input("enter the number"))
print("1.square root:")
print("2.power:")
print("3.factorial:")

select=int(input("select the operator from 1,2,3:"))
if select == 1:
    print(f"the square root of {num_1} if {math.sqrt(num_1)}")
elif select == 2:
    p=int(input("enter the power:"))
    print(f"the power of {num_1} is {math.pow(num_1,p)}")
elif select == 3:
    print(f"the factorial of {num_1} is {math.factorial(num_1)}")
else:
    print("invalid input:")
