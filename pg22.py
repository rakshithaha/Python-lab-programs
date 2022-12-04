list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
print("The list is:")
print(list)
num=int(input("Enter the number whose occurances is to be deleted"))
while num in list:
    list.remove(num)
print(list)
