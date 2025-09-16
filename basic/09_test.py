import random

number = random.randint(1,31) #1에서부터 31 사이의 숫자 # 1~31 까지의 숫자를 랜덤하게 뽑아서 number에 대입
print(f' 내 마음속 숫자: {number}') #1에서 31 사이의 숫자 중 하나
running = True #끊임없이 실행된다 # running 에 True 대입 #

# while 은 오른쪽에 있는 조건 결과가 True 일 경우 반복되는 구문
# running 이 초기에 True 이므로 무조건 실행되는 구조
while running:
    # 입력받은 값을 정수(int) 로 변환하여 guess 에 대입
    guess = int(input('1~31 중 내가 생각한 숫자는?'))
    print(f'입력받은 숫자 : {guess}')
    if number > guess: # 숫자가 추측보다 큰 경우 # number 가 guess 보다 크다면? 아래 내용 출력
        print('내가 생각한 숫자보다 작습니다.')
    elif number < guess: # 숫자가 추측보다 작은 경우 # number 가 guess 보다 작다면? 아래 내용 출력
        print('내가 생각한 숫자보다 큽니다.')
    else: # number 와 guess 가 서로 크지도 작지도 않으면? 아래 내용 출력
        print('정답입니다.')
        running = False #끊임없이 실행되는 것을 멈추기 위해서 False # running 변수는 False 값으로 바뀌게 된다.