# [BAEKJOON] 1032. 명령 프롬프트

N = int(input())

result = list(input())

for _ in range(N-1):
    command = input()
    for i in range(len(command)):
        if result[i] != command[i]:
            result[i] = '?'

print(('').join(result))