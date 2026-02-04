#014 - We Used to Sing a Song Together（★3）
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])

print(ans)