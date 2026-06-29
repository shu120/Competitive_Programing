import sys


def solve() -> None:
    input = sys.stdin.readline

    T = int(input())

    ans = []

    for _ in range(T):
        N = int(input())
        S = input()
        X = list(map(int, input().split()))
        Y = list(map(int, input().split()))

        if S[0] == "R":
            dp_r = 0
        else:
            dp_r = -X[0]

        if S[0] == "S":
            dp_s = 0
        else:
            dp_s = -X[0]

        for i in range(1, N):
            if S[i] == "R":
                cost_r = 0
                cost_s = -X[i]
            else:
                cost_r = -X[i]
                cost_s = 0

            new_r = max(dp_r, dp_s) + cost_r

            new_s = max(dp_s, dp_r + Y[i - 1]) + cost_s

            dp_r = new_r
            dp_s = new_s

        ans.append(str(max(dp_r, dp_s)))

    print("\n".join(ans))


solve()
