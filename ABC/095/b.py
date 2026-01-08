n, x = map(int, input().split())
m = [int(input()) for _ in range(n)]

least = sum(m)
remain = x -least
ans = n + (remain // min(m))
print(ans)