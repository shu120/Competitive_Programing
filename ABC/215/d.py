# D - Coprime 2
N, M = map(int, input().split())
A = list(map(int, input().split()))

prime = set()

for x in A:
    p = 2

    while p * p <= x:
        while x % p == 0:
            prime.add(p)
            x //= p

        p += 1

    if x > 1:
        prime.add(x)

ok = [True] * (M + 1)

for p in prime:
    for x in range(p, M + 1, p):
        ok[x] = False

ans = []

for x in range(1, M + 1):
    if ok[x]:
        ans.append(x)

print(len(ans))
print(*ans, sep="\n")
