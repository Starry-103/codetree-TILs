n=int(input())
mapper={
    'N': 3,
    'E': 0,
    'S': 1,
    'W': 2
}
dxs=[1, 0, -1, 0]
dys=[0, -1, 0, 1]
x, y = 0, 0
ans=-1
cnt=0
for _ in range(n):
    d, l = input().split()
    l=int(l)
    move=mapper[d]
    for _ in range(l):
        x=x+dxs[move]
        y=y+dys[move]
        cnt+=1
        if x==0 and y==0:
            ans=cnt
            break

print(ans)