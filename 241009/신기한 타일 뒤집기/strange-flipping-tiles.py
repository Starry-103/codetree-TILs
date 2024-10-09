n=int(input())
l=[0]*200000
now=100000
for _ in range(n):

    a, b=input().split()
    if  b=="L":
        for i in range(now, now- int(a), -1):
            l[i]=-1
        now=now-int(a)+1
    else:
        for i in range(now, now+int(a)):
            l[i]=1
        now=now+int(a)-1

print(l.count(-1), l.count(1))