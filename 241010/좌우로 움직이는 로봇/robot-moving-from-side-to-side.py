n, m = map(int, input().split())
pos_a=[0]
pos_b=[0]
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
        pos_a.append(pos_a[-1]+(1 if d == 'R' else -1))

for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
        pos_b.append(pos_b[-1]+(1 if d == 'R' else -1))

dif, ans =  0, 0

mlen=min(len(pos_a), len(pos_b))

for i in range(1, mlen):
    if pos_a[i] == pos_b[i]:
        if dif == 1:
            ans+=1
        dif=0
    elif pos_a[i] != pos_b[i]:
        dif = 1

if len(pos_a)>len(pos_b):
    last=pos_b[-1]
    for k in pos_a[mlen-1:]:
        if k==last:
            if dif==1:
                ans+=1
            dif=0
        elif k!=last:
            dif=1
elif len(pos_b)>len(pos_a):
    last=pos_a[-1]
    for k in pos_b[mlen-1:]:
        if k==last:
            if dif==1:
                ans+=1
            dif=0
        elif k!=last:
            dif=1
print(ans)