n, m = map(int,input().split())
l=list(map(int,input().split()))
for _ in range(m):
    rst=0
    a1, a2=map(int, input().split())
    for i in range(a1-1, a2):
        rst+=l[i]
    print(rst)