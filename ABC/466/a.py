N = int(input())
X = list(map(int, input().split()))

if all(i < 0 for i in X):
    print("Yes")
else:
    print("No")
