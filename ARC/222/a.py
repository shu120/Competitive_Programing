import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    K = 1

    for _ in range(M):
        L, R = map(int, input().split())
        K = max(K, R - L + 1)

    ans = []

    for i in range(N):
        ans.append(i % K + 1)

    print(*ans)
