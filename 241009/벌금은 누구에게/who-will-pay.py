n, m, k = map(int, input().split())
score=[k]*n
ans=-1
for _ in range(m):
    s=int(input())
    score[s-1]-=1
    if score[s-1]==0:
        ans=s
        break
        
print(ans)