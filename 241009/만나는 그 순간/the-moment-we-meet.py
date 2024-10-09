aloc=[0]
bloc=[0]
n, m = map(int, input().split())
for _ in range(n):
    d, t = input().split()
    for _ in range(int(t)):
        aloc.append(aloc[-1]+1 if d == 'R' else aloc[-1]-1)

for _ in range(m):
    d, t = input().split()
    for _ in range(int(t)):
        bloc.append(bloc[-1]+1 if d == 'R' else bloc[-1]-1)

ans=-1
for i in range(1, len(aloc)):
    if aloc[i]==bloc[i]:
        ans=i
        break

print(ans)