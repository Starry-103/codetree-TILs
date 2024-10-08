y, m, d = map(int, input().split())
def iy(y):
    if y%4 != 0:
        return 0
    elif y%100 == 0 and y%400 != 0:
        return 0
    else:
        return 1
md1=31
md2=30
md3=28
if iy(y):
    md3=29

if (m==2 and d<=md3) or (m in [1,3,5,7,8,10,12] and d<=31) or (m in [4,6,9,11] and d<=30):
    if m in [3,4,5]:
        print("Spring")
    elif m in [6,7,8]:
        print("Summer")
    elif m in [9,10,11]:
        print("Fall")
    else:
        print("Winter")
    
else:
    print("-1")