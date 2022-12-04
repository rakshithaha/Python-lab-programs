a=[]
b=[]
c=[]
list=['abc','xyz',1,2,'pqr',3,4,'a',4,5,6,3]
for i in list:
    if(type(i)==int):
        a.append(i)
    elif(type(i)==str):
        b.append(i)
    elif(type(i)==float):
        c.append(i)
print("Integer list: "+str(a))
print("Float list: "+str(c))
print("String list: "+str(b))
