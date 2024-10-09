n, m = map(int, input().split())
pos_a=[0]
pos_b=[0]
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_a.append(v+pos_a[-1])

for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_b.append(v+pos_b[-1])



state=0
cnt=0

for i in range(len(pos_a)):
    if pos_a[i]==pos_b[i]:
        if state != 0:
            cnt += 1
        state=0
    elif pos_a[i]>pos_b[i]:
        if state != 1:
            cnt += 1
        state = 1
    else:
        if state !=2:
            cnt += 1
        state = 2

print(cnt)