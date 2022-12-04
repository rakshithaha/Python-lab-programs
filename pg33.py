list=[]
print("Enter the length of the list")
len=int(input())
for i in range(len):
    elem=int(input("Enter a element"))
    list.append(elem)
print("The list is:")
print(list)

def binary_search(list,x):
    low=0
    high=len-1
    mid=0
    while low<=high:
        mid=(high+low)//2
        if list[mid]<x:
            low=mid+1
        elif list[mid]>x:
            high=mid-1
        else:
            return mid
    return -1

x=int(input("Enter the element to be searched"))
result=binary_search(list,x)
if result!=-1:
    print("Element is present at index",str(result))
else:
    print("Element is not present in the list")
