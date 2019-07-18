H=[]
def triangular(n):
    e=0
    if n==1:
        return 1
    else:
        L=[]
        for j in range(1,n+1):
            L.append(j)
        for i in range(0,n):
            a=L[i]+e
            e=a        
        return a

print triangular(1)
print triangular(3)
print triangular(10)
