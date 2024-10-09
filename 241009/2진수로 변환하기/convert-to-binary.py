n=int(input())
def my_bin(n):
    if n==0:
        return '0'
    elif n==1:
        return '1'

    if n%2==0:
        return my_bin(n//2) + '0'
    else:
        return my_bin(n//2)+'1'

print(my_bin(n))