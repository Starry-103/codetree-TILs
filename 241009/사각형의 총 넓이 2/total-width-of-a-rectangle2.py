n=int(input())
l=[[0 for _ in range(200)] for _ in range(200)]
offset=100
for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1+100, x2+100):
        for j in range(y1+100, y2+100):
            l[i][j]=1
result=0
for  k in l:
    result+=k.count(1)

print(result)