N = int(input())

ans = 0
r = 1

for _l in range(1, N):
    r = max(r, _l)

    while r < N:
        print("?", _l, r + 1, flush=True)
        res = input()

        if res == "Yes":
            r += 1
        else:
            break

    ans += r - _l

print("!", ans, flush=True)
