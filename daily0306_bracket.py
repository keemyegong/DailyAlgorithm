# [BAEKJOON] 9012. 괄호

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
  matching_list = []
  matching = input().strip()
  
  result = 'YES'
  
  for m in matching:
    if m == '(':
      matching_list.append('(')
    elif m == ')':
      if len(matching_list) > 0:
        matching_list.pop()
      else:
        result = 'NO'
        break

  if matching_list:
    result = 'NO'

  print(result)