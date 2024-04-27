# [BAEKJOON] 25304. 영수증

recipt = int(input())
total = 0

for _ in range(int(input())):
    price, num = map(int, input().split())
    total += price * num

if total != recipt:
    print('No')
else:
    print('Yes')