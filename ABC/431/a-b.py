# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    431.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: shukondo <shukondo@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/10 13:35:47 by shukondo          #+#    #+#              #
#    Updated: 2025/11/10 18:40:23 by shukondo         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#A
H, B = map(int, input().split())

d = H - B
if H > B:
	print(d)
else:
	print("0")
	
#A
H, B = map(int, input().split())
print(max(0, H-B)) #これ上手い

#B
X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())

for i in range(Q):
  p = int(input())
  X += W[p-1]
  print(X)
  W[p-1] *= -1