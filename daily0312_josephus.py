# [BAEKJOON] 11866. 요세푸스 문제 0

from collections import deque

n, k = map(int, input().split())
lst = deque(range(1, n+1))
result = []

for _ in range(n):
  for i in range(k):
    num = lst.popleft()
    if i != k-1:
      lst.append(num)
  result.append(num)

print("<{}>".format(', '.join(map(str, result))))