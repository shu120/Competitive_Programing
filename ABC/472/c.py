N, M, K = map(int, input().split())
A = list(map(int, input().split()))

eat = [0] * N
total = 0

for i in range(N):
    if i >= M:
        total -= eat[i - M]

    if total + A[i] <= K:
        print("Yes")
        eat[i] = A[i]
        total += A[i]
    else:
        print("No")
