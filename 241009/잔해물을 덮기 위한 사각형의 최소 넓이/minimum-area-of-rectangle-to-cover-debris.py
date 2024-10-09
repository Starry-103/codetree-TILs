l = [[0 for _ in range(2000)] for _ in range(2000)]

# 첫 번째 직사각형 좌표 입력 및 채우기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1+1000, x2+1000):
    for j in range(y1+1000, y2+1000):
        l[i][j] = 1  # 첫 번째 직사각형을 1로 채움

# 두 번째 직사각형 좌표 입력 및 0으로 덮어씌우기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1+1000, x2+1000):
    for j in range(y1+1000, y2+1000):
        l[i][j] = 0  # 두 번째 직사각형을 0으로 덮어씌움

# 남아있는 1의 좌표에서 최소, 최대 x, y 찾기
min_x = 2000
min_y = 2000
max_x = 0
max_y = 0

found = False  # 유효한 좌표가 있는지 확인하는 플래그
for i in range(2000):
    for j in range(2000):
        if l[i][j] == 1:
            found = True
            if i < min_x:
                min_x = i
            if i > max_x:
                max_x = i
            if j < min_y:
                min_y = j
            if j > max_y:
                max_y = j

# 유효한 좌표가 있으면 면적 계산, 없으면 0 출력
if found:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
else:
    print(0)  # 만약 남아있는 1이 없다면, 면적은 0