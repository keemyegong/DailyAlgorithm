# [BAEKJOON] 2751. 수 정렬하기 2

import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

for n in sorted(nums):
  print(n)