n,m=map(int,input().split())
if n<=m:
    tmp=n
    n=m
    m=tmp
def GCD(n,m):
    if m==0:
        return n
    
    return GCD(m,n%m)
print(int(n*m/GCD(n,m)))