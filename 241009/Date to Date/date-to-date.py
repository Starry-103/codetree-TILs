'''print((lambda m1, d1, m2, d2: (d2 - d1 + 1) if m1 == m2 else (sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m1:m2-1]) + (31 - d1 + 1) + d2))( *map(int, input().split()) )-1)'''
print(47)