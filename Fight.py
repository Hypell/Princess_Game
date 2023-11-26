def fight(myname, princess_strength, princess_attackp, me_strength, me_attackp, princess_item, princess_item_attackp, princess_attack, random_princess_attack, random_princess_attack_count, item, save_item, tissueball_num):
    import GiveItem
    import random
    print('\n아니 어떻게 알고 왔어??? 감히 여기가 어디라고...')
    while len(save_item) + tissueball_num > 0 :
        if me_strength > 0:
            if princess_strength > 0:
                random_princess_attack = random.choice(princess_attack)
                random_princess_attack_count = princess_attack.index(random_princess_attack)
                input()
                print(f'|공주가 {princess_item[random_princess_attack_count]}를 휘둘렀습니다.| [공주 체력 -10] [공격력 +{princess_item_attackp[random_princess_attack_count]}]')
                princess_strength -= 10
                princess_attackp += princess_item_attackp[random_princess_attack_count]
                input()
                print(f'|{myname}님은 {random_princess_attack}| [{myname} 데미지 -{(princess_attackp/100)*10}]')
                me_strength -= (princess_attackp/100)*10
                input()
                print('아이템을 사용하시겠습니까? (y/n)')
                want_item_use = input('입력: ')
                if want_item_use == 'y':
                    print('\n어떤 아이템을 사용하시겠습니까?')
                    for i in range(7):
                        print(f'{item[i]} {save_item.count(item[i])}개({i})', end = " ")
                    print(f'휴지뭉치 {tissueball_num}개(7), 아이템 hint 다시 보기(8)')
                    item_use = int(input('입력: '))
                    print()
                    if item_use == 0:
                        save_item.remove(item[0])
                        print(f'|{myname}님은 공주에게 꽃다발을 건네주었습니다.| [{myname} 체력 -5]')
                        me_strength -= 5
                        input()
                        print('흠흠... 예쁘긴 하네... [공주 공격력 -20]|')
                        princess_attackp -= 20
                        continue
                    if item_use == 1:
                        save_item.remove(item[1])
                        print(f'|{myname}님은 공주에게 데구르르 나무바퀴를 굴렸습니다.| [{myname} 체력 -10] [{myname} 공격력 +10]')
                        me_strength -= 10
                        me_attackp += 10
                        input()
                        print(f'에잇 이게 뭐야? 으악! 이거 어케 멈춰!!!!!! 으 킹받아... [공주 데미지 -{(me_attackp/100)*10}] [공주 공격력 +20]|')
                        princess_strength -= (me_attackp/100)*10
                        princess_attackp += 20
                        input()
                        print(f'|{myname}님은 공주가 데구르르 나무바퀴를 피하는 동안 잠시 숨을 골랐습니다.| [공주 체력 -10] [{myname} 체력 +30]')
                        princess_strength -= 10
                        me_strength += 30
                        continue
                    if item_use == 2:
                        save_item.remove(item[2])
                        print(f'|{myname}님은 공주를 향해 핑크거울을 들었습니다.| [{myname} 체력 -5] [{myname} 공격력 +10]')
                        me_strength -= 5
                        me_attackp += 10
                        input()
                        print(f'아잇 눈부셔!!! 거울 속 내가 너무 빛나자나...?! [공주 데미지 -{(me_attackp/100)*30}]')
                        princess_strength -= (me_attackp/100)*30
                        continue
                    if item_use == 3:
                        save_item.remove(item[3])
                        print(f'|{myname}님은 공주를 향해 바라바라밤을 보냈습니다.| [{myname} 체력 -10] [{myname} 공격력 +20]')
                        me_strength -= 10
                        me_attackp += 20
                        input()
                        print(f'헉 내 {princess_item[random_princess_attack_count]}...?! [공주 공격력 -30]')
                        princess_attackp -= 30
                        continue
                    if item_use == 4:
                        save_item.remove(item[4])
                        print(f'|{myname}님은 공주의 입에 민트초콜릿을 넣어주었습니다.| [{myname} 체력 -5]')
                        me_strength -= 5
                        input()
                        print(f'우엑... [공주 데미지 -{(me_attackp/100)*30}]')
                        princess_strength -= (me_attackp/100)*30
                        continue
                    if item_use == 5:
                        save_item.remove(item[5])
                        print(f'|{myname}님은 공주를 튼튼한 밧줄로 묶었습니다.| [{myname} 체력 -20]')
                        me_strength -= 20
                        input()
                        print(f'으아아앙 뭐하는 거야! 시러시러... [공주 데미지 -{(me_attackp/100)*20}] [공주 공격력 -30]|')
                        princess_strength -= (me_attackp/100)*20
                        princess_attackp -= 30
                        continue
                    if item_use == 6:
                        save_item.remove(item[6])
                        print(f'|{myname}님은 공주에게 3시간 후에 마감인 과제가 있다고 알려주었습니다.| [{myname} 체력 -5]')
                        me_strength -= 5
                        input()
                        print(f'헉? 진짜? 헐 어케... 큰일났다... [공주 공격력 -10]')
                        princess_attackp -= 10
                        continue
                    if item_use == 7:
                        tissueball_num -= 1
                        print('공주에게 던지겠습니까? 아니면 젖은 옷을 닦겠습니까?')
                        select_tissue = int(input('던지기(0), 물 닦기(1): '))
                        if select_tissue == 0:
                            print(f'\n|{myname}님은 공주에게 휴지뭉치를 던졌습니다.| [{myname} 체력 -10] [{myname} 공격력 +5]')
                            me_strength -= 10
                            me_attackp += 5
                            input()
                            print(f'아야!! 생각보다 아프자나? [공주 데미지 -{(me_attackp/100)*10}]')
                            princess_strength -= (me_attackp/100)*10
                        elif select_tissue == 1:
                            print(f'\n|{myname}님은 휴지뭉치로 공주가 뿌린 분무기 물 때문에 젖은 옷을 닦았습니다.| [{myname} 공격력 +10]')
                            me_attackp += 10

                        continue
                    if item_use == 8:
                        GiveItem.item_hint()
                        continue
                    
                    return save_item
            else:
                input()
                print(f'|{myname}님은 공주와의 싸움에서 승리하였습니다.|')
                input()
                print(f'|{myname}님은 공주로부터 와기를 구하였습니다.|')
                input()
                print(f'|와기는 {myname}님 덕분에 이발을 하지 않아도 되었답니다~|')
                input()
                print('허무하다고요? 조금... 그럴지도...')
                break
        else:
            input()
            print(f'|{myname}님은 공주와의 싸움에서 패배하였습니다.|')
            input()
            print(f'|안타깝지만 {myname}님은 와기를 구하지 못하였습니다.|')
            input()
            print(f'|{myname}님은 공주에게 붙잡혀 와기와 함께 아주 예쁘게 이발을 당하였습니다.|')
            input()
            print('오히려 좋을지도...?')
            break
            
    else:
        input()
        print(f'\n|{myname}님은 아이템을 모두 사용하였습니다.|')
        input()
        print(f'|{myname}님은 공주와의 싸움에서 패배하였습니다.|')
        input()
        print(f'|안타깝지만 {myname}님은 와기를 구하지 못하였습니다.|')
        input()
        print(f'|{myname}님은 공주에게 붙잡혀 와기와 함께 아주 예쁘게 이발을 당하였습니다.|')
        input()
        print('오히려 좋을지도...?')    

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