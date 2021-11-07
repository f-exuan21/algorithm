import heapq

INF = int(1e9)

def solution(n, edge):
	distance = [INF] * (n + 1)
	graph = [[] for _ in range(n + 1)]

	for e in edge:
		graph[e[0]].append((1, e[1])) #거리비용, 연결된 노드
		graph[e[1]].append((1, e[0]))

	q = []
	distance[1] = 0
	heapq.heappush(q, (0, 1))
	while q:
		dist, now = heapq.heappop(q)
		if dist > distance[now]:
			continue
		for cost, node in graph[now]:
			if distance[node] > dist + cost:
				distance[node] = dist + cost
				heapq.heappush(q, (distance[node], node))

	max = 0
	cnt = 0
	for d in distance:
		if d == INF:
			continue
		if max < d:
			max = d
			cnt = 1
		elif max == d:
			cnt += 1

	return (cnt)

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
