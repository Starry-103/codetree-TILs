move_dir=list(input())
x, y = 0, 0
dxs=[0, 1, 0, -1]
dys=[1, 0, -1, 0]
curr=0
ans=-1
cnt=0
for m in move_dir:
    if m=='L':
        curr=(curr+3)%4
    elif m=='R':
        curr=(curr+1)%4
    else:
        x=x+dxs[curr]
        y=y+dys[curr]
    cnt+=1
    if x==0 and y==0:
        ans=cnt
    if ans != -1:
        break

print(ans)