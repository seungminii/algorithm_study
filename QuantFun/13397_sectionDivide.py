#22.01.08 
#백준 13397번 구간나누기2

N, M = map(int, input().split())
arr = list(map(int, input().split()))

def devide(x):
    cnt = 1
    minX = maxX = arr[0]
    for i in range(1, N):
        minX = min(minX, arr[i])
        maxX = max(maxX, arr[i])
        if maxX - minX > x:
            cnt += 1
            minX = maxX = arr[i] 
    return cnt

left = result = 0
right = max(arr)

while(left <= right):
    mid = (left + right) // 2
    if devide(mid) <= M:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)

