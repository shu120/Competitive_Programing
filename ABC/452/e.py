import sys
input = sys.stdin.readline

MOD = 998244353

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

presum = [0] * (N + 1)
for i in range(N):
    presum[i + 1] = presum[i] + A[i]

sumB = sum(B) % MOD

sumA = 0
for i, a in enumerate(A, 1):
    sumA = (sumA + a * i) % MOD

term1 = sumA * sumB % MOD

term2 = 0

for j in range(1, M + 1):
    Bj = B[j - 1]
    if Bj == 0:
        continue

    k = 1
    while k * j <= N:
        n = k * j
        r = min((k + 1) * j - 1, N)
        s = presum[r] - presum[n - 1]
        term2 = (term2 + Bj * j * k % MOD * s) % MOD
        k += 1

ans = (term1 - term2) % MOD
print(ans)
