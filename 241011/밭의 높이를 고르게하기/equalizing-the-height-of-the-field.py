n, h, t = map(int, input().split())
heights=list(map(int, input().split()))
costlist=[]
for i in range(n-t+1):
    cost=0
    for j in range(i, i+t):
        cost+=abs(heights[j]-h)
    costlist.append(cost)

print(min(costlist))