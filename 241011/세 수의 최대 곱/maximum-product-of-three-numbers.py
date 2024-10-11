from math import prod
from itertools import combinations
n=int(input())
pos=[]
neg=[]

nums=list(map(int,input().split()))
for k in nums:
    if k>0:
        pos.append(k)
    elif k<0:
        neg.append(k)
sums=[]
if len(pos)<3:
    for elem in combinations(nums, 3):
        sums.append(prod(elem))
    print(max(sums))
else:
# pos 리스트에서 각 요소와 neg 리스트의 두 요소 조합에 대한 곱을 계산하여 sums에 추가
    for i in pos:
        for elem in combinations(neg, 2):
            sums.append(i * prod(elem))

# pos 리스트에서 세 요소 조합에 대한 곱을 sums에 추가
    for elem in combinations(pos, 3):
        sums.append(prod(elem))






    print(max(sums))

#음음양
#양양양