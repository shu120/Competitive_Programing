N, S, L = map(int, input().split())
A = list(map(int, input().split()))

pos = [0] * (N + 1)

for i in range(1, N):
    pos[i + 1] = pos[i] + A[i - 1]

ans = 1
right = S

for left in range(1, S + 1):
    x = pos[S] - pos[left]

    if x > L:
        continue

    while right + 1 <= N:
        y = pos[right + 1] - pos[S]

        cost = x + y + min(x, y)

        if cost <= L:
            right += 1
        else:
            break

    ans = max(ans, right - left + 1)

print(ans)
