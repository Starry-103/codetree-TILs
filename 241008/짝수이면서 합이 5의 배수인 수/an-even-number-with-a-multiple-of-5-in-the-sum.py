n=int(input())
def is_the_number(n):
    if n%2 != 0:
        return 0
    elif (n//10 + n%10)%5!=0:
        return 0

    else:
        return 1

if  is_the_number(n):
    print("Yes")
else:
    print("No")