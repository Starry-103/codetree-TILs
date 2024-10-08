a, b = map(int,input().split())
def myfunc(a,b):
    if a>=b:
        a=2*a
        b=b+10
    else:
        a=a+10
        b=2*b
    print(a,b)

myfunc(a,b)