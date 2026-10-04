import sys
input = sys.stdin.readline

T = int(input())
H = 1024

for _ in range(T):
    A, B, C = map(int, input().split())
    seen = [False] * (C + 1)

    for x in range(A):
        for y in range(B):
            z = x ^ y
            if z <= C:
                seen[z] = True

    if seen[C]:
        print("No")
        continue

    meX = list(range(A))
    meY = list(range(B))

    meX.append(H)

    for z in range(C):
        if not seen[z]:
            meY.append(H | z)

    print("Yes")
    print(len(meX), *meX)
    print(len(meY), *meY)
