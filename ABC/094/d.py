#D - Binomial Coefficients
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

N = max(a)
ans = -1
best = -1

for i in a:
    if i == N:
        continue

    score = min(i, N - i)

    if score > best:
        best = score
        ans = i

print(N, ans)
