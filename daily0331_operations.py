# [SWEA] 1232. 사칙연산

def inorder(node):
  if node != 0:
    inorder(left[node])
    inorder(right[node])
    calc.append(node)

for test_case in range(1, 11):
  N = int(input())

  tree = [0] * (N+1)
  left = [0] * (N+1)
  right = [0] * (N + 1)

  for _ in range(N):
    node_info = input().split()
    if len(node_info) > 2:
      tree[int(node_info[0])] = node_info[1]
      left[int(node_info[0])] = int(node_info[2])
      right[int(node_info[0])] = int(node_info[3])
    else:
      tree[int(node_info[0])] = node_info[1]

  calc = []
  inorder(1)

  stack = []

  for i in calc:
    if tree[i] == '*':
      a = stack.pop()
      b = stack.pop()
      stack.append(a * b)
    elif tree[i] == '+':
      a = stack.pop()
      b = stack.pop()
      stack.append(a + b)
    elif tree[i] == '-':
      a = stack.pop()
      b = stack.pop()
      stack.append(b - a)
    elif tree[i] == '/':
      a = stack.pop()
      b = stack.pop()
      stack.append(b//a)
    else:
      stack.append(int(tree[i]))

  print(f'#{test_case}', stack.pop())