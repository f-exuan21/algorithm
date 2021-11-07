
# 숫자의 개수는 많은데, 범위가 작을 때는 계수정렬!!
import sys
input = sys.stdin.readline
n = int(input())
array = [0] * 10001

for _ in range(n):
	array[int(input())] += 1

for i in range(len(array)):
	for j in range(array[i]):
		print(i)
