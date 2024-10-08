n = int(input())
l = list(map(int, input().split()))
l1=sorted(l)
l2=l1[::-1]
print(" ".join(map(str, l1)))
print(' '.join(map(str,l2)))