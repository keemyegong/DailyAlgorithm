# [BAEKJOON] 2628. 종이 자르기

x, y = map(int, input().split())
n = int(input())

x_list = [0] # x 값 담을 리스트, x 시작 좌표 0 할당
y_list = [0] # y 값 담을 리스트, y 시작 좌표 0 할당

for _ in range(n): # 컷팅 x, y 값 각 리스트에 할당
  xy, idx = map(int, input().split())
  if xy == 1:
    x_list.append(idx)
  else:
    y_list.append(idx)
x_list.append(x) # x 마지막 좌표 할당
y_list.append(y) # y 마지막 좌표 할당

x_list.sort(reverse=True) # 큰 값에서 작은 값 뺴기 위해 역정렬
y_list.sort(reverse=True)

max_size = 0 # 최대값
for x in range(len(x_list)-1): # 면적 완전 탐색
  for y in range(len(y_list)-1):
    size = (x_list[x] - x_list[x+1]) * (y_list[y] - y_list[y+1])
    if size > max_size:
      max_size = size

print(max_size)