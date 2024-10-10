n=int(input())
#carry가 있는지 판단 방법? 흠...
#3개의 숫자를 고르는 방법: 3중 for문?
#각각 더해본 후 carry 유무 판단 => 없을 시에 max_ans와 크기를 비교하여 최댓값 갱신
#==> print(max_ans)
max_ans=-1
nums=[
    int(input())
    for _ in range(n)
]
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

for a in nums:
    for b in nums:
        for c in nums:
            if has_no_carry(a,b,c):
                sum=a+b+c
                max_ans=max(max_ans, sum)

print(max_ans)