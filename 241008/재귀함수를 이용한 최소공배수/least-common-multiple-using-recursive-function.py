import math


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_of_list(numbers, n):
    
    if n == 1:
        return numbers[0]
    
    return lcm(numbers[n-1], lcm_of_list(numbers, n-1))

n = int(input())
numbers = list(map(int, input().split()))

result = lcm_of_list(numbers, n)

print(result)