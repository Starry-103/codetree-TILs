x=int(input())
ans=0
ps={}
cnt=0
for _ in range(x):
    n, p = map(int,input().split())
    if n in ps and ps[n]!=p:
        cnt+=1
    ps[n]=p
print(cnt)