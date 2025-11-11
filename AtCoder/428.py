# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    428.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/19 15:18:51 by shukondo          #+#    #+#              #
#    Updated: 2025/10/19 15:22:43 by shukondo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#A
s, a, b, x = map(int, input().split())

t = a + b
ans = (x//t * a * s + min(x % t, a) * s)
print(ans)


#B
n, k = map(int, input().split())
s = input().strip()

count = {}

for i in range(n - k + 1):
	sub = s[i:i+k]
	count[sub] = count.get(sub, 0) + 1

x = max(count.values())

cand = []
for t in count:
	if count[t] == x:
		cand.append(t)
cand.sort()

print(x)
print(' '.join(cand))


#C
import sys
input = sys.stdin.readline
out = []

Q = int(input())

stack = [(0, 0)]

for _ in range(Q):
	q = input().split()
	if q[0] == '1':
		c = q[1]
		balance, m = stack[-1]
		if c == '(':
			balance += 1
		else:
			balance -= 1
		m = min(m, balance)
		stack.append((balance, m))
	else:
		stack.pop()

	balance, m = stack[-1]
	out.append("Yes" if balance == 0 and m >= 0 else "No")

print("\n".join(out))