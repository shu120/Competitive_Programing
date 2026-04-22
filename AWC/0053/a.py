N = input()
A = list(map(int, input().split()))

if sum(A) % 2 == 0:
    print("Aoki")
else:
    print("Takahashi")
