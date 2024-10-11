n=int(input())
nums=list(map(int, input().split()))
nums.sort()
diff=[]
for i in range(n):
    diff.append(nums[i+n]-nums[i])

print(min(diff))