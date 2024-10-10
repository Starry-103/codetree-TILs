ans_max=0
n=int(input())
num_list=list(map(int, input().split()))
for i in range(0, n-2):
    for j in range(i+2, n):
        ans=num_list[i]+num_list[j]
        ans_max=max(ans, ans_max)

print(ans_max)