# [BAEKJOON] 4949. 균형 잡힌 세상

while True:
  string = input()
  result = 'yes'
  stack = []
  if string == '.':
    break
  for s in string:
    if s in '[(':
      stack.append(s)
    elif s in '])':
      if stack:
        s2 = stack.pop()
        if s == ']' and s2 != '[':
          result = 'no'
          break
        elif s == ')' and s2 != '(':
          result = 'no'
          break
        else:
          result = 'no'
          break
    elif s == '.':
      break

  if stack:
    print('no')
  else:
    print(result)