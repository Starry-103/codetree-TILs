n = int(input())
info=[]
for i in range(n):
    h, w = map(int, input().split())
    info.append([h, w, i+1])

info.sort()

for k in info:
    for j in k:
        print(j, end=' ')
    print()