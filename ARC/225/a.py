N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

conv = [0, 2, 4, 1, 3]

for row in X:
    print(*(conv[x] for x in row))
