#D - 756
N = int(input())

e = [0] * (N + 1)

for i in range(2, N + 1):
    cur = i
    j = 2

    while j * j <= cur:
        while cur % j == 0:
            e[j] += 1
            cur //= j

        j += 1

    if cur > 1:
        e[cur] += 1


def num(m):
    return sum(x >= m - 1 for x in e)


ans = (
    num(75)
    + num(25) * (num(3) - 1)
    + num(15) * (num(5) - 1)
    + num(5) * (num(5) - 1) // 2 * (num(3) - 2)
)

print(ans)
