# [BAEKJOON] 2480. 주사위 세 개

dices = list(map(int, input().split()))
arr = [0] * 7
arr = [arr[dice] + 1 for dice in dices]

if 3 in arr:
    prize = 10000 + (arr.index(3) * 1000)
elif 2 in arr:
    prize = 1000 + (arr.index(2) * 100)
else:
    prize = max(dices) * 100

print(prize)