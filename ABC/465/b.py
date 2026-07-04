X, Y, L, R, A, B = map(int, input().split())

inside = max(0, min(B, R) - max(A, L))

total = B - A
outside = total - inside

ans = inside * X + outside * Y
print(ans)
