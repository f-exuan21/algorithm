import heapq

n = int(input())
q = []
result = []
for _ in range(n):
	num = int(input())
	if num != 0:
		heapq.heappush(q, num)
	else:
		if q:
			result.append(heapq.heappop(q))
		else:
			result.append(0)

for r in result:
	print(r)
