n=int(input())
l=[[0 for _ in range(200)] for _ in range(200)]
for i in range(n):
    if i%2==0:
        color=1
    else:
        color=2
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1+100, x2+100):
        for j in range(y1+100, y2+100):
            l[i][j]=color

result=0

for k in l:
    result+=k.count(2)

print(result)