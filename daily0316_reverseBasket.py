# [BAEKJOON] 10811. 바구니 뒤집기

n, m = map(int, input().split())
lst = list(range(1, n+1))

for _ in range(m):
  s, e = map(int, input().split())
  lst[s-1:e] = lst[s-1:e][::-1]

print(*lst)