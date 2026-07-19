import sys
input = sys.stdin.readline

T = int(input())
ans = []

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    win = False
    cnt = 0

    for a in A + [0]:
        if a:
            cnt += 1
        else:
            if cnt and cnt != 2:
                win = True
            cnt = 0

    ans.append("Alice" if win else "Bob")

print("\n".join(ans))
