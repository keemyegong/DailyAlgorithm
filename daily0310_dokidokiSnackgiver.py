
# [BAEKJOON] 12789. 도키도키 간식드리미

n = int(input())
line = list(map(int, input().split()))[::-1] # 대기열
stack = []

taker = 1 # 간식 받을 순번
while True:
  if not line or (line and line[-1] != taker):
    # 줄이 비어있거나 줄의 마지막 순번이 taker가 아닐 경우
    if stack and stack[-1] == taker:
      # 스택의 마지막 순번이 taker라면
      stack.pop() # 스택에서 제거
      taker += 1 # taker 순번 1 증가
    elif line: # line에 남은 사람이 있다면
      stack.append(line.pop()) # 스택에 추가
    else: # 모든 경우에 해당되지 않는다면
      result = "Sad"
      break
  elif line and line[-1] == taker:
    # 줄의 마지막 순번이 takeㄱ일 경우
    line.pop() # 줄에서 제거
    taker += 1 # taker 순번 1 증가
  if taker > n: # taker 순번이 n을 넘어섰을 경우
    result = "Nice"
    break

print(result)