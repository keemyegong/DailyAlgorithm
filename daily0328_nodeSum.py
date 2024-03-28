# [SWEA] 5178. 노드의 합

def nodesum(node):
  if node <= N / 2:
    nodesum(2*node)
    nodesum(2*node+1)
    tree[node] = tree[2*node+1] + tree[2*node]

T = int(input())

for test_case in range(1, T + 1):
  N, M, L = map(int, input().split())
  # N: 노드의 개수
  # M: 리프 노드의 개수
  # L: 값을 출력할 노드 번호

  tree = [0] * (N + 2)

  for _ in range(M):
    idx, node = map(int, input().split())
    tree[idx] = node

  nodesum(1)
  print(f'#{test_case} {tree[L]}')