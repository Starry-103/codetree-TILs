n=int(input())
cnt, ans=0, 0
def in_range(a, b, n):
    return 0<=a and a<n and 0<=b and b<n
grid=[]
dys=[0, 1, 0, -1]
dxs=[-1, 0, 1, 0]
x, y=(0, 0)
for _ in range(n):
    grid.append(list(map(int, input().split())))
curr=0
for x in range(n):
    for y in range(n):
        for dx, dy in zip(dxs, dys):
            nx=x+dx
            ny=y+dy
            if in_range(nx, ny, n) and grid[nx][ny]==1:
                cnt+=1
        if cnt>=3:
            ans+=1
        cnt=0

print(ans)