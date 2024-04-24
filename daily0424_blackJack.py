# [BAEKJOON] 2798. 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = 0
for num1 in range(N):
    for num2 in range(num1 + 1, N):
        for num3 in range(num2 + 1, N):
            if cards[num1] + cards[num2] + cards[num3] > M:
                continue
            result = max(result, cards[num1] + cards[num2] + cards[num3])

print(result)