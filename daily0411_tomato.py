from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
check = True
q = deque([])
result = 0

# 출발점 찾기
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      q.append((i, j))

# 너비우선탐색
def BFS():
  global result
  while q:
    cur_i, cur_j = q.popleft()
    for d in dirs:
      ni, nj = cur_i + d[0], cur_j + d[1]
      if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
        q.append((ni, nj))
        arr[ni][nj] = arr[cur_i][cur_j] + 1 # 값 1씩 늘려가며 탐색 횟수 기록
        if arr[ni][nj] > result: # 최대값 갱신
          result = arr[ni][nj]

BFS()

for i in range(N): # 자라지 않은 토마토가 있는 경우
  if 0 in arr[i]:
    check = False # check 변수 False 처리
    print(-1)
    break

if check: # check가 True인 경우
    if not result: # result가 0이라면 (탐색하지 않았다면)
        print(0)
    else: # 값이 0부터 시작했으므로 -1
        print(result - 1)