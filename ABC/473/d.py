N, K = map(int, input().split())

A = [0] * N
ans = []


def dfs(i, total):
    if i == N - 1:
        remain = K - total

        if remain % N == 0:
            A[i] = remain // N
            ans.append(A.copy())

        return

    coef = i + 1

    for x in range((K - total) // coef + 1):
        A[i] = x
        dfs(i + 1, total + coef * x)


dfs(0, 0)

for a in ans:
    print(*a)
