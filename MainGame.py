# 기본

import time
import random

import MiniGame
import Fight

dotori_total_num = random.randint(15,25)

games = ['가위바위보', '숫자 맞추기', '상식 퀴즈', '알맞은 대답 고르기', 'O,X 퀴즈'] * 5
random_game = random.sample(games,dotori_total_num)

item = ['꽃다발', '데구르르 나무바퀴', '핑크 거울', '바라바라바람', '민트초콜릿', '튼튼한 밧줄', '3시간 후 마감인 과제']
save_item = []

princess_strength = random.randint(400,500)
princess_attackp = 100

me_strength = random.randint(300, 400)
me_attackp = 100

me_body = ['팔', '얼굴', '무릎', '등', '손', '목']
random_me_body = random.choice(me_body)

princess_item = ['미용 가위', '분무기', '빗자루', '수건']

princess_item_attackp = [20, 10, 10, 0]

scissors = f'공주의 {princess_item[0]}에 {random_me_body}을 맞았습니다.'
water = f'공주가 {princess_item[1]}로 뿌린 물에 {random_me_body}가 젖었습니다.'
broom = f'공주의 {princess_item[2]}에 {random_me_body}을 맞았습니다.'
towel = f'공주의 {princess_item[3]}에 {random_me_body}을 맞았습니다.'

princess_attack = [scissors, water, broom, towel]
random_princess_attack = random.choice(princess_attack)
random_princess_attack_count = princess_attack.index(f'{random_princess_attack}')

situation_qs = ['당신은 개발자와 오늘 데이트를 한다. 어떤 선물을 들고 갈까?\n꽃다발(0) 케이크(1) 인형(2)', '도토리는 어떤 동물일까?\n고양이(0) 다람쥐(1) 판다(2)', '하늘에서 내려온 토~끼가 하는 말~\n움치치 움치치(0) 바니바니 바니바니(1) 으쌰으쌰 으쌰으쌰(2)', '개발자의 가장 큰 장점은 무엇일까?\n성격(0) 미모(1) 지성(2)', '와기는 누구일까?\n개발자 본인(0) 개발자가 좋아하는 아이돌(1) 개발자의 남자친구(2)']
situation_as = [2, 0, 0, 1, 2]

quiz_qs = ['이 게임의 개발자의 이름은? (ex. 김공주)', '이 게임의 개발자가 다니는 학교는? (ex. 미용실대학교)', '이 게임의 이름은?', '이 게임의 개발자의 2022년 기준 나이는? (ex. 10살)', '이 게임의 개발자의 생일은? (ex. 01월 01일)']
quiz_as = ['박혜리', '서울대학교', '공주의 미용실', '22살', '06월 15일']

ox_qs = ['개발자의 전공은 컴퓨터공학이다. (O/X)', '개발자는 도토리를 키운다. (O/X)', '개발자는 군필이다. (O/X)', '개발자는 놀고 먹는 것을 아주 좋아한다. (O/X)', '개발자는 지금 게임 코드를 짜는 게 귀찮다. (O/X)']
ox_as = ['X', 'X', 'X', 'O', 'O']



#INTRO

