# [BAEKJOON] 10814. 나이순 정렬

N = int(input())
users = []

for _ in range(N):
  age, name = input().split()
  users.append((int(age), name))

users = sorted(users, key = lambda x: x[0])
# 첫 번째 요소값을 기준으로 정렬

for user in users:
  print(*user)