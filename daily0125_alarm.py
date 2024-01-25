#백준 알고리즘 2884번
#입력받은 시간보다 45분 빠른 알람 시간 출력하기

h, m = map(int, input().split())

if h != 0:
  if m < 45:
    h -= 1
    m = m - 45 + 60
  else:
    m -= 45
else:
  if m < 45:
    h = 23
    m = m - 45 + 60
  else:
    h = 0
    m -= 45

if m == 60:
  m = 0

print(h, m)