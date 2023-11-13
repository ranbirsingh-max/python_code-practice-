def add(x,y):
   return x+y
def subtract(x,y):
   return x-y
def multiply(x,y):
   return x*y
def divide(x,y):
   return x/y
def mod(x,y):
   return x%y
print("select the operations:\n"
      "1.add\n"
      "2.subtract\n"
      "3.multiply\n"
      "4.divide\n"
      "5.mod\n")
select=int(input("select the operations from 1,2,3,4,5:"))
x=int(input("enter the first number:"))
y=int(input("enter the second number:"))

if select == 1:
    print(x,"+",y,"=",add(x,y))
elif select == 2:
   print(x,"-",y,"=",subtract(x,y))
elif select ==3:
   print(x,"*",y,"=",multiply(x,y))
elif select ==4:
   print(x,"/",y,"=",divide(x,y))
elif select ==5:
   print(mod(x,"%",y,"=",x,y))
else:
    print("invalid input")
