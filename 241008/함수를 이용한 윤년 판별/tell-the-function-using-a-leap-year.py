y=int(input())
def iy(n):
    if n%4 != 0:
        return False
    elif n%100 == 0 and n%400 != 0:
        return False
    else:
        return True

if iy(y):
    print("true")
else:
    print("false")