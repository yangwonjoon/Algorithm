
N = int(input())
current_cards = list(map(int, input().split()))
M = int(input())
target_cards = list(map(int, input().split()))

card_dict = {}

for card in current_cards:
    if(card in card_dict):
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for card in target_cards:
    print(card_dict[card], end=' ')



