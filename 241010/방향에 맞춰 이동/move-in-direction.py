n=int(input())
dx, dy = {'W': -1, 'S': 0, 'E': 1, 'N': 0}, {'W': 0, 'S': -1, 'E': 0, 'N': 1}
x, y = 0, 0
for _ in range(n):
    a, b = input().split()
    x+=dx[a]*int(b)
    y+=dy[a]*int(b)

print(x, y)