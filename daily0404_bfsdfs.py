from collections import deque

def DFS(node):
  DFS_visited[node] = True # 방문 처리
  print(node, end=' ') # 현재 방문 노드 출력
  for i in range(1, N+1):
    if not DFS_visited[i] and graph[node][i]: # 방문하지 않은 연결된 노드라면
      DFS(i) # 재귀 호출 (재귀는 반복문 처음부터 다시 돌면서 연결된 노드 전부 탐색)

def BFS(node):
  q = deque([node]) # 데크에 출발점 노드 넣고 시작
  BFS_visited[node] = True # 방문 처리
  while q: # 큐가 빌 때까지
    node = q.popleft() # 방문할 노드 pop
    print(node, end = ' ') # 현재 방문 노드 출력
    for i in range(1, N+1):
      if not BFS_visited[i] and graph[node][i]: # 방문하지 않은 연결된 노드라면
        q.append(i) # 방문할 노드 추가
        BFS_visited[i] =  True

N, M, V = map(int, input().split())
# 정점의 개수, 간선의 개수, 탐색 시작 정점 번호

graph = [[False] * (N+1) for _ in range(N+1)]
DFS_visited = [False] * (N+1)
BFS_visited = [False] * (N+1)

# 그래프 인접 노드 저장
for i in range(M):
  n1, n2 = map(int, input().split())
  graph[n1][n2] = True
  graph[n2][n1] = True

DFS(V)
print()
BFS(V)