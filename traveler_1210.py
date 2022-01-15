#21/12/10
#모험가 길드 문제

N = input()
group = 0
ans = 0
scared = sorted(list(map(int, input().split())))
for i in scared:
    group += 1
    if group >= i:
        ans += 1
        group = 0


print(ans)

