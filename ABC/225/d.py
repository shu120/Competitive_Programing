# D - Play Train
N, Q = map(int, input().split())

prev = [-1] * N
nex = [-1] * N

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x = q[1] - 1
        y = q[2] - 1

        nex[x] = y
        prev[y] = x

    elif q[0] == 2:
        x = q[1] - 1
        y = q[2] - 1

        nex[x] = -1
        prev[y] = -1

    else:
        x = q[1] - 1

        while prev[x] != -1:
            x = prev[x]

        ans = []

        while x != -1:
            ans.append(x + 1)
            x = nex[x]

        print(len(ans), *ans)
