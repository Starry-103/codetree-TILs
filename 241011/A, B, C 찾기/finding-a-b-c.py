sums=list(map(int, input().split()))
sums.sort()
if sums[0]+sums[1]==sums[2]:
    print(sums[0], sums[1], sums[3])
else:
    print(sums[0], sums[1], sums[2])