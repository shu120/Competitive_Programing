#C - Special Trains
import sys
input = sys.stdin.readline

N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    ans = 0

    for j in range(i, N - 1):
        c, s, f = CSF[j]

        if ans <= s:
            ans = s + c
        else:
            if ans % f == 0:
                ans += c
            else:
                ans += f - ans % f
                ans += c
    print(ans)

print(0)
