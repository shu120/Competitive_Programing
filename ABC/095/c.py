a, b, c, x, y = map(int, input().split())

cost1 = a * x + b * y

pair = min(x, y)
cost2 = c * 2 * pair + a * (x - pair) + b * (y - pair)

cost3 = c * 2 * max(x, y)

ans = min(cost1, cost2, cost3)
print(ans)