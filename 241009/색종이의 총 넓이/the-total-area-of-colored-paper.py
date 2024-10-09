l=[[0 for _ in range(200)] for _ in range(200)]
n=int(input())
for _ in range(n):
    x, y = map(int,input().split())
    for i in range(x+100, x+108):
        for j in range(y+100, y+108):
            l[i][j]=1

result=0
for k in l:
    result+=k.count(1)

print(result)