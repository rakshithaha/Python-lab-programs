list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
print("The list is:")
print(list)
print("list sorted in ascending order:")
list.sort()
print(list)
print("list sorted in descending order:")
list.sort(reverse=True)
print(list)
