import sys
input = sys.stdin.readline

MOD = 998244353

T = int(input())

for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))

    a = 0

    while a < N and P[a] == a + 1:
        a += 1

    ans = a * N - a * (a + 1) // 2

    if a == N:
        ans += 1

    print(ans % MOD)
