N, D = map(int, input().split())
X = list(map(int, input().split()))

ans = []

for i in range(N):
    ok = True

    for j in range(N):
        if i == j:
            continue

        if abs(X[i] - X[j]) < D:
            ok = False
            break

    if ok:
        ans.append(i + 1)

print(len(ans))
print(*ans)
