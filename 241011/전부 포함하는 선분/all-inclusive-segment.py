n=int(input())
lines=[
    tuple(map(int, input().split()))
    for _ in range(n)
]
f1=sorted(lines, key= lambda x: x[0])[1:]
f2=sorted(lines, key= lambda x: x[1])[:-1]

length1=sorted(f1, key= lambda x: x[1])[-1][1]-f1[0][0]
length2=f2[-1][1]-sorted(f2, key= lambda x: x[0])[0][0]
ans=min(length1, length2)
print(ans)


#제일 앞 or 제일 뒤 제거 => 가장 작은 시작 ~ 가장 큰 끝 = 답
#제일 앞 or 제일 뒤 선분이 겹칠 경우 :