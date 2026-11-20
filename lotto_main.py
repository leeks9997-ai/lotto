from lotto_utils import *

while True:
    try:
        count = int(input("몇 게임 할래? (1~10 사이)"))
        if 1 <= count <= 10:
            break
        print('1~10 사이로 입력해주세요')

    except ValueError:
        print('숫자 입력하세요')

games = make_games(count)

print('\n\n### 로또 번호 생성기 ###\n\n')
for i in range(count):
    print(f'게임 {i+1}: {to_text(games[i])}')