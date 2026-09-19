from bisect import bisect_right
N, M, K = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
ans = 0

sum_A = [0] * (N + 1)
for i in range(N):
    sum_A[i + 1] = sum_A[i] + A[i]

sum_B = [0] * (M + 1)
bill = [0] * (M + 1)
for i in range(M):
    sum_B[i + 1] = sum_B[i] + B[i]
    bill[i + 1] = bill[i] + (B[i] + K - 1) // K

money = X + K * Y

for j in range(M + 1):
    if bill[j] > Y:
        break
    rem = money - sum_B[j]
    if rem < 0:
        break
    i = bisect_right(sum_A, rem) - 1
    ans = max(ans, i + j)

print(ans)
