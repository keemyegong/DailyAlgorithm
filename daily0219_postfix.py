# [SWEA] 1223. 계산기2

T = 10
 
for test_case in range(1, T+1):
  N = int(input())
  fx = input()

  result = ''
  stack = []

  pri = {'*': 2, '+': 1}

  # 후위 표기식 변환
  for i in fx:
      if i == '*' or i == '+': # 연산자일 때
          while stack and pri.get(stack[-1], 0) >= pri[i]:
              result += stack.pop() # 스택 원소보다 우선순위가 높지 않으면 스택 원소 pop
          stack.append(i) # stack에 i append
      else: # 피연산자면 result에 추가
          result += i

  while stack:
      result += stack.pop()

  # 후위 표기식 연산
  for i in result:
      if i == '*':
          a = stack.pop()
          b = stack.pop()
          stack.append(a*b)
      elif i == '+':
          a = stack.pop()
          b = stack.pop()
          stack.append(a+b)
      else:
          stack.append(int(i))

  result = stack.pop() # 최종 합산 결과 pop

  print(f'#{test_case} {result}')