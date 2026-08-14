N, R = map(int, input().split())
A = list(map(int, input().split()))

minim = min(A)
ans = 0

for i in range(N):
    ans += A[i] - minim

print(ans)
