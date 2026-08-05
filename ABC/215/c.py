# C - One More aab aba baa
from itertools import permutations

S, K = map(str, input().split())
K = int(K)

words = set(permutations(S))
words = sorted(words)

print("".join(words[K - 1]))
