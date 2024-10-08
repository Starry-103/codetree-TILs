n=int(input())
def mlun(n):
    if n==2:
        return 4
    if n==1:
        return 2
    return (mlun(n-1)*mlun(n-2))%100

print(mlun(n))