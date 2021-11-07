n, m = map(int, input().split())

graph = []

for _ in range(n):
	graph.append(list(input()))

row = [0] * n
col = [0] * m
for i in range(n):
	for j in range(m):
		if graph[i][j] == 'X':
			row[i] = 1
			col[j] = 1

row_count = 0
for i in range(n):
	if row[i] == 0:
		row_count += 1

col_count = 0
for j in range(m):
	if col[j] == 0:
		col_count += 1

print(max(row_count, col_count))
