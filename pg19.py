a=int(input("Enter number of rows: "))
for i in range(0,a+1,1):
    for j in range(i+1,a+1,1):
        print(j,end=" ")
    print("\n")
