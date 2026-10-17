from math import isqrt

N = int(input())

ans = 0
fact = 2

for leng in range(3, 100):
    fact *= leng

    if fact > N:
        break

    if leng == 3:
        a = 1

        while a * (a + 1) * (a + 2) <= N:
            d = (isqrt(a ** 4 + 8 * a * N) - 3 * a * a) // (4 * a)

            if d > 0:
                ans += d

            a += 1

    else:
        a = 1

        while True:
            prod = 1

            for i in range(leng):
                prod *= a + i

                if prod > N:
                    break

            if prod > N:
                break

            a += 1

        a -= 1
        d = 1

        while a > 0:
            while a > 0:
                prod = 1

                for i in range(leng):
                    prod *= a + i * d

                    if prod > N:
                        break

                if prod <= N:
                    break

                a -= 1

            if a == 0:
                break

            ans += a
            d += 1

print(ans)
