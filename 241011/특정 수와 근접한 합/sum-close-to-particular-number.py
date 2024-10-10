import itertools
n, s = map(int, input().split())
nums=list(map(int, input().split()))
print(min(abs(s - sum(nums) + elem) for elem in list(map(sum, itertools.combinations(nums, 2)))))