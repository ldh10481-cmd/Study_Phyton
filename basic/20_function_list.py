# 반환타입: O 매개변수: O 자판기
def 토스트기(bread): # 선언 : 만들어만놨지 누가 사용한건 아님
    print(f'{bread} 가 구워진다.') # 실질적 동작이 아님, 사람눈에만 보이는거
    return f'구워진 {bread}' # 실제로 밖으로 나오는 값

# 반환타입: O 매개변수: X 폴라로이드
def 번호표기계():
    return "번호표"

print(번호표기계())
# 반환타입: X 매개변수: O 모금함
def 저금통(coin):
    print(f'{coin}원 저축')

#저금통(500)
# 저금통에는 return 이 없는데 저금통 실행후 나온값을 출력하려고 하니
# None 이 출력 되는 것
print(저금통(100))

# 반환타입: X 매개변수: X 리모콘
def 호출벨():
    print('호출벨이 울린다.')

호출벨()



#사용
#dish = 토스트기('종이') # return 으로 나온 값을 dish 에 담는다.
#print(dish) # dish 안의 값을 출력
print(토스티기('감자')) # 토스트기에서 나온 값을 바로 출력

#자판기
def vending(card):
    print(f'{card}로 결제했다')
    return f'{card}로 결제한 음료가 나왔다'

card = vending('카드')
print(card)

#폴라로이드
def polaroid():
     return ' 사진이 나온다'

print(polaroid())

#모금함
def box(cash):
    print(f'{cash}를 냈다')

box('10000원')

#리모콘
def remote():
    print(f'티비를켜다')

remote()

a=20
print()




