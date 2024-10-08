a, b = map(int,input().split())
l=[3,6,9]
cnt=0
def itn(n):
    if n//10 in l or n%10 in l or n%3==0:
        return 1
for n in range(a,b+1):
    if itn(n):
        cnt+=1
        
print(cnt)