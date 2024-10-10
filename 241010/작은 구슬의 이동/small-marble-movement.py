n, t = map(int, input().split())
x, y, d = input().split()
mapper={
    'R': 0,
    'D': 1,
    'L': 3,
    'U': 2
}
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
y=int(y)-1
x=int(x)-1
curr=mapper[d]
def in_range(x, y, n):
    return 0<=x and x<n and 0<=y and y<n
for _ in range(t):
    nx=x+dxs[curr]
    ny=y+dys[curr]
    if in_range(nx, ny, n):
        x=nx
        y=ny
    else:
        curr=3-curr
        
    
print(x+1, y+1)