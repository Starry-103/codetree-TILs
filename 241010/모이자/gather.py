n=int(input())
l=list(map(int, input().split()))
sums=[]

for od, p in enumerate(l):
    sum=0
    #p=1번째 사람 => 나머지 사람들 하나씩 돌아가며 * (거리)
    for dd, i in enumerate(l):
        sum+=i*(abs(od-dd))
        
    sums.append(sum)





print(min(sums))