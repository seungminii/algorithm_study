#21/12/10
#상하좌우 문제

N = int(input())
plan = list(input().split())
print(plan)
array = [[0 for col in range(N)] for row in range(N)]

x, y = 1, 1
for i in plan:
    #print(i)
    if i == 'L':
        y -= 1 
        if(y < 1):
            y += 1
            continue
    elif i == 'R':
        y += 1
        if(y > N):
            y -= 1
            continue
    elif i == 'D':
        x += 1

        if(x > N):
            x -= 1
            continue
    elif i == 'U':
        x -= 1 
        if(x < 1):
            x += 1
            continue
print(x, y)