# 백준 2839

# 설탕 무게
n = int(input())

# 봉지 개수
count = 0
while n >= 0:
	if n % 5 == 0:
		count += n // 5
		break
	n -= 3
	count += 1

if n < 0:
	print(-1)
else:
	print(count)
