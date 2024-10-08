n=int(input())
def f102938(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum//10

print(f102938(n))