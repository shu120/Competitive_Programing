import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X, Y, K = map(int, input().split())

    dist = {}

    curr = X
    cnt = 0

    while True:
        dist[curr] = cnt

        if curr == 0:
            break

        curr //= K
        cnt += 1

    curr = Y
    cnt = 0

    while True:
        if curr in dist:
            ans = dist[curr] + cnt
            print(ans)
            break

        curr //= K
        cnt += 1
