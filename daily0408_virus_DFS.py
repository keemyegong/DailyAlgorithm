# [BAEKJOON] 2606. 바이러스 - DFS 풀이

N = int(input()) # 컴퓨터의 수
line = int(input()) # 연결된 쌍의 수

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0

for i in range(line):
  node1, node2 = map(int, input().split())
  graph[node1][node2] = True
  graph[node2][node1] = True

def DFS(start): # 깊이 우선 탐색
  global cnt
  visited[start] = True
  for i in range(2, N+1): # 라인 수만큼 탐색
    if not visited[i] and graph[start][i]:
      cnt += 1
      DFS(i)

DFS(1)
print(cnt)