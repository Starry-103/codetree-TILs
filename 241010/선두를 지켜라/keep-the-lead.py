n, m = map(int, input().split())
pos_n=[0]
pos_m=[0]
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_n.append(pos_n[-1]+v)

for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        pos_m.append(pos_m[-1]+v)
leader, cnt=0, 0
for i in range(len(pos_n)):
    if pos_n[i]>pos_m[i]:
        if leader==2:
            cnt+=1
        leader=1
    elif pos_n[i]<pos_m[i]:
        if leader==1:
            cnt+=1
        leader=2
print(cnt)