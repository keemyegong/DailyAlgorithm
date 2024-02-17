#  [SWEA] 5099. 피자 굽기

T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N: 오븐의 크기, M: 피자의 개수
    pizza = list(map(int, input().split())) # 피자 위 치즈의 양

    for i in range(M):
        pizza[i] = [i, pizza[i]] # 인덱스와 함께 저장 
 
    oven = [] # Queue
    for i in range(N):
        p = pizza.pop(0)
        oven.append(p) # 피자를 오븐에 넣고 시작
 
    while len(oven) != 1: # 오븐에 하나가 남을 때까지
        p = oven.pop(0)
        p[1] = p[1] // 2 # 치즈 녹이기
        if p[1] <= 0 and len(pizza) > 0: # 치즈가 0이고 남은 피자가 있으면
          oven.append(pizza.pop(0)) # 새로운 피자를 꺼내 오븐에 넣기
        else:
            oven.append(p) # 아니라면 꺼낸 피자를 다시 오븐에 넣기
 
    print(f'#{test_case} {oven[0][0]+1}') # 피자 인덱스 출력
