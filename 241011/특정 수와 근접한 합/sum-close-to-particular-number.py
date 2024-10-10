import itertools
n, s, *nums = map(int, input().split())
print(min(abs(s - sum(nums) + elem) for elem in list(map(sum, itertools.combinations(nums, 2)))))