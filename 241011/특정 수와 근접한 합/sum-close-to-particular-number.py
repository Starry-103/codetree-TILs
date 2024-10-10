from itertools import combinations
n, s = map(int, input().split())
nums=list(map(int, input().split()))
print(min(abs(s - sum(nums) + elem) for elem in list(map(sum, combinations(nums, 2)))))