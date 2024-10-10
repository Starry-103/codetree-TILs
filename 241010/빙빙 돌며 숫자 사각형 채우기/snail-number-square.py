m, n = map(int, input().split())
#0=오른쪽, 시계방향 회전
dxs=[0, 1, 0, -1]
dys=[1, 0, -1, 0]

grid=[
    [0] * n
    for _ in range(m)
]
grid[0][0]=1
curr=0
x, y = 0, 0
def is_ok(x, y):
    return 0<=x and x<m and 0<=y and y<n
for i in range(2, n*m+1):
    nx, ny = x+dxs[curr], y+dys[curr]
    if not is_ok(nx, ny) or grid[nx][ny] != 0:
        curr=(curr+1)%4
    x = x+dxs[curr]
    y = y+dys[curr]
    grid[x][y]=i

print('\n'.join(' '.join(map(str, k)) for k in grid))