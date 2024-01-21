num_of_animal = 0
num_of_food = 100

name = ['고양이', '강아지', '토끼', '호랑이', '여우']
eat = [10, 13, 7, 31, 22]

def create_dict(name, eat):
    user_dict = {'name': name, 'eat': eat}
    print(f'{name}가 방문했어요!')
    return user_dict
#동물들의 정보를 딕셔너리 형태로 담는 함수

many_animal = list(map(create_dict, name, eat))
#map을 통해 동물들의 정보를 각각 딕셔너리 형태로 담아 many_animal에 할당하고 안내 문구 출력

nums = range(len(name))
info = list(map(lambda x: {'name': many_animal[x]['name'], 'eat': many_animal[x]['eat']}, nums))

def total_food(num):
    global num_of_food
    num_of_food -= num
    print('남은 밥의 수 :', num_of_food, 'kg')
#eat_food에서 개수를 인자로 받아 남은 밥의 수에서 인자만큼 수 차감

def eat_food(info):
    for i in nums:
        eating = eat[i]
        print(f'{info[i]['name']}가 {eating}kg의 밥을 먹고 갑니다.')
        total_food(eating)
#대여 개수를 계산해 출력
#total_food 함수에 섭취 kg을 인자로 넘기고 남은 kg 출력

eat_food(info)