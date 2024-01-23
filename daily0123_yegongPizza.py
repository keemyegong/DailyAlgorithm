#keemyegong 피자가게가 오픈했습니다. 손님들을 맞이해 봅시다.
  #1. customers 리스트에 있는 동물 손님들은 랜덤으로 방문합니다.
  #2. 피자는 일곱 조각으로 나갑니다. 피자를 나눠먹을 손님의 수 n이 주어질 때, 모든 동물 손님이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 함수를 작성하세요.
  #3. 피자의 수량은 총 10개입니다. 수량이 부족하면 경고 문구를 띄우고 영업을 종료하세요.
  
import random

customers = ['토끼', '고양이', '강아지', '호랑이', '알파카', '햄스터']

pizza_amount = 10

def eatPizza(n):
    if n // 7 == 0:
        pizza = 1
    elif n // 7 >= 1 and n % 7 >= 1:
        pizza = n // 7 + 1
    else:
        pizza = n // 7
    return pizza

visit_customer = random.choice(customers)

while True:
  n = int(input(f'안녕하세요, {visit_customer}님! 몇 명이서 오셨나요?'))
  if pizza_amount - eatPizza(n) < 0:
    print('피자가 부족해요!')
    break
  else:
    print(f'피자 {eatPizza(n)}개 나왔습니다! 맛있게 드세요.')
    pizza_amount -= eatPizza(n)