a,b=map(int,input().split())
def itp(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
rst=0
for n in range(a,b+1):
    if itp(n):
        rst+=n
print(rst)