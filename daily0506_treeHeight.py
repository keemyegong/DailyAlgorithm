# [SWEA] 14510. 나무 높이

# 수업 질문 및 정보 공유 코드

# 아이디어: 모든 나무의 1과 2씩 자라는 경우를 따져서 처리, 2씩 자라는 경우를 우선적으로 얻고 경우의 수를 두어서 처리
# 모든 나무의 2씩 자랄 수 있는 경우를 얻고 나머지로 1씩 자랄 수 있는 경우를 얻는다. (나머지 연산 이용)
#1) 1과 2로 자랄 수 있는 경우의 수가 모두 있는 경우, 쌍으로 묶어서 처리 1,2 -> 2일 걸림
#2-1) 1만 남은 경우: 경우의 수 * 2 - 1
#2-2) 2만 남은 경우: 4일(홀1짝2홀1짝2)에 3개의 나무를 처리할 수 있으므로 3으로 나누어서 경우의 수를 따짐
# 4일로 지정하여 처리한 이유는 각 날짜별 홀짝이라는 주기를 완성시켜서 처리해야 문제를 해석하는 데 용이하기 때문입니다
#2-2-1) 나머지가 1인 경우 mok * 4 + 2 (2가 자라야 하는 나무가 한 개 남았으므로 2일 소요)
#2-2-1) 나머지가 2인 경우 mok * 4 + 3 (2가 자라야 하는 나무가 두 개 남았으므로 3일 소요)

from collections import defaultdict

T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    trees = list(map(int, input().split()))
    max_h = max(trees)
    trees = [max_h-t for t in trees if max_h-t > 0]

    #2씩 자라는 경우와 1씩 자라는 경우 얻기 
    plant_len = defaultdict(int)
    for t in trees :
        mok, res = divmod(t, 2)
        plant_len[2] += mok
        plant_len[res] += 1

    min_n = min(plant_len[1], plant_len[2])
    result = min_n * 2 #1,2 크기의 쌍 식물 처리하기 위해 2일 필요
    plant_len[1] -= min_n
    plant_len[2] -= min_n
    
    #크기 1이 자라야하는 식물만 남은 경우
    if plant_len[1]>0 and plant_len[2]==0 :
        #2틀당 1개씩 식물완료
        result += plant_len[1]*2-1 
    #크기 2가 자라야하는 식물만 남은 경우
    elif plant_len[1]==0 and plant_len[2]>0 :
        #4일에 3개 식물 처리 (홀1짝2홀1짝2 주기 완성하기 위해 4일로 지정)
        mok, res = divmod(plant_len[2], 3)
        res_days = {0:0, 1:2, 2:3} 
        result += mok*4 + res_days[res]

    print(f'#{tc}', result)