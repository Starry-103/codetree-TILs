from itertools import combinations
skill=list(map(int, input().split()))
diff=(list((abs(sum(skill)-2*sum(elem))) for elem in combinations(skill, 3)))
print(min(diff))