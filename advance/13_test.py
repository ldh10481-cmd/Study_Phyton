while True:
    try:
        text = input('값을 넣으면 숫자로 변환 됩니다.')
        num = int(text)
        print(f'당신이 입력한 값:{num} 이 숫자로 변환 되었습니다.')
        break
    except ValueError:
        print(f'{text} 는 숫자가 아닙니다.')








# try:
#     text = input('값을 넣으면 숫자로 변환 됩니다.')
#     num = int(text)
#     print(f'당신이 입력한 값 : {num} 이 숫자로 변환 되었습니다.')
# except ValueError:
#     print('숫자를 입력해주세요.')
# finally:
#     print('끝')
