def triangular(n):
    if n==1:
        return 1
    else:
        return n+triangular(n-1)
    
print triangular(1)
print triangular(2)
print triangular(3)
print triangular(10)
