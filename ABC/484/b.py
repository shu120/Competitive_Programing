K = int(input())
A = list(map(int, input().split()))

A.sort()

if (A[-1] == 9):
    print(A[0])
else:
    print("-1")
