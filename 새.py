# n = int(input())

# i = 1
# time = 0
# while n > 0:
# 	if i <= n:
# 		n -= i
# 	else:
# 		i = 1
# 		n -= i
# 	i += 1
# 	time += 1

# print(time)


n = int(input())
result = 0
k = 1

while n != 0:
	if k > n:
		k = 1
	n -= k
	k += 1
	result += 1

print(result)
