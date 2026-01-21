N = int(input())
a = list(map(int, input().split()))

print(max(set(a)) - min(set(a)))
