# [BAEKJOON] 2309. 일곱 난쟁이
  # 부분집합으로 개수 N, 합 M이 되는 집합 탐색

dwarfs = [int(input()) for _ in range(9)]
N = 7 # 원소 개수
M = 100 # 원소 합

result_list = []

for i in range(1 << 9):
  arr_list = []
  for j in range(9):
    if i & (1 << j):
      arr_list.append(dwarfs[j])
  if sum(arr_list) == M and len(arr_list) == N:
    result_list = arr_list

result_list.sort()
for result in result_list:
  print(result)