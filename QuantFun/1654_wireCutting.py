#22.10.10
#백준 1654번 랜선자르기
#매개변수 탐색(Parametric Search)

k,n = map(int,input().split())
arr = []
#arr = [0 for _ in range(k)]
#ans = [0 for _ in range(k)]

for _ in range(k):
    arr.append(int(input()))
#배열이 아닌 리스트라서 append 로 입력 받으면서 값을 넣으면 된다. -> 초기화 필요 없음(동적 가변 함수)

def cutting(x):
    sum = 0
    for i in range(k):
        sum += arr[i] // mid
    return sum

start, end = 0, max(arr)
ans = 0
while start <= end:
    mid = ( start + end ) // 2 
    if mid == 0:
        mid = 1
    if cutting(mid) < n:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)

