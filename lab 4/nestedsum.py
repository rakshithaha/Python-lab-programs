def nested_sum(a):
    sum=0
    for i in a:
        if(type(i)==list):
            sum=sum+nested_sum(i)
        else:
            sum=sum+i
    return sum

b=nested_sum([[1,2],[3],[4,5,6]])
print(b)
