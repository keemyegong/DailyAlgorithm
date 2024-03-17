# [BAEKJOON] 24511. queuestack

import sys
from collections import deque

n = int(input()) # 자료구조 개수
qs = list(map(int, sys.stdin.readline().split())) # 큐/스택 판별 리스트
nums = list(map(int, sys.stdin.readline().split())) # 각 자료구조에 든 원소 리스트
m = int(input()) # 삽입할 수열 길이
per = list(map(int, sys.stdin.readline().split())) # 삽입할 수열 리스트
result = deque() # 결과 리스트

for i in range(n):
  if qs[i] == 1: # 자료구조가 스택이라면 패스 (후입선출이므로 값이 변하지 않음)
    pass
  else: # 큐라면
    result.appendleft(nums[i]) # 주어진 수열을 result의 왼쪽에 하나씩 삽입

for i in range(m): # 수열의 길이만큼
  result.append(per[i]) # result의 끝에 수열 원소 삽입
  print(result.popleft(), end=' ') # result의 왼쪽에서부터 하나씩 pop