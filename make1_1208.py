#21/12/08
#1이 될 때  까지 문제

cnt = 0

N, K = input('입력 : ').split()
N = int(N)
K = int(K)
while(N != 1):
    if(N % K == 0):
        cnt += 1
        N //= K 

    else:
        cnt += 1
        N -= 1

print(cnt)