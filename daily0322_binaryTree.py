# [SWEA] 5176. 이진탐색
# 1. 반복문으로 이진 트리 생성
# 2. inorder 함수를 통해 순회하며 중위 순회 순서대로 값 저장
# 3. 요구 노드의 인덱스 => 해당 트리의 저장 값으로 취급

def inorder(node): # 이진트리 중위순회 하며 값 저장
  if not node:
    return
  inorder(left[node])
  tree.append(node)
  inorder(right[node])

for test_case in range(1, int(input())+1):
  V = int(input())
  left = [0] * (V+1)
  right = [0] * (V+1)
  tree = [0]
  
  for i in range(1, V): # 이진트리 생성
    if i*2 == V:
      left[i] = 2*i
      break
    if i*2+1 == V:
      left[i] = i*2
      right[i] = i*2+1
      break      
    left[i] = i*2
    right[i] = i*2+1
  
  inorder(1) # 중위순회
  
  print(f'#{test_case} {tree.index(1)} {tree.index(V//2)}')