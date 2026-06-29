N, M = map(int, input().split())

curr = [0] * (N + 1)
event = [[] for _ in range(M + 1)]

for _ in range(N):
    A, D, B = map(int, input().split())

    curr[A] += 1
    event[D].append((A, B))

ans = 0
for color in range(1, N + 1):
    if curr[color] > 0:
        ans += 1

for day in range(1, M + 1):
    for A, B in event[day]:
        if curr[A] == 1:
            ans -= 1
        curr[A] -= 1

        if curr[B] == 0:
            ans += 1
        curr[B] += 1

    print(ans)
