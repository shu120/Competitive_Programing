#D - Various Sushi
N, K = map(int, input().split())

sushi = []
for _ in range(N):
    t, d = map(int, input().split())
    sushi.append((t, d))

sushi.sort(key=lambda x: x[1], reverse=True)

used = set()
dup = []
total = 0

for t, d in sushi[:K]:
    total += d

    if t in used:
        dup.append(d)
    else:
        used.add(t)

x = len(used)
ans = total + x * x

for t, d in sushi[K:]:
    if t in used:
        continue

    if not dup:
        break

    total -= dup.pop()
    total += d
    used.add(t)

    x += 1
    ans = max(ans, total + x * x)

print(ans)
