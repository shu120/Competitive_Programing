N = int(input())
A = list(map(int, input().split()))

c1 = 0
c10 = 0
c100 = 0

for a in A:
    x = (-a) % 1000

    c100 += x // 100
    c10 += x // 10 % 10
    c1 += x % 10

print(c1, c10, c100)
