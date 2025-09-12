# 반환타입: O 매개변수: O 자판기
# 반환타입: O 매개변수: X 폴라로이드
# 반환타입: X 매개변수: O 모금함
# 반환타입: X 매개변수: X 리모콘

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








0
