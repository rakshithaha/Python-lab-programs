list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
print("The list is:")
print(list)
print("The largest element in the list is", max(list))
print("The frequency of the largest element is:")
frequency=print(list.count(max(list)))
