def rps_game(myname, item, save_item):
    import random
    import GiveItem
    dotori_rps = random.randint(0,2)
    print('가위~바위~보~!')
    me_rps = int(input('가위(0), 바위(1), 보(2): '))
    if me_rps > 2:
        print('\n가위(0), 바위(1), 보(2) 중에서 고르시죠 ^^')
        input()
        rps_game(myname, item, save_item)
    elif me_rps == dotori_rps:
        print('\n비겼어요 개굴. 다시 해봐여.')
        input()
        rps_game(myname, item, save_item)
    elif me_rps - dotori_rps ==1 or dotori_rps - me_rps == 2:
        print('\n앗 제가 졌네요.. 아이템 하나 드릴게요...')
        input()
        GiveItem.give_item(myname, item, save_item)
    else:
        print('\n제가 이겼네요! 안녕히가세요~')
        input()
        print(f'|{myname}님은 아이템 획득에 실패하였습니다.|')
        input()

    return save_item
    
def guessnum_game(myname, item, save_item):
    import random
    import GiveItem
    dotori_guess = random.randint(1,15)
    print('\n1에서 15 사이의 숫자 중 제가 생각하고 있는 숫자를 맞춰보세요~~ 기회는 3번!')
    guess_count=0
    while guess_count < 3:
        try:
            me_guess = int(input('입력: '))
        except:
            continue
        guess_count += 1
        if me_guess > dotori_guess:
            print('\n제가 생각한 숫자는 더 낮아요!')
        elif me_guess < dotori_guess:
            print('\n제가 생각한 숫자는 더 높아요!')
        else:
            print('\n정답입니다! 축하해요~ 아이템 하나 드릴게요!')
            input()
            GiveItem.give_item(myname, item, save_item)
            break

    else: 
        print('\n죄송해요... 안녕히가세요~')
        input()
        print(f'|{myname}님은 아이템 획득에 실패하였습니다.|')
        input()
    
    return save_item

def ox_game(myname, item, save_item, ox_qs, ox_as):
    import random
    import GiveItem
    print('\n어서와~ O,X 퀴즈 한 번 풀어봐~')
    input()

    ox_q = random.choice(ox_qs)
    print(ox_q)

    ox_q_count = ox_qs.index(ox_q)

    ox_a = input('입력: ')

    if ox_a == ox_as[ox_q_count]:
        print('\n맞췄네~! 여기 아이템~')
        input()
        GiveItem.give_item(myname, item, save_item)
    else:
        print('\n안타깝네.. 안녕~')
        input()
        print(f'|{myname}님은 아이템 획득에 실패하였습니다.|')
        input()
    ox_qs.remove(ox_q)
    ox_as.remove(ox_as[ox_q_count])
    
    return save_item, ox_qs, ox_as

def quiz_game(myname, item, save_item, quiz_qs, quiz_as):
    import random
    import GiveItem
    print('\n상식 퀴즈! 예시의 형식에 맞게 답해봥~')
    input()
    print('기회는 한 번밖에 없으니 잘 생각해보라궁~!')
    input()

    quiz_q = random.choice(quiz_qs)
    print(quiz_q)

    quiz_q_count = quiz_qs.index(quiz_q)

    quiz_a = input('입력: ')
    if quiz_a == quiz_as[quiz_q_count]:
        print('\n오! 정답! 아이템 하나 줄겡~')
        input()
        GiveItem.give_item(myname, item, save_item)
    else:
        print('\n이걸 몰라..? 잘 가...')
        input()
        print(f'|{myname}님은 아이템 획득에 실패하였습니다.|')
        input()

    quiz_qs.remove(quiz_q)
    quiz_as.remove(quiz_as[quiz_q_count])

    return save_item, quiz_qs, quiz_as

def situation_game(myname, item, save_item, situation_qs, situation_as):
    import random
    import GiveItem
    print('\n이제부터 넌 질문을 보고 개발자가 원하는 답을 골라야 한다.')
    input()
    print('왜냐고? 그건 개발자의 마음이니까.^^')
    input()

    situation_q = random.choice(situation_qs)
    print(situation_q)

    situation_q_count = situation_qs.index(situation_q)

    situation_a = int(input('입력: '))


    if situation_a > 2:
        print('\n0, 1, 2 중에 골라야 한다. 다시!')
    elif situation_a == situation_as[situation_q_count]:
        print('\n아쉽지만 맞췄다. 아이템을 받아서 떠나라.')
        input()
        GiveItem.give_item(myname, item, save_item)
    else:
        print('\n큭큭. 아직 뭘 모르는구나.')
        input()
        print(f'|{myname}님은 아이템 획득에 실패하였습니다.|')
        input()

    situation_qs.remove(situation_q)
    situation_as.remove(situation_as[situation_q_count])

    return save_item, situation_qs, situation_as

def tissue(myname, tissue_num, tissueball_num):
    print(f'\n|{myname}님은 길에서 휴지를 발견하였습니다.|')
    input()
    print('휴지를 주우시겠습니까? (y/n)')
    tissue = input('입력: ')
    if tissue == 'y':
        tissue_num += 1
        print(f'\n|{myname}님은 휴지를 {tissue_num}장 획득하였습니다.|')
        input()
        if tissue_num % 5 == 0:
            print('\n휴지 5장으로 휴지뭉치를 1개 만드시겠습니까? (y/n)')
            tissueball = input('입력: ')
            if tissueball == 'y':
                tissueball_num += 1
                tissue_num = 0
                print(f'\n|{myname}님은 휴지뭉치를 {tissueball_num}개 획득하였습니다.|')
                input()
    else:
        input()   
    
    return tissue_num, tissueball_num

def walk():
    import time
    print('='*60)
    print('\nloading...')
    time.sleep(2)
    print('\n\n뚜벅뚜벅...')
    input()