n=[]
l=int(input("enter number of elements:")
for i in range(l):
ele=int(input())
n.append()
print(n)
def linear_search(n,x):
for i in range(len(n)):
if n[i]==x:
return i 
return -1
x=int(input("element to find"))
ans=linear_search(n,x)
if(ans==-1):
print("element not found")
else:
print("element found at index:",ans)
