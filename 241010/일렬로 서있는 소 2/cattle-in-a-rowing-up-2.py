n=int(input())
cowlist=list(map(int,input().split()))
cnt=0
for indi, i in enumerate(cowlist):
    for indj, j in enumerate(cowlist[indi+1:]):
        if j>=i:
            for k in cowlist[indi+indj+2:]:
                if k>=j:
                    cnt+=1
print(cnt)