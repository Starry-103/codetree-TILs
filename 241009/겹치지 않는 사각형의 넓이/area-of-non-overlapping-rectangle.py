# 입력 받기
a, b, c, d = map(int, input().split())  # 첫 번째 직사각형 좌표
q, w, e, r = map(int, input().split())  # 두 번째 직사각형 좌표

# 첫 번째 직사각형의 넓이 구하기
out = abs((a - c) * (b - d)) + abs((q - e) * (w - r))

# 입력 받기 (겹치는 부분 확인용 좌표)
u, i, o, p = map(int, input().split())

# 첫 번째 직사각형과 세 번째 직사각형의 겹치는 부분 계산
temp = []
temptemp = []

# x좌표 처리
if a < u < c:
    temp.append(u)
if a < o < c:
    temp.append(o)
if u < a < o:
    temp.append(a)
if u < c < o:
    temp.append(c)

# y좌표 처리
if b < i < d:
    temptemp.append(i)
if b < p < d:
    temptemp.append(p)
if i < b < p:
    temptemp.append(b)
if i < d < p:
    temptemp.append(d)

# 겹치는 부분이 있으면 넓이를 계산해서 빼줌
if len(temp) == 2 and len(temptemp) == 2:
    out -= abs((temp[0] - temp[1]) * (temptemp[0] - temptemp[1]))

# 첫 번째 직사각형 좌표를 두 번째 직사각형으로 변경
a, b, c, d = q, w, e, r
temp, temptemp = [], []

# 두 번째 직사각형과 세 번째 직사각형의 겹치는 부분 계산
# x좌표 처리
if a < u < c:
    temp.append(u)
if a < o < c:
    temp.append(o)
if u < a < o:
    temp.append(a)
if u < c < o:
    temp.append(c)

# y좌표 처리
if b < i < d:
    temptemp.append(i)
if b < p < d:
    temptemp.append(p)
if i < b < p:
    temptemp.append(b)
if i < d < p:
    temptemp.append(d)

# 겹치는 부분이 있으면 넓이를 계산해서 빼줌
if len(temp) == 2 and len(temptemp) == 2:
    out -= abs((temp[0] - temp[1]) * (temptemp[0] - temptemp[1]))

# 최종 결과 출력
print(out)