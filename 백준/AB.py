# 백준 16953

a, b = map(int, input().split())
result = 0
while b > a:
	if b % 2 == 0:
		b //= 2
		result += 1
	elif b % 10 == 1:
		b //= 10
		result += 1
	else:
		break
if a == b:
	print(result + 1)
else:
	print(-1)
