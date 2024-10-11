x=int(input())
n=1
while 1:
    if n**2<=x<(n+1)**2:
        break
    n+=1
if x==n**2:
    time=2*n-1
elif n**2<x<=n**2+n:
    time=2*n
else:
    time=2*n+1
print(time)