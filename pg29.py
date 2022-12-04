list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
tup=tuple(list)
print(tup)
for i in tup:
    if tup.count(i)>1:
        rep=i
print(rep,"is the repeated element")
