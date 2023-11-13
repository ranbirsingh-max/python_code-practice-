print("1.calculate temperature celsius to fahrenheit:")
print("2.calculate temperature fahrenheit to celsius:")
select=int(input("select operation from 1,2:"))
if select == 1:
    celsius=int(input("enter the temperature in celsius:"))
    fahrenheit=(1.8*celsius)+32
    print("the temperature in fahrenheit is :",fahrenheit)
elif select == 2:
    fahrenheit=int(input("enter the temperature in fahrenheit:"))
    celsius=(fahrenheit-32)*5/9
    print("the temperature in celsius:",celsius)
else:
    print("invalid input")
