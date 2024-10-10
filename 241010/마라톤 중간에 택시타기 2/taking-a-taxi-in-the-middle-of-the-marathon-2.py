import sys
INT_MAX = sys.maxsize
n=int(input())
arr=[
    list(map(int, input().split()))
    for _ in range(n)
]

ans=INT_MAX
for i in range(1, n-1):
    prev_idx=0
    dist=0
    for j in range(1, n):
        if i==j:
            continue
        dist+=abs(arr[j][0]-arr[prev_idx][0])+abs(arr[j][1]-arr[prev_idx][1])
        
        prev_idx=j
    ans=min(ans, dist)

print(ans)