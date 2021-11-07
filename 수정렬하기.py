# 수 정렬하기

n = int(input())
nums = []

for _ in range(n):
	nums.append(int(input()))

# 선택 정렬 알고리즘
for i in range(n):
	min_index = i
	for j in range(i, n):
		if nums[j] < nums[min_index]:
			min_index = j
	nums[i], nums[min_index] = nums[min_index], nums[i]

for num in nums:
	print(num)
