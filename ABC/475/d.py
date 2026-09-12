from itertools import permutations

S = input()

c = list(set(S))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for p in permutations("0123456789", len(c)):
    mp = dict(zip(c, p))

    if mp[S[0]] == "0":
        continue

    T = "".join(mp[c] for c in S)
    P = int(T)

    if is_prime(P):
        print(P)
        break
else:
    print(-1)
