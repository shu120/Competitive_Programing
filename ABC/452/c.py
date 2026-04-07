import sys
input = sys.stdin.readline

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

M = int(input())
S = [input().strip() for _ in range(M)]

valid = set()

for s in S:
    for i, c in enumerate(s):
        valid.add((len(s), i + 1, c))

for s in S:
    if len(s) != N:
        print("No")
        continue

    ok = True
    for i in range(N):
        if (A[i], B[i], s[i]) not in valid:
            ok = False
            break

    print("Yes" if ok else "No")
