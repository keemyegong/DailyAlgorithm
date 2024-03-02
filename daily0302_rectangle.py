# [BAEKJOON] 직사각형 네개의 합집합의 면적 구하기

arr = [[0]*100 for _ in range(100)]

for _ in range(4):
  lx, ly, rx, ry = map(int, input().split())

  for x in range(lx, rx):
    for y in range(ly, ry):
      arr[x][y] += 1

result = 0
for i in range(100):
  for j in range(100):
    if arr[i][j] > 0:
      result += 1

print(result)