#024 - Select +／- One（★2
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

minop = 0
for i in range(N):
    minop += abs(A[i] - B[i])

if minop <= K and (K - minop) % 2 == 0:
    print("Yes")
else:
    print("No")
