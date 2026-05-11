import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    xorsum = 0
    mod = K + 1

    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if (i + j) % 2 == 1:
                xorsum ^= row[j] % mod

    if xorsum:
        print("Alice")
    else:
        print("Bob")
