n, t = map(int, input().split())
move=list(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

x, y = n//2, n//2
ans=arr[x][y]
dxs=[-1, 0, 1, 0]
dys=[0, 1, 0, -1]
curr=0
def in_range(a, b):
    return 0<=a and a<n and 0<=b and b<n
for m in move:
    if m=='R':
        curr=(curr+1)%4
    elif m=='L':
        curr=(curr+3)%4
    else:
        nx=x+dxs[curr]
        ny=y+dys[curr]
        if in_range(nx, ny):
            x=nx
            y=ny
            ans+=arr[x][y]
        
print(ans)