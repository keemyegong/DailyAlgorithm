# [BAEKJOON] 10250. ACM 호텔

for _ in range(int(input())):
  h, w, n = map(int, input().split()) # 층, 높이, 손님 수
  
  for i in range(n):
    y = n % h # 방 번호 y 배정
    if y == 0: y = h
    x = n // h # 방 번호 x 배정
    if n % h > 0:
      x += 1
    y, x = str(y), str(x)

  if len(x) == 1: # 자릿수 맞추기
    x = '0' + x
  
  print(y+x)