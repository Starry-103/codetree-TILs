a, b = map(int,input().split())
l=[3,6,9]
cnt=0
def itn(n):
    str_n=str(n)
    if '3' in str_n or '6' in str_n or '9' in str_n or n%3==0:
        return 1
for n in range(a,b+1):
    if itn(n):
        cnt+=1
        
print(cnt)