print('\ntip: press ENTER to continue')
input()
print('tip: do not press while loading')
input()
print('loading...')
time.sleep(2)
myname = input('\n이름: ')
print()
print('='*60)
print('\nloading...')
time.sleep(2)
print('\n룰루랄라~')
input()
print ('앗 이게 뭐지? 와기가 편지를 남기고 갔네?')
input()
print(f'''-//-------------------
|   {myname}에게,{" "*(10-len(myname))}|
|   낣졺왃섣굻햁줩   |
|   공주의 미용실    |
-------------------//-''')
input()
print('엥? 공주의 미용실? 와서 구해달라고?')
input()
print(f'|{myname}님은 지도를 획득하였습니다.|')
input()
print('오호... 여기 있는 길을 쭉 따라가다보면 나오는구만! 한 번 가볼까?')
input()
while True:
    print('모험을 떠나보시겠습니까? (yes/no)')
    quest = input('입력: ')
    if quest == 'yes':
        print('''
  ∧＿∧
（｡･ω･｡)つ━☆・*。
⊂　    ノ    ゜+.
　しーＪ　　　°。+ *´¨)
　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)
　　　　　　　　　　(¸.·´ (¸.·’*''')
        print('\n\n{{공주의 미용실~ >.<}}')
        input()
        print('START')
        input()
        break
    elif quest == 'no':
        print('\n왜 와기 안 구하러 가는뎅.. 뿌엥.. 다시해!!\n')
    else:
        print('\n장난치지 말고 똑바로 입력하라잉^^\n')


# 길 걷기

print('='*60)
print('\nloading...')
time.sleep(2)
print('''\n\n     O
    -|-
 ,,,/|\n''')
input()
print('''          O
         -|-
      ,,,/|\n''')
input()
print('''               O
              -|-
           ,,,/|\n''')
input()


# 도토리 대화

dotori_meet_num = 0

password = [ 0, 1, 2, 2, 4]
pass_num = 1

save_item = []

tissue_num = 0
tissueball_num = 0

while dotori_meet_num < dotori_total_num:
    MiniGame.walk()
    print(f'\n|{myname}님은 도토리를 마주쳤습니다.|')
    input()
    print('도토리와 대화를 하시겠습니까? (y/n)')
    dotori_talk = input('입력: ')
    if dotori_talk == 'y':
        print('\nloading...')
        time.sleep(1)
        print(f'\n{myname}님 ㅎㅇ~ 나랑 {random_game[dotori_meet_num]} 게임 해보실? 이기면 아이템 하나 드림~ (y/n)')
        dotori_game = input('입력: ')
        if dotori_game == 'y':
            if random_game[dotori_meet_num] == '가위바위보':
                print()
                save_item = MiniGame.rps_game(myname, item, save_item)
            if random_game[dotori_meet_num] == '숫자 맞추기':
                save_item = MiniGame.guessnum_game(myname, item, save_item)
            if random_game[dotori_meet_num] == '상식 퀴즈':
                save_item, quiz_qs, quiz_as = MiniGame.quiz_game(myname, item, save_item, quiz_qs, quiz_as)
            if random_game[dotori_meet_num] == '알맞은 대답 고르기':
                save_item, situation_qs, situation_as = MiniGame.situation_game(myname, item, save_item, situation_qs, situation_as)
            if random_game[dotori_meet_num] == 'O,X 퀴즈':
                save_item, ox_qs, ox_as = MiniGame.ox_game(myname, item, save_item, ox_qs, ox_as)
        else:
            print('\n싫음 말고~ ㅃㅇ~')
            input()
    else:
        print('\nㅃㅇ~\n')

    dotori_meet_num += 1

    if dotori_meet_num % 2 == 0:
        tissue_num, tissueball_num = MiniGame.tissue(myname, tissue_num, tissueball_num)

    if dotori_meet_num % 3 == 0:
        if pass_num < 5:
            print(f'\n|{myname}님은 미용실 문의 비밀번호를 획득하였습니다.|')
            input()
            print(f'|미용실 문 비밀번호의 {pass_num}째 자리 번호는 {password[pass_num]}입니다.|')
            input()
            pass_num += 1
else:
    print('\n어? 저기 앞에 미용실 보인다!')
    input()


#미용실 입장

MiniGame.walk()
print(f'\n|{myname}님은 미용실에 도착하였습니다.|\n')
input()

guesspass_num = 0

while guesspass_num < 2:
    print('삐빅. 비밀번호 4자리를 입력하시오.')
    guesspass = input('비밀번호: ')
    if guesspass == '1224':
        print('\nSUCCESS')
        input()
        print('|미용실 문이 열렸습니다.|')
        input()
        break
    else:
        print('\nFAIL')
        input()
        guesspass_num += 1
