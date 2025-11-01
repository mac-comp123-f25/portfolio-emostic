def every_other(a):
    """deletes elements at odd indices"""
    # del a[1::2]
    """deletes elements at even indices"""
    return a[:len(a):2]

list2=["mary","John","Susan","Elma","Miriam","Apiu"]
alist=every_other(list2)
print(list2)
print(alist)

def sum_positive(b):
    total = 0
    for x in b:
        if x>0:
           total += x
    return total
negative_num=sum_positive({1,2,-5,3,4,5,-1})
print(negative_num)