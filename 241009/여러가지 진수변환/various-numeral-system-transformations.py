n, b = map(int, input().split())
def my_chan(n,b):
    if n<b:
        return str(n)

    return my_chan(n//b, b) + str(n%b)

print(my_chan(n, b))