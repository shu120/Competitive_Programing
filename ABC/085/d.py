#D - Katana Thrower
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
A =[]
B =[]
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

mxA = max(A)

B.sort(reverse=True)

ans = 0

for b in B:
    if b <= mxA:
        break
    H -=b
    ans += 1
    if H <= 0:
        print(ans)
        exit()

if H > 0:
    ans += (H + mxA - 1) // mxA

print(ans)
