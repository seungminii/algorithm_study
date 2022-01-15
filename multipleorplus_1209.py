#21/12/09
#곱하기 혹은 더하기 문제


S = list(map(int, input())) # 정수로 변환
ans = S[0]
for i in range(1,len(S)):
    if ans >= 1 and S[i] >= 1:
        ans *= S[i]
    else:
        ans += S[i]

print(ans)