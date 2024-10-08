n=int(input())
def N(n):
    if n==2:
        return 2
    if n==1:
        return 1
    return N(n//3)+N(n-1)
print(N(n))