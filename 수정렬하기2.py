# 숫자 개수도 많고 범위도 클 때 >> 퀵정렬, 병합정렬, 힙 사용 or 기본 정렬 라이브러리 사용

n = int(input())

# 병합 정렬
# 분할정보 방식을 이용
# 절반씩 합치면서 정렬하면, 전체 리스트가 정렬
# 시간복잡도 O(NlogN)

array = []
for _ in range(n):
	array.append(int(input()))

def merge_sort(array):
	if len(array) <= 1:
		return array
	mid = len(array) // 2
	left = merge_sort(array[:mid])
	right = merge_sort(array[mid:])
	i, j, k = 0, 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			array[k] = left[i]
			i += 1
		else:
			array[k] = right[j]
			j += 1
		k += 1
	if i == len(left):
		while j < len(right):
			array[k] = right[j]
			k += 1
			j += 1
	else:
		while i < len(left):
			array[k] = left[i]
			k += 1
			i += 1

	return array

print(merge_sort(array))
