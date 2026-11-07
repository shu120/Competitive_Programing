N, Q = map(int, input().split())
K = list(map(int, input().split()))

A = list(range(1, N + 1))

for k in K:
    tmp = []
    for i in range(k - 1, -1, -1):
        tmp.append(-A[i])

    for i in range(k):
        A[i] = tmp[i]

for X in A:
    print(X)