else:
    print('삐빅. 비밀번호 입력 허용 횟수 2회를 초과하였습니다.')
    input()
    print(f'|{myname}님은 와기를 구하지 못할 위기에 처했습니다.|')
    input()
    print(f'|만약 게임을 계속하고 싶다면 개발자에게 아부를 하여 비밀번호를 알아내시오.|')
    input()
    guesspass = input('비밀번호: ')
    if guesspass == '1224':
        print('\nSUCCESS')
        input()
        print('|미용실 문이 열렸습니다.|')
        input()
    else:
        print('\n바보구나?')
        input()
        print('|게임을 종료합니다.|')
        input()
        print('''
  ∧＿∧
（｡･ω･｡)つ━☆・*。
⊂　    ノ    ゜+.
　しーＪ　　　°。+ *´¨)
　　　　　　　　　.· ´¸.·*´¨) ¸.·*¨)
　　　　　　　　　　(¸.·´ (¸.·’*''')
        print('\n\n{{공주의 미용실~ >.<}}')
        input()
        print('END')

# 공주 대면

print('='*60)
print('\nloading...')
time.sleep(2)
print('\n으아아앙 살려줘어어ㅓ')
input()
print('헉 무슨 소리지?')
input()
print('소리가 나는 곳을 향해 다가가본다(0) 도망친다(1): ')
input('입력: ')
print(f'\n|{myname}님은 공주와 눈이 마주쳤습니다.|')
input()
print('너 뭐야???!!!! 어떻게 들어왔어???!!!!!')
input()
print('|공주가 미용 가위를 들고 다가옵니다.|')
input()
print('우에에에엥ㅇ 살려주세여어ㅓ어')
input()
print('이왕 이렇게 된 거... 어쩔 수 없지...')
input()
print('공주와 싸우시겠습니까? (y/n)')
fight_start = input('입력: ')
if not fight_start == 'y':
    print('\n왜? 무서워? 어차피 싸워야돼~ ^^')
    input()
else:
    print()


# 공주와 싸우기 intro

print('='*60)
print('\nloading...')
time.sleep(2)
print('\n|도토리들로부터 얻은 아이템들을 사용하여 공주와 싸울 수 있습니다.|')
input()
print(f'|{myname}님에게는 현재', end = " ")
for i in range(7):
    print(f'{item[i]} {save_item.count(item[i])}개,', end = " ")
print(f'휴지뭉치 {tissueball_num}개가 있습니다.|')
input()
print('FIGHT!')
input()
print('='*60)
print('\nloading...')
time.sleep(2)

print('\n|아이템 hint|')
input()
print('꽃다발 [선물]: 공주가 좋아함.')
input()
print('바라바라바람 [방어]: 공주의 무기를 날려버릴 수 있음.')
input()
print('핑크 거울 [방어 & 공격]: 공주의 미모를 반사하여 공주를 눈부시게 만듦.')
input()
print('민트초콜릿 [공격]: 공주는 반민초임.')
input()
print('튼튼한 밧줄 [공격]: 공주를 묶을 수 있음.')
input()
print('3시간 후 마감인 과제 [공격]: 공주의 주의를 돌림.')
input()
print('휴지뭉치 [공격 & 회복]: 공주에게 던지거나, 분무기 물을 닦아낼 수 있음.')
input()
print('데구르르 나무바퀴 [회복]: 공주에게 굴리면 공주가 약오르지만, 그동안 쉴 수 있음.')
input()
print('='*60)
print('\nloading...')
time.sleep(2)


# 공주와 싸우기

Fight.fight(myname, princess_strength, princess_attackp, me_strength, me_attackp, princess_item, princess_item_attackp, princess_attack, random_princess_attack, random_princess_attack_count, item, save_item, tissueball_num)
