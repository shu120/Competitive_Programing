N, Q = map(int, input().split())

mas = [False] * N
color = ["a"] * N
ver = [0] * N

curr = "a"
cnt = 0

for _ in range(Q):
    q = input().split()

    if q[0] == "1":
        X = int(q[1]) - 1

        if mas[X]:
            mas[X] = False
            ver[X] = cnt

        else:
            if ver[X] < cnt:
                color[X] = curr

            mas[X] = True

    else:
        curr = q[1]
        cnt += 1

for i in range(N):
    if not mas[i] and ver[i] < cnt:
        color[i] = curr

print("".join(color))
