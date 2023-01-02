def has_duplicates(list):
    for i in list:
        s=list.count(list[i])
        if(s>1):
            print("True")
            break
has_duplicates([1,2,2])
