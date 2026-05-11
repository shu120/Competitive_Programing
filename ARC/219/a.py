import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

S_set = set(S)

for s in S:
    flipped = ''.join('1' if c == '0' else '0' for c in s)

    if flipped not in S_set:
        print("Yes")
        print(s)
        sys.exit()

print("No")
