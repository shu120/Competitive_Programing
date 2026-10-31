N = int(input())
X = list(map(int, input().split()))

ans = []

for i in range(N):
    if i == 0:
        ans.append((X[-1] - X[0]) // 2)
        continue

    if i == N - 1:
        ans.append((X[-1] - X[0]) // 2)
        continue

    left = max(X[i] - X[0], X[-1] - X[i - 1]) // 2
    right = max(X[i + 1] - X[0], X[-1] - X[i]) // 2

    ans.append(min(left, right))

print(*ans, sep="\n")
