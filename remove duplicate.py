string=input()
rem_dup=[]
for i in string:
    if i not in rem_dup:
        rem_dup.append(i)
for i in rem_dup:
    print(i, end = " ")
