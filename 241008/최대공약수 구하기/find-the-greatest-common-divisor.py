n,m=map(int,input().split())
def MCD(n,m):
    if n>=m:
        B=n
        S=m
    else:
        B=m
        S=n
    while S != 0:
        [B, S]= [S, B%S]
    return B
print(MCD(n,m))