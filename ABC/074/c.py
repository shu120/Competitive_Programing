#C - Sugar Water
import sys
input = sys.stdin.readline

A, B, C, D, E, F = map(int, input().split())

ans = 0
maxdens = 0
for na in range(F // (A * 100) + 1):
	remA = F - A * 100 * na
	for nb in range(remA // (B * 100) + 1):
		remB = remA - B * 100 * nb
		for nc in range(remB // C + 1):
			remC = remB - C * nc
			for nd in range(remC // D + 1):
				suger = C * nc + D * nd

				if suger <= (100 * A * na + 100 * B * nb) * E / 100 :
					liq = suger + 100 * (A * na + B * nb)
					if liq > 0:
						dens = 100 * suger / liq
						if dens > maxdens:
							ans = (liq, suger)
							maxdens = dens
				else:
					break

if ans == 0:
	print(A * 100, 0)
else:
	print(*ans)