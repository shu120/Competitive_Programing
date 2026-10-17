N, K, T = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
ans = 0
t = 0

for a in A:
    if a > T:
        break

    if a > t:
        cnt = (a - t + K - 1) // K
        ans += cnt

    t = a + K

if t < T:
    ans += (T - t + K - 1) // K

print(ans)
