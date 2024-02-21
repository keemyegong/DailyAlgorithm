# [SWEA] 5176. 이진탐색 

T = int(input())

def inorder(node): # 중위순회
  if node != 0:
    inorder(left[node])
    result.append(node)
    inorder(right[node])

for test_case in range(1, T+1):
  N = int(input())
  left = [0] * (N+1)
  right = [0] * (N+1)

  for i in range(1, N): # 부모 노드 인덱스에 자식 노드 인덱스 저장
    if i*2 == N: # 트리의 끝에 왼쪽 자식만 있을 경우
      left[i] = i*2
      break
    if i*2+1 == N: # 오른쪽 자식까지 있을 경우
      left[i] = i*2
      right[i] = i*2+1
      break
    left[i] = i*2 # 부모 인덱스에 왼쪽 자식 노드 저장
    right[i] = i*2+1 # 오른쪽 자식 노드 저장

  result = [0]
  inorder(1)
  print(result)
  print(f'#{test_case} {result.index(1)} {result.index(N//2)}')
