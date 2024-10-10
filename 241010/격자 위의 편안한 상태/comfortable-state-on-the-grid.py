n, m = map(int, input().split())
grid=[
    [0]*n
    for _ in range(n)
]
dxs=[0, 1, 0, -1]
dys=[1, 0, -1, 0]
def in_range(a, b):
    return 0<=a and a<n and 0<=b and b<n

for _ in range(m):
    r, c = map(int, input().split())
    grid[r-1][c-1]=1
    cnt=0
    for d in range(4):
        nr=r-1+dxs[d]
        nc=c-1+dys[d]
        if in_range(nr, nc) and grid[nr][nc]==1:
            cnt+=1
    if cnt==3:
        print('1')
    else:
        print('0')