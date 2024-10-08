n=int(input())
l=list(map(int, input().split()))
for n in l:
    if n%2==0:
        print(int(n/2), end=' ')
    else:
        print(int(n), end=' ')