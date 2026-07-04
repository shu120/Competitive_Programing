from collections import deque

N = int(input())
S = input()

A = deque()
rev = False

for k in range(1, N + 1):
    if rev:
        A.appendleft(k)
    else:
        A.append(k)

    if S[k - 1] == 'o':
        if rev:
            rev = False
        else:
            rev = True

if rev:
    print(*reversed(A))
else:
    print(*A)
