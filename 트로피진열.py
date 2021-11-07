from abc import abstractproperty


n = int(input())
array = []

for _ in range(n):
	array.append(int(input()))

max = 0
left = 0
for i in array:
	if max < i:
		max = i
		left += 1
max = 0
right = 0
for i in array[::-1]:
	if max < i:
		max = i
		right += 1
print(left)
print(right)
