#D - Five, Five Everywhere
N = int(input())

ans = []

for x in range(2, 55556):
    is_prime = True

    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            is_prime = False
            break

    if is_prime and x % 5 == 1:
        ans.append(x)

    if len(ans) == N:
        break

print(*ans)
