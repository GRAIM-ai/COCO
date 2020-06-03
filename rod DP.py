INT_MIN=-32767
def max(a,b):
    if(a>b):
        return a
    else:
        return b
def cutRod(price,n):
    val=[0 for x in range(n+1)]
    for i in range(1,n+1):
        max_val=INT_MIN
        for j in range(i):
            #3 line code
            max_val=max(max_val,price[i-1-j]+val[j])
            val[i]=max_val
            print(val)
    return val[n]

priceArr=[1,5,8,9,10,17,17,20]
size=len(priceArr)
print("Maximum obtainable value is " +str(cutRod(priceArr,size)))