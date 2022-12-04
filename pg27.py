r=int(input("Enter the rows"))
c=int(input("Enter the columns"))
print("Enter Matrix:")
m1=[[int(input()) for i in range(c)]for i in range (r)]
print("Matrix is:")
for n in m1:
    print(n)
sum=0
for i in range(r):
    for j in range(c):
        if i==j:
            sum=sum+m1[i][j]
print(sum)
