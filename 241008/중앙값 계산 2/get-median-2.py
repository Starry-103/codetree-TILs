n=int(input())
nl=list(map(int, input().split()))
def print_mid(n):
    print(sorted(nl[:(n+1)])[n//2], end=' ')

for i in range(n):
    if i%2==0:
        print_mid(i)