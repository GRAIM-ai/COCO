def max_select(a,b):
    if(a>b):
        return a
    else:
        return b
def rodcutting(price,size):
    if size<=0:
        return 0
    max_price=0
    for i in range(0,size):
        max_price=max_select(max_price,price[i]+rodcutting(price,size-i-1))
    return max_price

a_price=[1,5,8,10,17,17,20]
a_size=len(a_price)
print(rodcutting(a_price,a_size))
