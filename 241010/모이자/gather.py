n=int(input())
l=list(map(int, input().split()))
sums=[]

for od, p in enumerate(l):
    sum=0
    for dd, i in enumerate(l):
        sum+=i*(abs(od-dd))        
    sums.append(sum)
print(min(sums))