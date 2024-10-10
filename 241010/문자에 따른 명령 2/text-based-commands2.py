move=list(input())
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
curr=3
for d in move:
    if d=='R':
        curr=(curr+1)%4
    elif d=='L':
        curr=(curr-1+4)%4
    else:
        x+=dx[curr]
        y+=dy[curr]

print(x, y)