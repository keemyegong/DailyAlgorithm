# [BAEKJOON] 1920. 수 찾기
# 이분탐색 이용 풀이

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split())) # 참조 리스트
nums.sort()

M = int(input())
find_nums = list(map(int, input().split())) # 찾을 수 리스트

for num in find_nums: # 찾을 수 리스트에서 순회
  result = 0 # 결과 값
  start = 0 # 시작 인덱스
  end = N - 1 # 종료 인덱스
  while start <= end: # 시작 인덱스가 종료 인덱스보다 작거나 같을 동안
    mid = (start + end) // 2 # 중간값 인덱스 설정
    if num == nums[mid]: # 값을 찾았다면 결과값 1 할당하고 종료
      result = 1
      break
    elif num > nums[mid]: # 찾는 값이 중간값보다 크다면 시작값 재설정
      start = mid + 1
    else: # 찾는 값이 중간값보다 작다면 종료값 재설정
      end = mid - 1
  
  print(result)