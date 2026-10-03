N, K = map(int, input().split())
A = list(map(int, input().split()))

B = sorted(A)

diff = []

for i in range(N):
    if A[i] != B[i]:
        diff.append(i)

if not diff:
    print("Yes")
elif diff[-1] - diff[0] + 1 <= K:
    print("Yes")
else:
    print("No")
