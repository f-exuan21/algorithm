from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]

start = int(1e9)
end = 1

for _ in range(m):
	x, y, weight = map(int, input().split())
	adj[x].append((y, weight))
	adj[y].append((x, weight))
	start = min(start, weight)
	end = max(end, weight)

start_node, end_node = map(int, input().split())

def bfs(c):
	queue = deque([start_node])
	visited = [False] * (n + 1)
	visited[start_node] = True
	while queue:
		x = queue.popleft()
		for node, weight in adj[x]:
			if not visited[node] and weight >= c:
				queue.append(node)
				visited[node] = True
	return visited[end_node]


result = start
while start <= end:
	mid = (start + end) // 2
	if bfs(mid): # 이 중량으로 이동 가능한지 확인
		result = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)
