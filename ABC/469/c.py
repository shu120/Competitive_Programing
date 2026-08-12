N = int(input())
S = input()

pos = []

for i, c in enumerate(S, 1):
    if c == "x":
        pos.append(i)

for x in pos:
    print(x)

for _ in range(N - len(pos)):
    print(N)
