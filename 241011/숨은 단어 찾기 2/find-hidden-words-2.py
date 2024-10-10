n, m = map(int, input().split())
arr=[
    list(input())
    for _ in range(n)
]

def in_range(a, b):
    return 0<=a and a<n and 0<=b and b<m

dxs=[0, 1, 1, 1, 0, -1, -1, -1]
dys=[1, 1, 0, -1, -1, -1, 0, 1]
#오른쪽방향 => 시계방향 회전
cnt=0
for x in range(n):
    for y in range(m):
        if arr[x][y]=='L':
            for d in range(8):
                nx=x+dxs[d]
                ny=y+dys[d]
                if in_range(nx,ny):
                    if arr[nx][ny]=='E':
                        nx=nx+dxs[d]
                        ny=ny+dys[d]
                        if in_range(nx, ny):
                            if arr[nx][ny]=='E':
                                cnt+=1

print(cnt)