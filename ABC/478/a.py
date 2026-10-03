N, M = map(int, input().split())

q = M // N
r = M % N

for i in range(N):
    if i < r:
        print(q + 1)
    else:
        print(q)
