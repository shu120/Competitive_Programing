# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    429.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/25 20:42:45 by shukondo          #+#    #+#              #
#    Updated: 2025/10/25 22:40:26 by shukondo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#A
n, m = map(int, input().split())

for i in range(1, n+1):
	if i <= m:
		print("OK")
	else:
		print("Too Many Requests")

#B
n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = sum(a)
ans = sum - m

if ans in a:
	print("Yes")
else:
	print("No")

#C
from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)

ans = 0
for i in count.values():
	ans += i * (i - 1) // 2 * (n - i)

print(ans)

#D
n, m, c = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
new_a = []
for i in a:
	new_a.append(i)
for i in a:
	new_a.append(i + m)

ans = 0

for j in range(n):
	index_stop = j + c - 1
	stop_pos = new_a[index_stop]

	if j + 1 < n:
		next_pos = a[j + 1]
	else:
		next_pos = a[0] + m
	len = next_pos - a[j]

	add_val = len * c
	ans += add_val

print(ans)