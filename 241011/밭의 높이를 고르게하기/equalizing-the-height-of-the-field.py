n, h, t = map(int, input().split())
heights = list(map(int, input().split()))

# 초기 구간의 비용 계산
cost = sum(abs(heights[i] - h) for i in range(t))
costlist = [cost]

# 슬라이딩 윈도우 방식으로 비용 갱신
for i in range(1, n - t + 1):
    # 이전 구간의 비용에서 빠진 부분 빼고, 새로 추가된 부분 더하기
    cost += abs(heights[i + t - 1] - h) - abs(heights[i - 1] - h)
    costlist.append(cost)

print(min(costlist))