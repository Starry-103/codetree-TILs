n = int(input())
nums = [int(input()) for _ in range(n)]
max_ans = -1

def has_no_carry(x, y, z):
    # 각 숫자를 문자열로 변환한 후, 자릿수를 맞춰줌
    max_len = max(len(str(x)), len(str(y)), len(str(z)))
    str_x = str(x).zfill(max_len)
    str_y = str(y).zfill(max_len)
    str_z = str(z).zfill(max_len)
    
    # 각 자리수를 더해서 carry가 발생하는지 확인
    for i in range(max_len):
        digit_sum = int(str_x[i]) + int(str_y[i]) + int(str_z[i])
        if digit_sum >= 10:
            return False  # carry 발생
    return True  # carry 발생 안 함

# 중복 없이 3개의 숫자 고르기 (i < j < k 조건을 이용)
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if has_no_carry(nums[i], nums[j], nums[k]):
                sum_value = nums[i] + nums[j] + nums[k]
                max_ans = max(max_ans, sum_value)

print(max_ans)