list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
print("The list is:")
print(list)
def linear_search(list,n,key):
    for i in range(0,n):
        if(list[i]==key):
            return i
    else:
            return -1
n=len
key=int(input("Enter the element to be searches"))
res=linear_search(list,n,key)
if(res==-1):
    print("Element not found")
else:
    print("Element found at index:",res)
