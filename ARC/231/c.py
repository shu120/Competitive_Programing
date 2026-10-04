import sys
input = sys.stdin.readline


def invalid(i, A, B, N):
    l = A[i] - B[i]
    r = A[i] + B[i]

    l_ng = False
    r_ng = False

    if i > 0:
        nl = A[i - 1] - B[i - 1]
        nr = A[i - 1] + B[i - 1]

        if nl < l < nr:
            l_ng = True
        if nl < r < nr:
            r_ng = True

    if i + 1 < N:
        nl = A[i + 1] - B[i + 1]
        nr = A[i + 1] + B[i + 1]

        if nl < l < nr:
            l_ng = True
        if nl < r < nr:
            r_ng = True

    return l_ng and r_ng


T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0

    for i in range(N):
        if invalid(i, A, B, N):
            cnt += 1

    Q = int(input())

    for _ in range(Q):
        P, S = map(int, input().split())
        P -= 1

        for i in range(max(0, P - 1), min(N, P + 2)):
            if invalid(i, A, B, N):
                cnt -= 1

        B[P] = S

        for i in range(max(0, P - 1), min(N, P + 2)):
            if invalid(i, A, B, N):
                cnt += 1

        if cnt == 0:
            print("Yes")
        else:
            print("No")
