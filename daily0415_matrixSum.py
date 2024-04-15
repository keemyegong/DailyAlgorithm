# [BAEKJOON] 2738. 행렬 덧셈

N, M = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(N)]
matrix2 = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]

for i in range(N):
  for j in range(M):
    result[i][j] += (matrix1[i][j] + matrix2[i][j])
  print(*result[i])