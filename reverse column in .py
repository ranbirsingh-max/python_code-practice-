col = int(input("enter the number of columns:"))
rows=3
matrix=[]
for i in range (rows):
    row=list(map(int,input().split()))
    matrix.append(row)
for i in range(int(rows//2)):
    temp=matrix[i][col-1]
    matrix[i][col-1]=matrix[rows-i-1][col-1]
    matrix[rows-i-1][col-1]=temp
for ele in matrix:
    print(ele)
