def give_item(myname, item, save_item):
    import random

    new_item = random.choice(item)
    print(f'|아이템: {new_item}|')
    input()

    save_item.append(new_item)
    print(f'|{myname}님은 {new_item}을/를 {save_item.count(new_item)}개 획득하였습니다.|')
    input()

    return save_item

def item_hint ():
    print('\n|아이템 hint|')
    input()
    print('꽃다발 [선물]: 공주가 좋아함.')
    print('바라바라바람 [방어]: 공주의 미용 가위를 날려버릴 수 있음.')
    print('핑크 거울 [방어 & 공격]: 공주의 미모를 반사하여 공주를 눈부시게 만듦.')
    print('민트초콜릿 [공격]: 공주는 반민초임.')
    print('튼튼한 밧줄 [공격]: 공주를 묶을 수 있음.')
    print('3시간 후 마감인 과제 [공격]: 공주의 주의를 돌림.')
    print('휴지뭉치 [공격 & 회복]: 공주에게 던지고, 분무기 물을 닦아낼 수 있음.')
    print('데구르르 나무바퀴 [회복]: 공주에게 굴리면 공주가 약오르지만, 그동안 쉴 수 있음.')