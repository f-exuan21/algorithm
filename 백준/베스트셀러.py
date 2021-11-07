n = int(input())

array = {}

for _ in range(n):
	book = input()
	if book not in array:
		array[book] = 1
	else:
		array[book] += 1

target = max(array.values())

result = []
for book, number in array.items():
	if target == number:
		result.append(book)

result = sorted(result)
print(result[0])
