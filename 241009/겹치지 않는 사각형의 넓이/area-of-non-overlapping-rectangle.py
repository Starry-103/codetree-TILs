l=[[0 for _ in range(2000)] for _ in range(2000)]
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1+1000, x2+1000):
        for j in range(y1+1000, y2+1000):
            l[i][j]=1

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1+1000, x2+1000):
    for j in range(y1+1000, y2+1000):
        l[i][j]=0

result=0
for k in l:
    result+=k.count(1)


print(result)