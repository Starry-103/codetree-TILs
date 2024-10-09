def todec(n,m):
    num=0
    for i in str(n):
        num=num*m+int(i)
    return num

def toq(n,m):
    if n<m:
        return str(n)
    
    return toq(n//m, m) + str(n%m)

a, b=map(int, input().split())
n=int(input())
print(toq(todec(n, a), b))