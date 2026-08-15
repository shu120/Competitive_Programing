N = int(input())
A = sorted(list(map(int, input().split())))

coord = 0
ans = 0

r = 0
while r < N and A[r] < 0:
    r += 1

_l = r - 1

for _ in range(N):
    if _l < 0:
        nxt = A[r]
        r += 1

    elif r >= N:
        nxt = A[_l]
        _l -= 1

    elif abs(coord - A[_l]) <= abs(coord - A[r]):
        nxt = A[_l]
        _l -= 1

    else:
        nxt = A[r]
        r += 1

    ans += abs(coord - nxt)
    coord = nxt

print(ans)
