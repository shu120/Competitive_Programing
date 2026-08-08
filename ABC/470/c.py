N, Q = map(int, input().split())

A = [0] * N
notzero = set()

ans = 0

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x = q[1] - 1

        ans ^= A[x]
        A[x] += 1
        ans ^= A[x]

        notzero.add(x)

    else:
        for x in list(notzero):
            ans ^= A[x]
            A[x] -= 1
            ans ^= A[x]

            if A[x] == 0:
                notzero.remove(x)

    print(ans)
