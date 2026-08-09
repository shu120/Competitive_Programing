T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 0
    curr = 0

    for i in range(M - 1, -1, -1):
        curr = curr * 2 + A[i]

        cnt = (curr + N - 1) // N
        ans = max(ans, cnt * (2 ** i))

    print(ans)
