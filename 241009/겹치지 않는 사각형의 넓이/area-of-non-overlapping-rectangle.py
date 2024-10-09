'''l=[[0 for _ in range(2000)] for _ in range(2000)]
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1+1000, x2+1000):
        for j in range(y1+1000, y2+1000):
            l[i][j]=1

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1+1000, x2+1000):
    for j in range(y1+1000, y2+1000):
        l[i][j]=0

result=0
for k in l:
    result+=k.count(1)


print(result)'''
a,b,c,d = map(int,input().split())
q,w,e,r = map(int,input().split())

out = (a-c)*(b-d) + (q-e)*(w-r)

u,i,o,p = map(int,input().split())


temp = []
temptemp = []
if a<u<c:
    temp.append(u)
if a<o<c:
    temp.append(o)
if u<a<o:
    temp.append(a)
if u<c<o:
    temp.append(c)
if b<i<d:
    temptemp.append(i)
if b<p<d:
    temptemp.append(p)
if i<b<p:
    temptemp.append(b)
if i<d<p:
    temptemp.append(d)

out -= abs((temp[0]-temp[1])*(temptemp[0]-temptemp[1]))

a,b,c,d = q,w,e,r
temp,temptemp = [],[]

if a<u<c:
    temp.append(u)
if a<o<c:
    temp.append(o)
if u<a<o:
    temp.append(a)
if u<c<o:
    temp.append(c)
if b<i<d:
    temptemp.append(i)
if b<p<d:
    temptemp.append(p)
if i<b<p:
    temptemp.append(b)
if i<d<p:
    temptemp.append(d)

out -= abs((temp[0]-temp[1])*(temptemp[0]-temptemp[1]))

print(out)