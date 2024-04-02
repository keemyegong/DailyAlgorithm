import sys

string = sys.stdin.readline().strip() + ' '

stack = []
result = ''
check = 0

for s in string:
  if s == '<' or check == 1:
    if s == '<':
      check = 1
      while stack:
        result += stack.pop()
      result += '<'
    elif s == '>':
      check = 0
      result += s
    else:
      result += s
  elif s == ' ':
    while stack:
      result += stack.pop()
    result += ' '
  else:
    stack.append(s)

while stack:
  result += stack.pop()

print(result)