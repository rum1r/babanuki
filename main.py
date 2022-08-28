from typing import List, Dict, Union
import random


def create_initial_deck() -> List[str]:
    """トランプの53枚を用意するよ！"""
    initial_deck = []
    # 1〜13
    for n in range(1, 14):
        # egara（str）
        if n == 1:
            egara = 'A'
        elif n == 11:
            egara = 'J'
        elif n == 12:
            egara = 'Q'
        elif n == 13:
            egara = 'K'
        else:
            egara = str(n)
        initial_deck.append(egara)

    # 4 suit each card
    initial_deck = initial_deck * 4
    # add baba
    initial_deck.append('X')
    # 53 cards

    return initial_deck


def create_player(
    name: str, is_auto: bool = True
) -> Dict[str, Union[str, List[str], bool]]:
    """プレヤークラスだよ！"""
    return {
        'name': name,
        'deck': [],
        'is_win': False,
        'is_auto': is_auto,
    }


def initial_deal(initial_deck: List[str], *args: tuple) -> List[Dict]:
    """カードを配るよ！"""
    players = list(args)
    random.shuffle(initial_deck)
    q, mod = divmod(len(initial_deck), len(players))

    for i in range(len(players)):
        slice_n = q
        if i < mod:
            slice_n += 1
        players[i]['deck'] = initial_deck[:slice_n]
        del initial_deck[:slice_n]
    return players


def initial_putdown(deck: List[str]) -> List[str]:
    """揃ったカードを捨てるよ！"""
    while len(set(deck)) != len(deck):
        popped_card = deck.pop(0)
        if popped_card in deck:
            deck.remove(popped_card)
        else:
            deck.append(popped_card)
    return deck


def create_turn_index(passer_i, taker_i, players_count) -> tuple:
    """次に引かれる人, 引く人 を決定するよ！"""
    passer_i = taker_i
    taker_i = taker_i + 1
    if passer_i >= players_count:
        passer_i = 0
        taker_i = 1
    elif taker_i >= players_count:
        taker_i = 0
    return passer_i, taker_i


# 53枚のカードを作る
initial_deck = create_initial_deck()

# プレーヤーを作るよ
player1 = create_player('A')
player2 = create_player('B')
player3 = create_player('C')

# カードを配る
players = initial_deal(initial_deck, player1, player2, player3)

for player in players:
    # 2枚揃ったカードを捨てる
    initial_putdown(player['deck'])
    print(player['deck'])
