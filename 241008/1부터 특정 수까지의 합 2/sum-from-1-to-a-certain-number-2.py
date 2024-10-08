def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1)
n=int(input())
print(sumN(n))