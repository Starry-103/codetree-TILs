n=int(input())
blocks=[]
for _ in range(n):
    blocks.append(int(input()))
avg=int(sum(blocks)/n)
ans=0
for i in blocks:
    if i>avg:
        ans+=i-avg

print(ans)