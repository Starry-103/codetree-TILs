from math import prod
from itertools import combinations
n=int(input())

nums=list(map(int,input().split()))
nums.sort()
sum1=nums[-1]*nums[-2]*nums[-3]
sum2=nums[0]*nums[1]*nums[-1]







print(max(sum1, sum2))

#음음양
#양양양